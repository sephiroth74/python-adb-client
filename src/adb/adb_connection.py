#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import os
import re
import shutil
import subprocess
import time
from typing import List, Optional, Dict, Tuple

import zope.event

from . import events

__all__ = ['Device', 'get_adb_path']

adb_path = None


class Device(object):
    """
    Represententation of a device, as listed from 'adb devices -l'
    """

    def __init__(self, identifier: str, attrs: Dict[str, str]):
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


def which(command: str,
          ip: Optional[str] = None,
          transport_id: Optional[str] = None) -> Optional[str]:
    """
    Execute 'which' command on the specified device and return the result
    :param command:     command to test with 'which'
    :param ip:   device ip
    :param transport_id:   device transport id
    :return: the command path on the device, if found
    """
    result, code = shell(f"which {command}", ip=ip, transport_id=transport_id)
    if code == 0:
        return result
    return None


def execute(command: str,
            ip: Optional[str] = None,
            transport_id: Optional[str] = None,
            *args,
            **kwargs) -> bool:
    """
    Execute an adb command on the given device, if connected
    :param command:     command to execute
    :param ip:   device ip
    :param transport_id:   device transport id
    :param args:        optional list of arguments to pass to command
    :param kwargs:
    :return:
    """
    ip = f"-s {ip} " if ip else f"-t {transport_id} " if transport_id else ""
    adb = get_adb_path()
    final_command = "{} {}{}".format(adb, ip, (command % args)).split()
    command_log = "{} {}{}".format(os.path.basename(adb), ip, (command % args)).split()
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
        return out.returncode == 0
    except subprocess.CalledProcessError:
        return False


def capture_output(command: str,
                   ip: Optional[str] = None,
                   transport_id: Optional[str] = None,
                   **kwargs) -> Tuple[Optional[str], int]:
    """
    Execute an adb command on the given device and return the result
    :param command:         command to execute
    :param ip:       device address ip
    :param transport_id:    device transport id
    :param kwargs:
    :return:
    """
    ip = f"-s {ip} " if ip else f"-t {transport_id} " if transport_id else ""
    adb = get_adb_path()
    command1 = "{} {}{}".format(adb, ip, command).split()
    command_log = "{} {}{}".format(os.path.basename(adb), ip, command).split()
    try:
        log().spam("Executing `%s`" % " ".join(command_log))
        out = subprocess.Popen(
            command1,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            shell=kwargs.get("shell", False),
        )
        result = out.communicate()
        return result[0].decode("utf-8").strip(), out.returncode
    except subprocess.CalledProcessError as e:
        log().warning(e)
        return None, 1


def shell(command: str, ip: Optional[str] = None, transport_id: Optional[str] = None) -> Tuple[str, int]:
    """
    Execute a command in the adb shell
    :param command:         shell command to execute
    :param ip:              device ip
    :param transport_id:    device transport id
    :return: result, code
    """
    ip = f"-s {ip} " if ip else f"-t {transport_id} " if transport_id else ""
    adb = get_adb_path()
    base_command = f"{adb} {ip} shell {command}".split()
    command_log = f"{os.path.basename(adb)} {ip} shell {command}".split()
    log().spam(f"Executing `{' '.join(command_log)}`")

    out = subprocess.Popen(
        base_command,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        shell=False,
    )
    result = out.communicate()
    return result[0].decode("UTF-8").strip(), out.returncode


def wait_for_device(ip: Optional[str] = None, transport_id: Optional[str] = None) -> bool:
    """
    Execute and return the result of 'adb wait-for-device'
    :param ip:              device ip
    :param transport_id:    device transport id
    :return:                true if device connects
    """
    if is_connected(ip=ip, transport_id=transport_id):
        return True
    return execute("wait-for-device", ip=ip, transport_id=transport_id)


def root(ip: Optional[str] = None, transport_id: Optional[str] = None) -> bool:
    """
    Restart adb connection as root
    :param ip:              device ip
    :param transport_id:    device transport id
    :return:                true if root succeded
    """
    assert not is_root(ip)
    result = execute("root", ip=ip, transport_id=transport_id)

    time.sleep(1)
    if not is_connected(ip=ip, transport_id=transport_id):
        wait_for_device(ip=ip, transport_id=transport_id)
    return result


# noinspection SpellCheckingInspection
def unroot(ip: Optional[str] = None, transport_id: Optional[str] = None) -> bool:
    """
    Restart adb as unroot
    :param ip:              device ip
    :param transport_id:    device transport id
    :return:                True on success
    """
    assert is_root(ip)
    result = execute("unroot", ip=ip, transport_id=transport_id)
    time.sleep(1)
    if not is_connected(ip=ip, transport_id=transport_id):
        wait_for_device(ip)
    return result


def is_root(ip: Optional[str] = None, transport_id: Optional[str] = None) -> bool:
    """
    Test if adb connection is running as root
    :param ip:              device ip
    :param transport_id:    device transport id
    :return:                True if adb is running as root
    """
    result, code = shell("whoami", ip=ip, transport_id=transport_id)
    return result == "root"


def devices() -> List[Device]:
    """
    Return a list of attached devices
    :return:
    """
    result, code = capture_output("devices -l")
    if code == 0 and result:
        attached_devices = list(map(lambda x: x.split("\t")[0], result.split("\n")[1:]))
        result = list(filter(lambda y: y is not None, map(lambda x: Device.parse(x), attached_devices)))
        return result
    else:
        return []


def is_connected(ip: Optional[str] = None, transport_id: Optional[str] = None) -> bool:
    """
    Returns true if the given device is connected
    :param ip:  device ip
    :param transport_id:  device transport_id
    :return: true if connected
    """
    result, code = capture_output("get-state", ip=ip, transport_id=transport_id)
    log().spam(f"Result: `{result}` (code:{code})")
    return code == 0 and result == "device"


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


def reboot(ip: Optional[str] = None, transport_id: Optional[str] = None) -> bool:
    """
    Reboot the device
    :param ip:              device ip
    :param transport_id:    device transport id
    :return:                True on success
    """
    if execute("reboot", ip=ip, transport_id=transport_id):
        zope.event.notify(events.ADBEvent(events.ADBConnectionEvent.Reboot, ip))
        return True
    return False


def remount(ip: Optional[str] = None, transport_id: Optional[str] = None) -> bool:
    """
    Remount the file system
    :param ip:              device ip
    :param transport_id:    device transport id
    :return:                True on success
    """
    if not is_root(ip=ip, transport_id=transport_id):
        root(ip=ip, transport_id=transport_id)
    return execute("remount", ip=ip, transport_id=transport_id)


def remount_as(ip: Optional[str] = None,
               transport_id: Optional[str] = None,
               writeable: bool = False, folder: str = "/system") -> Tuple[str, int]:
    """
    Mount/Remount file-system
    :param folder:          folder to mount
    :param writeable:       mount as writeable or readable-only
    :param ip:              device ip
    :param transport_id:    device transport id
    :rtype:                 a tuple containing the result string and the result code (0 = success)
    """
    if writeable:
        return shell(f"mount -o rw,remount {folder}", ip=ip, transport_id=transport_id)
    else:
        return shell(f"mount -o ro,remount {folder}", ip=ip, transport_id=transport_id)
