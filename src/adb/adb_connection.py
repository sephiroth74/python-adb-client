#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import os
import re
import shutil
import subprocess
import time
from typing import List, Optional, Dict

import zope.event

from . import events

__all__ = ['Device', 'ADBCommandResult', 'get_adb_path', 'set_adb_path', 'which', 'execute', 'capture_output', 'shell',
           'wait_for_device', 'root', 'unroot', 'is_root', 'devices', 'is_connected', 'connect', 'disconnect_all', 'disconnect',
           'reboot', 'remount_as', 'remount', 'busybox', 'bugreport', 'mdns_check', 'version', 'mdns_services']

adb_path = None


class Device(object):
    """
    Represententation of a device, as listed from 'adb devices -l'
    """

    def __init__(self, identifier: str, attrs: Dict[str, str]):
        super(Device, self).__init__()
        self._identifier = identifier
        self._attrs = attrs

    @property
    def identifier(self):
        return self._identifier

    @property
    def transport_id(self):
        return self._attrs['transport_id']

    def is_usb(self) -> bool:
        """
        Return true if the attached device is connected through USB
        :return:
        """
        return 'usb' in self._attrs

    def is_emulator(self) -> bool:
        """
        Return true if the attached device is an emulator
        :return:
        """
        return self._identifier.startswith('emulator-')

    def is_wifi(self) -> bool:
        """
        Return true if the attached device is connected through wi-fi
        :return:
        """
        if not self.is_usb() and not self.is_emulator():
            return re.match(Device.PATTERN_IP, self._identifier) is not None
        return False

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        if item in self._attrs:
            return self._attrs[item]
        return None

    def __str__(self):
        string = f"Device(id={self._identifier},"
        for key, value in self._attrs.items():
            string += f"{key}={value},"
        string += ")"
        return string

    PATTERN_LINE = re.compile("^([^\\s]+)\\s+device\\s+(.*)$")
    PATTERN_ATTR = re.compile("(\\w+:\\w+)")
    PATTERN_IP = re.compile(
        "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):[0-9]+$")

    @staticmethod
    def parse(string: str) -> Optional[Device]:
        match1 = re.match(Device.PATTERN_LINE, string)
        if match1:
            device_id = match1.group(1)
            attrbutes = match1.group(2)
            device_attr = dict(map(lambda x: x.split(':'), re.findall(Device.PATTERN_ATTR, attrbutes)))
            return Device(device_id, device_attr)
        else:
            log().warning(f"Failed to parse device string {string}")
            return None


class ADBCommandResult(object):
    RESULT_OK = 0

    def __init__(self, result: Optional[str], code: int):
        super(ADBCommandResult, self).__init__()
        self._result = result
        self._code = code

    def __iter__(self):
        return (self._result, self._code).__iter__()

    def __str__(self):
        return f"Result(code={self._code}, result={self._result})"

    @property
    def code(self):
        """
        Error Code returned. if '0' it means no error
        :return:
        """
        return self._code

    @property
    def result(self): return self._result


def log():
    from . import _logger
    logger = _logger.get_logger(__name__)
    return logger


def get_adb_path() -> str:
    """
    Attempts to retrieve the current adb path from the system environment
    :return:
    """
    global adb_path
    if adb_path is None:
        adb_path = shutil.which("adb")

        # if adb_path is None:
        #     from libs2 import platform
        #     adb_path = platform.get_platform().get_adb_path()

        log().debug(f"Found adb: {adb_path}")

    assert adb_path
    return adb_path


def set_adb_path(path: str):
    """
    Set the global adb path
    :param path: absolute adb path
    """
    global adb_path
    adb_path = path


def which(command: str, ip: Optional[str] = None) -> Optional[str]:
    """
    Execute 'which' command on the specified device and return the result
    :param command:     command to test with 'which'
    :param ip:   device ip
    :return: the command path on the device, if found
    """
    result = shell(f"which {command}", ip=ip)
    if result.code == ADBCommandResult.RESULT_OK:
        return result.result
    return None


def execute(command: str,
            ip: Optional[str] = None,
            *args,
            **kwargs) -> bool:
    """
    Execute an adb command on the given device, if connected
    :param command:     command to execute
    :param ip:   device ip
    :param args:        optional list of arguments to pass to command
    :param kwargs:
    :return:
    """
    ip_arg = f"-s {ip} " if ip else ""
    adb = get_adb_path()
    final_command = "{} {}{}".format(adb, ip_arg, (command % args)).split()
    command_log = "{} {}{}".format(os.path.basename(adb), ip_arg, (command % args)).split()
    output = subprocess.PIPE if "stdout" not in kwargs else kwargs["stdout"]

    try:
        log().spam(f"Executing `{' '.join(command_log)}`")
        out = subprocess.Popen(final_command, stderr=subprocess.STDOUT, stdout=output)
        result = out.communicate()
        if not command == "get-state":
            log().spam(
                "Result: `%s` (code:%s)" % (
                    result[0].decode("utf-8").strip() if result[0] else "None",
                    out.returncode)
            )
        return out.returncode == ADBCommandResult.RESULT_OK
    except subprocess.CalledProcessError:
        return False


def capture_output(command: str, ip: Optional[str] = None, **kwargs) -> ADBCommandResult:
    """
    Execute an adb command on the given device and return the result
    :param command:         command to execute
    :param ip:       device address ip
    :param kwargs:
    :return:
    """
    ip_arg = f"-s {ip} " if ip else ""
    adb = get_adb_path()
    command1 = "{} {}{}".format(adb, ip_arg, command).split()
    command_log = "{} {}{}".format(os.path.basename(adb), ip_arg, command).split()
    try:
        log().spam("Executing `%s`" % " ".join(command_log))
        out = subprocess.Popen(
            command1,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            shell=kwargs.get("shell", False),
        )
        result = out.communicate()
        return ADBCommandResult(result[0].decode("utf-8").strip(), out.returncode)
    except subprocess.CalledProcessError as e:
        log().warning(e)
        return ADBCommandResult(None, 1)


def shell(command: str, ip: Optional[str] = None) -> ADBCommandResult:
    """
    Execute a command in the adb shell
    :param command:         shell command to execute
    :param ip:              device ip
    :return: result, code
    """
    ip_arg = f"-s {ip} " if ip else ""
    adb = get_adb_path()
    base_command = f"{adb} {ip_arg} shell {command}".split()
    command_log = f"{os.path.basename(adb)} {ip_arg} shell {command}".split()
    log().spam(f"Executing `{' '.join(command_log)}`")

    out = subprocess.Popen(
        base_command,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        shell=False,
    )
    result = out.communicate()
    return ADBCommandResult(result[0].decode("UTF-8").strip(), out.returncode)


def busybox(command: str, ip: Optional[str] = None) -> ADBCommandResult:
    """
    Executes a shell command using 'busybox'. If busybox in not installed on the device it will fail.\n
    See https://busybox.net/

    :param command:         the busybox command to execute
    :param ip:              device ip
    :return:                command result
    """
    return shell(f"busybox {command}", ip=ip)


def wait_for_device(ip: Optional[str] = None) -> bool:
    """
    Execute and return the result of 'adb wait-for-device'
    :param ip:              device ip
    :return:                true if device connects
    """
    if is_connected(ip=ip):
        return True

    execute(
        "wait-for-device shell 'while [[ -z $(getprop sys.boot_completed) ]]; do sleep 1; done; input keyevent 143'",
        ip=ip)

    return is_connected(ip=ip)


def root(ip: Optional[str] = None) -> bool:
    """
    Restart adb connection as root
    :param ip:              device ip
    :return:                true if root succeded
    """
    if is_root(ip=ip):
        return True
    execute("root", ip=ip)
    wait_for_device(ip=ip)
    return is_root(ip=ip)


# noinspection SpellCheckingInspection
def unroot(ip: Optional[str] = None) -> bool:
    """
    Restart adb as unroot
    :param ip:              device ip
    :return:                True on success
    """
    if not is_root(ip=ip):
        return True

    execute("unroot", ip=ip)
    wait_for_device(ip=ip)
    return not is_root(ip=ip)


def is_root(ip: Optional[str] = None) -> bool:
    """
    Test if adb connection is running as root
    :param ip:              device ip
    :return:                True if adb is running as root
    """
    result, code = shell("whoami", ip=ip)
    return result == "root"


def devices() -> List[Device]:
    """
    Return a list of attached devices
    :return:
    """
    result = capture_output("devices -l")
    if result.code == ADBCommandResult.RESULT_OK and result.result:
        attached_devices = list(map(lambda x: x.split("\t")[0], result.result.split("\n")[1:]))
        result = list(filter(lambda y: y is not None, map(lambda x: Device.parse(x), attached_devices)))
        return result
    else:
        return []


def is_connected(ip: Optional[str] = None) -> bool:
    """
    Returns true if the given device is connected
    :param ip:  device ip
    :return: true if connected
    """
    result = capture_output("get-state", ip=ip)
    log().spam(result)
    return result.code == ADBCommandResult.RESULT_OK and result.result == "device"


def connect(ip: str) -> bool:
    """
    Attempts to connect to the device with the given ip address
    :param ip: device ip
    :return: true if connection succeed
    """
    log().debug(f"Connecting to {ip}..")

    if is_connected(ip=ip):
        log().notice("Already connected...")
        return True

    try:
        out = subprocess.Popen(
            f"{get_adb_path()} connect {ip}",
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            shell=True,
        )
        result = out.communicate()  # noqa: F841
        time.sleep(50 / 1000)
        if out.returncode == 0 and is_connected(ip):
            zope.event.notify(events.ADBEvent(events.ADBConnectionEvent.Connect, ip))
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False


def disconnect_all() -> bool:
    """
    Disconnect all connected devices
    :return: true if successfully disconnected from all devices
    """
    log().verbose("Disconnecting from everything..")
    if execute("disconnect"):
        zope.event.notify(events.ADBEvent(events.ADBConnectionEvent.Disconnect, None))
        return True
    return False


def disconnect(ip: str) -> bool:
    """
    Disconnect from the given device ip
    :param ip: device ip
    :return: true if successfully disconnected
    """
    log().verbose(f"Disconnecting from {ip}..")
    if execute("disconnect", ip=ip):
        zope.event.notify(events.ADBEvent(events.ADBConnectionEvent.Disconnect, ip))
        return True
    return False


def reboot(ip: Optional[str] = None) -> bool:
    """
    Reboot the device
    :param ip:              device ip
    :return:                True on success
    """
    if execute("reboot", ip=ip):
        zope.event.notify(events.ADBEvent(events.ADBConnectionEvent.Reboot, ip))
        return True
    return False


def remount(ip: Optional[str] = None) -> bool:
    """
    Remount the file system if root is permitted
    :param ip:              device ip
    :return:                True on success
    """
    if not is_root(ip=ip):
        if not root(ip=ip):
            return False
    return execute("remount", ip=ip)


def remount_as(ip: Optional[str] = None,
               writeable: bool = False, folder: str = "/system") -> bool:
    """
    Mount/Remount file-system
    :param folder:          folder to mount
    :param writeable:       mount as writeable or readable-only
    :param ip:              device ip
    :rtype:                 true on success
    """
    if not is_root(ip=ip):
        if not root(ip=ip):
            return False
    if writeable:
        return shell(f"mount -o rw,remount {folder}", ip=ip).code == ADBCommandResult.RESULT_OK
    else:
        return shell(f"mount -o ro,remount {folder}", ip=ip).code == ADBCommandResult.RESULT_OK


def version() -> Optional[str]:
    """
    Fetch and return the current adb version
    :return: the output as returned by 'adb version'
    """
    result = capture_output("version")
    if result.code == ADBCommandResult.RESULT_OK:
        return result.result
    return None


def mdns_services() -> ADBCommandResult:
    """
    Return the result of the command 'adb mdns services'
    :return:
    """
    return capture_output("mdns services")


def mdns_check() -> ADBCommandResult:
    """
    Return the result of the command 'adb mdns check'
    :return:
    """
    return capture_output("mdns check")


def bugreport(dest: Optional[str] = None, ip: Optional[str] = None) -> bool:
    """
    Execute and return the result of the command 'adb bugreport'
    :param dest:    optional target local folder/filename for the bugreport
    :param ip:      optional device ip
    :return:        true on success
    """
    return execute(f"bugreport {dest}", ip=ip)
