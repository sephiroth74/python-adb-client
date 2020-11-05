#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Android Debug Bridge version 1.0.41
Version 30.0.4-6686687
Installed as /Users/alessandro/Library/Android/sdk/platform-tools/adb

global options:
 -a         listen on all network interfaces, not just localhost
 -d         use USB device (error if multiple devices connected)
 -e         use TCP/IP device (error if multiple TCP/IP devices available)
 -s SERIAL  use device with given serial (overrides $ANDROID_SERIAL)
 -t ID      use device with given transport id
 -H         name of adb server host [default=localhost]
 -P         port of adb server [default=5037]
 -L SOCKET  listen on given socket for adb server [default=tcp:localhost:5037]

general commands:
 devices [-l]             list connected devices (-l for long output)
 help                     show this help message
 version                  show version num

networking:
 connect HOST[:PORT]      connect to a device via TCP/IP [default port=5555]
 disconnect [HOST[:PORT]]
     disconnect from given TCP/IP device [default port=5555], or all
 pair HOST[:PORT] [PAIRING CODE]
     pair with a device for secure TCP/IP communication
 forward --list           list all forward socket connections
 forward [--no-rebind] LOCAL REMOTE
     forward socket connection using:
       tcp:<port> (<local> may be "tcp:0" to pick any open port)
       localabstract:<unix domain socket name>
       localreserved:<unix domain socket name>
       localfilesystem:<unix domain socket name>
       dev:<character device name>
       jdwp:<process pid> (remote only)
       acceptfd:<fd> (listen only)
 forward --remove LOCAL   remove specific forward socket connection
 forward --remove-all     remove all forward socket connections
 ppp TTY [PARAMETER...]   run PPP over USB
 reverse --list           list all reverse socket connections from device
 reverse [--no-rebind] REMOTE LOCAL
     reverse socket connection using:
       tcp:<port> (<remote> may be "tcp:0" to pick any open port)
       localabstract:<unix domain socket name>
       localreserved:<unix domain socket name>
       localfilesystem:<unix domain socket name>
 reverse --remove REMOTE  remove specific reverse socket connection
 reverse --remove-all     remove all reverse socket connections from device
 mdns check               check if mdns discovery is available
 mdns services            list all discovered services

file transfer:
 push [--sync] [-z ALGORITHM] [-Z] LOCAL... REMOTE
     copy local files/directories to device
     --sync: only push files that are newer on the host than the device
     -n: dry run: push files to device without storing to the filesystem
     -z: enable compression with a specified algorithm (any, none, brotli)
     -Z: disable compression
 pull [-a] [-z ALGORITHM] [-Z] REMOTE... LOCAL
     copy files/dirs from device
     -a: preserve file timestamp and mode
     -z: enable compression with a specified algorithm (any, none, brotli)
     -Z: disable compression
 sync [-l] [-z ALGORITHM] [-Z] [all|data|odm|oem|product|system|system_ext|vendor]
     sync a local build from $ANDROID_PRODUCT_OUT to the device (default all)
     -n: dry run: push files to device without storing to the filesystem
     -l: list files that would be copied, but don't copy them
     -z: enable compression with a specified algorithm (any, none, brotli)
     -Z: disable compression

shell:
 shell [-e ESCAPE] [-n] [-Tt] [-x] [COMMAND...]
     run remote shell command (interactive shell if no command given)
     -e: choose escape character, or "none"; default '~'
     -n: don't read from stdin
     -T: disable pty allocation
     -t: allocate a pty if on a tty (-tt: force pty allocation)
     -x: disable remote exit codes and stdout/stderr separation
 emu COMMAND              run emulator console command

app installation (see also `adb shell cmd package help`):
 install [-lrtsdg] [--instant] PACKAGE
     push a single package to the device and install it
 install-multiple [-lrtsdpg] [--instant] PACKAGE...
     push multiple APKs to the device for a single package and install them
 install-multi-package [-lrtsdpg] [--instant] PACKAGE...
     push one or more packages to the device and install them atomically
     -r: replace existing application
     -t: allow test packages
     -d: allow version code downgrade (debuggable packages only)
     -p: partial application install (install-multiple only)
     -g: grant all runtime permissions
     --abi ABI: override platform's default ABI
     --instant: cause the app to be installed as an ephemeral install app
     --no-streaming: always push APK to device and invoke Package Manager as separate steps
     --streaming: force streaming APK directly into Package Manager
     --fastdeploy: use fast deploy
     --no-fastdeploy: prevent use of fast deploy
     --force-agent: force update of deployment agent when using fast deploy
     --date-check-agent: update deployment agent when local version is newer and using fast deploy
     --version-check-agent: update deployment agent when local version has different version code and using fast deploy
     --local-agent: locate agent files from local source build (instead of SDK location)
     (See also `adb shell pm help` for more options.)
 uninstall [-k] PACKAGE
     remove this app package from the device
     '-k': keep the data and cache directories

debugging:
 bugreport [PATH]
     write bugreport to given PATH [default=bugreport.zip];
     if PATH is a directory, the bug report is saved in that directory.
     devices that don't support zipped bug reports output to stdout.
 jdwp                     list pids of processes hosting a JDWP transport
 logcat                   show device log (logcat --help for more)

security:
 disable-verity           disable dm-verity checking on userdebug builds
 enable-verity            re-enable dm-verity checking on userdebug builds
 keygen FILE
     generate adb public/private key; private key stored in FILE,

scripting:
 wait-for[-TRANSPORT]-STATE...
     wait for device to be in a given state
     STATE: device, recovery, rescue, sideload, bootloader, or disconnect
     TRANSPORT: usb, local, or any [default=any]
 get-state                print offline | bootloader | device
 get-serialno             print <serial-number>
 get-devpath              print <device-path>
 remount [-R]
      remount partitions read-write. if a reboot is required, -R will
      will automatically reboot the device.
 reboot [bootloader|recovery|sideload|sideload-auto-reboot]
     reboot the device; defaults to booting system image but
     supports bootloader and recovery too. sideload reboots
     into recovery and automatically starts sideload mode,
     sideload-auto-reboot is the same but reboots after sideloading.
 sideload OTAPACKAGE      sideload the given full OTA package
 root                     restart adbd with root permissions
 unroot                   restart adbd without root permissions
 usb                      restart adbd listening on USB
 tcpip PORT               restart adbd listening on TCP on PORT

internal debugging:
 start-server             ensure that there is a server running
 kill-server              kill the server if it is running
 reconnect                kick connection from host side to force reconnect
 reconnect device         kick connection from device side to force reconnect
 reconnect offline        reset offline/unauthorized devices to force reconnect

environment variables:
 $ADB_TRACE
     comma-separated list of debug info to log:
     all,adb,sockets,packets,rwx,usb,sync,sysdeps,transport,jdwp
 $ADB_VENDOR_KEYS         colon-separated list of keys (files or directories)
 $ANDROID_SERIAL          serial number to connect to (see -s)
 $ANDROID_LOG_TAGS        tags to be used by logcat (see logcat --help)
 $ADB_LOCAL_TRANSPORT_MAX_PORT max emulator scan port (default 5585, 16 emus)
 $ADB_MDNS_AUTO_CONNECT   comma-separated list of mdns services to allow auto-connect (default adb-tls-connect)

"""

from __future__ import annotations

import re
import shutil
import subprocess
import time
from typing import List, Optional, Dict, Tuple, Any

# noinspection PyPackageRequirements
import zope.event

from .. import events
from .. import constants

__all__ = [
    "ADBCommandResult",
    "Device",
    "bugreport",
    "busybox",
    "capture_output",
    "connect",
    "devices",
    "disconnect",
    "disconnect_all",
    "execute",
    "get_adb_path",
    "is_connected",
    "is_root",
    "mdns_check",
    "mdns_services",
    "pull",
    "push",
    "reboot",
    "reconnect",
    "reconnect_device",
    "reconnect_offline",
    "remount",
    "remount_as",
    "root",
    "set_adb_path",
    "shell",
    "unroot",
    "version",
    "wait_for_device",
    "which",
    "extends_extra_arguments",
    "expand_extra_arguments",
]

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
        return self._attrs["transport_id"] if "transport_id" in self._attrs else None

    def is_usb(self) -> bool:
        """
        Return true if the attached device is connected through USB
        :return:
        """
        return "usb" in self._attrs

    def is_emulator(self) -> bool:
        """
        Return true if the attached device is an emulator
        :return:
        """
        return self._identifier.startswith("emulator-")

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
        "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):[0-9]+$"
    )

    @staticmethod
    def parse(string: str) -> Optional[Device]:
        match1 = re.match(Device.PATTERN_LINE, string)
        if match1:
            device_id = match1.group(1)
            attrbutes = match1.group(2)
            device_attr = dict(
                map(lambda x: x.split(":"), re.findall(Device.PATTERN_ATTR, attrbutes))
            )
            return Device(device_id, device_attr)
        else:
            log().warning(f"Failed to parse device string {string}")
            return None


class ADBCommandResult(object):
    RESULT_OK = 0
    RESULT_ERROR = 1

    def __init__(
            self,
            result: Tuple[Optional[bytes], Optional[bytes]] = (None, None),
            code: int = RESULT_OK,
    ):
        super(ADBCommandResult, self).__init__()
        self._stdout = result[0] if result[0] else None
        self._stderr = (
            result[1].decode("utf-8").strip() if result[1] is not None else None
        )
        self._code = code

    def __iter__(self):
        return (self._code, self.output(), self.error()).__iter__()

    def __str__(self):
        return f"Result(code={self._code}, output={self._stdout}, error={self._stderr})"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @property
    def code(self):
        """
        Error Code returned. if '0' it means no error
        :return:
        """
        return self._code

    def output(self, raw: bool = False):
        if self._stdout and not raw:
            return self._stdout.decode("utf-8").strip()
        return self._stdout

    def error(self):
        return self._stderr

    def is_ok(self):
        return self.code == ADBCommandResult.RESULT_OK

    def is_error(self):
        return not self.is_ok()

    @staticmethod
    def from_error(code: int = RESULT_ERROR):
        return ADBCommandResult(result=(None, None), code=code)


def log():
    from .. import _logger

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


def busybox(command: str, ip: Optional[str] = None, **kwargs):
    """
    Executes a shell command using 'busybox'. If busybox in not installed on the device it will fail.\n
    See https://busybox.net/
    :param command:
    :param ip:
    :param kwargs:
    :return:
    """
    return shell(f"{constants.BUSYBOX} {command}", ip, **kwargs)


def which(command: str, ip: Optional[str] = None) -> Optional[str]:
    """
    Execute 'which' command on the specified device and return the result
    :param command:     command to test with 'which'
    :param ip:          device ip
    :return:            the command path on the device, if found
    """
    which_cmd = f"{constants.WHICH}"
    result = shell(f"{which_cmd} {command}", ip=ip)
    if result.code == ADBCommandResult.RESULT_OK and result.output() and len(result.output()) > 0:
        return result.output()
    return None


def execute(command: str, ip: Optional[str] = None, **kwargs) -> bool:
    """
    Execute an adb command on the given device, if connected
    :param command: command to execute
    :param ip:      device identifier
    :param kwargs:
    :return:
    """
    ip_arg = f"-s {ip} " if ip else ""
    adb = get_adb_path()
    command_line = f"{ip_arg}{command} {get_extra_arguments(**kwargs)}"
    command_full = f"{adb} {command_line}".strip()
    command_log = f"adb {command_line}".strip()
    output = subprocess.PIPE if "stdout" not in kwargs else kwargs["stdout"]

    try:
        log().debug(f"Executing `{command_log}`")
        out = subprocess.Popen(
            command_full.split(), stderr=subprocess.STDOUT, stdout=output
        )
        result = out.communicate()
        if not command == "get-state":
            result_str = result[0].decode("utf-8").strip() if result[0] else "None"
            log().spam(f"Result(code={out.returncode}, result={result_str})")
        return out.returncode == ADBCommandResult.RESULT_OK
    except subprocess.CalledProcessError:
        return False


def capture_output(
        command: str, ip: Optional[str] = None, **kwargs
) -> ADBCommandResult:
    """
    Execute an adb command on the given device and return the result
    :param command:  command to execute
    :param ip:       device id
    :param kwargs:   if contains the 'args' key, its value is passed as arguments to the input command
    :return:
    """
    ip_arg = f"-s {ip} " if ip else ""
    adb = get_adb_path()
    command_line = f"{ip_arg}{command} {get_extra_arguments(**kwargs)}"
    command_full = f"{adb} {command_line}".strip()
    command_log = f"adb {command_line}".strip()
    try:
        if kwargs.get("log", True):
            log().debug(f"Executing `{command_log}`")
        out = subprocess.Popen(
            command_full.split(),
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=False,
        )
        result = out.communicate()
        return ADBCommandResult(result, out.returncode)
    except subprocess.CalledProcessError as e:
        log().warning(e)
        return ADBCommandResult(code=ADBCommandResult.RESULT_ERROR)


def shell(command: str, ip: Optional[str] = None, **kwargs) -> ADBCommandResult:
    """
    Execute a command in the adb shell
    :param command:         shell command to execute
    :param ip:              device ip
    :param kwargs:          if contains the 'args' key, its value is passed as arguments to the input command
    :return:
    """
    ip_arg = f"-s {ip} " if ip else ""
    adb = get_adb_path()
    command_line = f"{ip_arg} shell"
    command_args = f"{command} {get_extra_arguments(**kwargs)}"
    command_full = f"{adb} {command_line} {command_args}".strip()
    command_log = f"adb {command_line} {command_args}".strip()
    log().debug(f"Executing `{command_log}`")

    out = subprocess.Popen(
        command_full.split(),
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=False,
    )

    result = out.communicate()
    code = out.returncode
    return ADBCommandResult(result, code)


def wait_for_device(ip: Optional[str] = None) -> bool:
    """
    Execute and return the result of 'adb wait-for-device'
    :param ip:              device ip
    :return:                true if device connects
    """
    # if is_connected(ip=ip):
    #     return True

    execute(
        "wait-for-device shell 'while [[ -z $(getprop sys.boot_completed) ]]; do sleep 1; done; input keyevent 143'",
        ip=ip,
    )

    return is_connected(ip=ip)


def reconnect(ip: Optional[str] = None) -> bool:
    """
    kick connection from host side to force reconnect

    :param ip:  device id
    :return:    true on success
    """
    return execute("reconnect", ip=ip)


def reconnect_device(ip: Optional[str] = None) -> bool:
    """
    kick connection from device side to force reconnect
    :param ip:  device id
    :return:    true on success
    """
    return execute("reconnect device", ip=ip)


def reconnect_offline(ip: Optional[str] = None) -> bool:
    """
    reset offline/unauthorized devices to force reconnect

    :param ip:  device id
    :return:    true on success
    """
    return execute("reconnect offline", ip=ip)


def root(ip: Optional[str] = None) -> bool:
    """
    Restart adb connection as root
    :param ip:              device ip
    :return:                true if root succeded
    """
    # if is_root(ip=ip):
    #     return True
    # execute("root", ip=ip)
    # execute("reconnect", ip=ip)
    # wait_for_device(ip=ip)
    # return is_root(ip=ip)
    return execute("root", ip=ip)


# noinspection SpellCheckingInspection
def unroot(ip: Optional[str] = None) -> bool:
    """
    Restart adb as unroot
    :param ip:              device ip
    :return:                True on success
    """
    # if not is_root(ip=ip):
    #     return True
    #
    # execute("unroot", ip=ip)
    # reconnect(ip=ip)
    # wait_for_device(ip=ip)
    # return not is_root(ip=ip)
    return execute("unroot", ip=ip)


def is_root(ip: Optional[str] = None) -> bool:
    """
    Test if adb connection is running as root
    :param ip:              device ip
    :return:                True if adb is running as root
    """
    result = shell("whoami", ip=ip)
    if result.code == ADBCommandResult.RESULT_OK:
        log().spam(f"whoami: {result.output()}")
        return result.output() == "root"
    return False


def devices(**kwargs) -> List[str]:
    """
    Return a list of attached devices
    :param kwargs: extra arguments
    :return:
    """
    result = capture_output(command="devices", **kwargs)
    if result.code == ADBCommandResult.RESULT_OK:
        return list(map(lambda x: x.split("\t")[0], result.output().split("\n")[1:]))
    else:
        return []
    # if result.code == ADBCommandResult.RESULT_OK and result.result:
    #     attached_devices = list(map(lambda x: x.split("\t")[0], result.result.split("\n")[1:]))
    #     result = list(filter(lambda y: y is not None, map(lambda x: Device.parse(x), attached_devices)))
    #     return result
    # else:
    #     return []


def is_connected(ip: Optional[str] = None) -> bool:
    """
    Returns true if the given device is connected
    :param ip:  device ip
    :return: true if connected
    """
    result = capture_output(command="get-state", ip=ip, log=False)
    # log().spam(result)
    return result.code == ADBCommandResult.RESULT_OK and result.output() == "device"


def connect(ip: Optional[str]) -> bool:
    """
    Attempts to connect to the device with the given ip address
    :param ip: device ip
    :return: true if connection succeed
    """
    log().debug(f"Connecting to {ip}..")

    if is_connected(ip=ip):
        log().info("Already connected...")
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


def disconnect(ip: Optional[str]) -> bool:
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


def reboot(ip: Optional[str] = None, mode: Optional[str] = None) -> bool:
    """
    Reboot the device
    :param ip:              device ip
    :param mode:            reboot type
    :return:                True on success
    """
    command = "reboot {}".format(mode if mode else "")
    if execute(command, ip=ip):
        zope.event.notify(events.ADBEvent(events.ADBConnectionEvent.Reboot, ip))
        return True
    return False


def remount(ip: Optional[str] = None) -> bool:
    """
    Remount the file system if root is permitted. Requires root
    :param ip:              device ip
    :return:                True on success
    """
    return execute("remount", ip=ip)


def remount_as(
        ip: Optional[str] = None, writeable: bool = False, folder: str = "/system"
) -> bool:
    """
    Mount/Remount file-system. Requires root
    :param folder:          folder to mount
    :param writeable:       mount as writeable or readable-only
    :param ip:              device ip
    :rtype:                 true on success
    """
    if writeable:
        return (
                shell(f"mount -o rw,remount {folder}", ip=ip).code
                == ADBCommandResult.RESULT_OK
        )
    else:
        return (
                shell(f"mount -o ro,remount {folder}", ip=ip).code
                == ADBCommandResult.RESULT_OK
        )


def version() -> Optional[str]:
    """
    Fetch and return the current adb version
    :return: the output as returned by 'adb version'
    """
    result = capture_output(command="version")
    if result.code == ADBCommandResult.RESULT_OK:
        return result.output()
    return None


def mdns_services() -> ADBCommandResult:
    """
    Return the result of the command 'adb mdns services'
    :return:
    """
    return capture_output(command="mdns services")


def mdns_check() -> ADBCommandResult:
    """
    Return the result of the command 'adb mdns check'
    :return:
    """
    return capture_output(command="mdns check")


def bugreport(dest: Optional[str] = None, ip: Optional[str] = None) -> bool:
    """
    Execute and return the result of the command 'adb bugreport'
    :param dest:    optional target local folder/filename for the bugreport
    :param ip:      optional device ip
    :return:        true on success
    """
    return execute("bugreport", ip=ip, args=(dest if dest else "",))


def push(ip: Optional[str], src: str, dst: str, **kwargs) -> bool:
    return execute(command="push", ip=ip, **extends_extra_arguments(src, dst, **kwargs))


def pull(ip: Optional[str], src: str, dst: str, **kwargs):
    return execute(command="pull", ip=ip, **extends_extra_arguments(src, dst, **kwargs))


""" Utilities """


def get_extra_arguments(**kwargs) -> str:
    _check_extra_arguments_type(**kwargs)
    if "args" in kwargs:
        return " ".join(filter(lambda x: x is not None, kwargs["args"]))
    return ""


def expand_extra_arguments(**kwargs) -> List[str]:
    _check_extra_arguments_type(**kwargs)
    if "args" in kwargs:
        return list(filter(lambda x: x is not None, kwargs["args"]))
    return []


def extends_extra_arguments(*args, **kwargs) -> Dict[Any, Any]:
    _check_extra_arguments_type(**kwargs)
    newlist = expand_extra_arguments(**kwargs)
    newlist.extend(args)
    kwargs["args"] = newlist
    return kwargs


def _check_extra_arguments_type(**kwargs):
    if "args" in kwargs:
        if not isinstance(kwargs["args"], (tuple, list)):
            raise RuntimeError(
                f'`args` must be either a tuple or a list, got {type(kwargs["args"])} instead'
            )
