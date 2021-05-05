#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import optional
from pathlib import Path
from typing import Dict, Union, Optional

from . import adb_connection
from . import constants
from .adb_connection import ADBCommandResult

__all__ = ["ADBClient"]


def log():
    from . import _logger

    logger = _logger.get_logger(__name__)
    return logger


class ADBClient(object):
    def __init__(self, identifier: Optional[str] = None):
        self._identifier = identifier
        self._busybox: Optional[optional.Optional[bool]] = None
        self._which: Optional[optional.Optional[bool]] = None

    @property
    def identifier(self):
        return self._identifier

    def has_busybox(self):
        if self._busybox is None:
            self._busybox = optional.Optional.of(self.exists(constants.BUSYBOX))
        return self._busybox.get()

    def hash_which(self):
        if self._which is None:
            self._which = optional.Optional.of(self.exists(constants.WHICH))
        return self._which.get()

    def wait_for_device(self) -> bool:
        if self.is_connected():
            return True
        return adb_connection.wait_for_device(ip=self._identifier)

    def connect(self):
        return adb_connection.connect(ip=self._identifier)

    def disconnect(self):
        return adb_connection.disconnect(ip=self._identifier)

    @staticmethod
    def disconnect_all():
        return adb_connection.disconnect_all()

    def is_connected(self):
        return adb_connection.is_connected(ip=self._identifier)

    def reconnect(self):
        return adb_connection.reconnect(ip=self._identifier)

    def reconnect_device(self):
        return adb_connection.reconnect_device(ip=self._identifier)

    def reconnect_offline(self):
        return adb_connection.reconnect_offline(ip=self._identifier)

    def is_root(self):
        return adb_connection.is_root(ip=self._identifier)

    def root(self):
        self._connect_if_disconnected()
        if not self.is_root():
            adb_connection.root(ip=self._identifier)
            self.reconnect_device()
            self.wait_for_device()
            return adb_connection.is_root(ip=self._identifier)
        return True

    def unroot(self):
        self._connect_if_disconnected()
        if self.is_root():
            adb_connection.unroot(ip=self._identifier)
            self.reconnect_device()
            self.wait_for_device()
            return not adb_connection.is_root(ip=self._identifier)
        return True

    def shell(self, command: str, **kwargs):
        self._connect_if_disconnected()
        return adb_connection.shell(command=command, ip=self._identifier, **kwargs)

    def capture_output(self, command: str, **kwargs):
        self._connect_if_disconnected()
        return adb_connection.capture_output(
            command=command, ip=self._identifier, **kwargs
        )

    def execute(self, command: str, **kwargs):
        self._connect_if_disconnected()
        return adb_connection.execute(command=command, ip=self._identifier, **kwargs)

    def remount_filesystem(self, writeable: bool):
        self._connect_if_disconnected()
        return adb_connection.remount_as(ip=self._identifier, writeable=writeable)

    def remount(self):
        self._connect_if_disconnected()
        return adb_connection.remount(ip=self._identifier)

    def reboot(self, mode: Optional[str] = None, wait_device: bool = False):
        self._connect_if_disconnected()
        if adb_connection.reboot(ip=self._identifier, mode=mode):
            if wait_device:
                return self.wait_for_device()
            return True
        return False

    def bugreport(self, dst: Optional[str] = None):
        adb_connection.bugreport(dst, self._identifier)

    def get_id(self) -> Optional[str]:
        """
        Return the value of ANDROID_ID
        See: https://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID

        :return:
        """
        code, output, _ = self.shell("settings get secure android_id")
        if code == ADBCommandResult.RESULT_OK:
            return output
        return None

    def getprop(
            self, key: Optional[str] = None
    ) -> Optional[Union[str, Dict[str, str]]]:
        if key:
            with self.shell(f"getprop {key}") as result:
                if result.is_ok():
                    return result.output()
                return None
        else:
            with self.shell("getprop") as result:
                if result.is_ok() and result.output():
                    return self._parse_properties(result.output())
                return None

    def setprop(self, key: str, value: str):
        return self.shell(f"setprop {key} {value}")

    def get_mac_address(self) -> Optional[str]:
        result = self.ifconfig()
        if result.code == ADBCommandResult.RESULT_OK:
            match = re.search("HWaddr[\\s]+([0-9:a-zA-Z]+)", result.output())
            if match and len(match.groups()) > 0:
                return match.groups()[0]
        return None

    def set_bluetooth_enabled(self, value: bool):
        log().verbose(f"Turning Bluetooth {'on' if value else 'off'}...")
        return self.shell(f"service call bluetooth_manager {6 if value else 8}")

    def get_global_settings(self) -> Optional[Dict[str, str]]:
        code, output, error = self.shell("settings list global")
        if code == ADBCommandResult.RESULT_OK and output:
            return dict(map(lambda x: x.split("=", 1), output.splitlines()))
        return None

    def get_system_settings(self) -> Optional[Dict[str, str]]:
        code, output, error = self.shell("settings list system")
        if code == ADBCommandResult.RESULT_OK and output:
            return dict(map(lambda x: x.split("=", 1), output.splitlines()))
        return None

    def get_global_settings_value(self, key: str):
        """Retrieve a value from the device global settings"""
        return self.shell(f"settings get global {key}")

    def get_system_settings_value(self, key: str):
        """Retrieve a value from the device system settings"""
        return self.shell(f"settings get system {key}")

    def set_global_settings_value(self, key: str, value: str):
        self.root()
        return self.shell(f"settings put global {key} {value}")

    def set_system_settings_value(self, key: str, value: str):
        self.root()
        return self.shell(f"settings put system {key} {value}")

    def dumpsys_bluetooth(self):
        return self.dumpsys("bluetooth_manager")

    def dumpsys(self, which: str, **kwargs):
        """
        For a list of arguments see: https://developer.android.com/studio/command-line/dumpsys
        :param which:   which system service to dump
        :param kwargs:  additional arguments
        :return:
        """
        return self.shell(
            command="dumpsys", **adb_connection.extends_extra_arguments(which, **kwargs)
        )

    def dumpsys_meminfo(self, package: str):
        return self.shell(f"dumpsys meminfo {package}")

    def ifconfig(self):
        return self.shell("ifconfig")

    def gc(self, pid: int) -> bool:
        """Force the GC for the given pid"""
        return self.shell(f"kill -10 {pid}").is_ok()

    def pid(self, packagename: str) -> int:
        """Retrieve the pid of the given package or -1 if not found"""
        result = self.shell(f"pidof -s {packagename}")
        if result.is_ok():
            return int(result.output())
        return -1

    """ -----------------------------------------------------------------------"""
    """ File system methods """
    """ -----------------------------------------------------------------------"""

    def is_file(self, path: str) -> bool:
        return self._test_file(path, "f")

    def is_dir(self, path: str) -> bool:
        return self._test_file(path, "d")

    def is_symlink(self, path: str) -> bool:
        return self._test_file(path, "h")

    def exists(self, path: str) -> bool:
        return self._test_file(path, "e")

    def remove(self, dst: str):
        return self.shell(f"rm -fr {dst}")

    def cat(self, filename: str, encoding: str = 'utf-8') -> str:
        code, output, error = self.shell(f"cat {filename}", encoding=encoding)
        if code != ADBCommandResult.RESULT_OK:
            raise IOError(f"File {filename} not found")
        return output

    def which(self, command: str) -> Optional[str]:
        self._connect_if_disconnected()
        if self.hash_which():
            return adb_connection.which(command=command, ip=self._identifier)
        elif self.has_busybox():
            result = self.busybox(f"which {command}")
            if result.is_ok():
                return result.output()
        else:
            return None

    def ls(self, dirname: str, **kwargs):
        args = adb_connection.expand_extra_arguments(**kwargs)
        args.append(dirname)
        return self.shell("ls", args=args)

    def busybox(self, command: str, **kwargs):
        return self.shell(f"busybox {command}", **kwargs)

    def push(self, src: Path, dst: str, **kwargs) -> bool:
        log().notice(f"--> Push `{src}` into `{dst}`...")
        self._connect_if_disconnected()
        return adb_connection.push(ip=self._identifier, src=str(src), dst=dst, **kwargs)

    def pull(self, src: str, dst: Path, **kwargs):
        log().notice(f"<-- Pull `{src}` into `{dst}`...")
        self._connect_if_disconnected()
        final_dst = dst
        if dst.is_dir():
            if not dst.exists():
                raise IOError(f"{dst} does not exist")
            final_dst = dst / os.path.basename(src)
        return adb_connection.pull(
            ip=self._identifier, src=src, dst=str(final_dst), **kwargs
        )

    """ -----------------------------------------------------------------------"""
    """ Key Events """
    """ -----------------------------------------------------------------------"""

    def getevent(self):
        result = self.shell("getevent -p")
        if result.is_ok():
            return re.findall(r"^add device [0-9]+: ([^\n]+)\n\s*name:\s*\"(.*)\"\n?", result.output(), re.MULTILINE)
        return None

    def getevent_named(self, name: str):
        events = self.getevent()
        if events and len(events) > 0:
            return next(map(lambda y: y[0], filter(lambda x: x[1] == name, events)), events[0])
        return '/dev/input/event0'

    def key_up(self, key: int, device: str = '/dev/input/event0'):
        return self.shell(
            f"""
        sendevent {device} 0004 0004 000c0042 &&
        sendevent {device} 0001 {key} 00000000 &&
        sendevent {device} 0000 0000 00000000
        """
        )

    def key_down(self, key: int, device: str = '/dev/input/event0'):
        return self.shell(
            f"""
        sendevent {device} 0004 0004 000c0042 &&
        sendevent {device} 0001 {key} 00000001 &&
        sendevent {device} 0000 0000 00000000
        """
        )

    def send_raw_key(self, key: int, device: str = '/dev/input/event0'):
        """
        Most values are from CplusPlusKeyCodes
        Seee https://supportcommunity.zebra.com/s/article/Find-out-key-event-via-ADB?language=en_US
        or
        http://androidxref.com/4.4_r1/xref/prebuilts/ndk/6/platforms/android-9/arch-arm/usr/include/linux/input.h
        for help about key codes
        """
        return self.shell(
            f"""
        sendevent {device} 0004 0004 000c0042 &&
        sendevent {device} 0001 {key} 00000001 &&
        sendevent {device} 0000 0000 00000000 &&
        sendevent {device} 0004 0004 000c0042 &&
        sendevent {device} 0001 {key} 00000000 &&
        sendevent {device} 0000 0000 00000000"""
        )

    def send_key(self, key: int) -> ADBCommandResult:
        assert type(key) is int
        log().verbose(f"Sending key: {key}")
        return self.shell(f"input keyevent {key}")

    def send_text(self, char: str) -> ADBCommandResult:
        assert type(char) is str
        log().verbose(f"Sending {char}...")
        return self.shell(f"input text {char}")

    """ ----------------------------------------------------------------------- """
    """ Private Methods """
    """ ----------------------------------------------------------------------- """

    def _test_file(self, path: str, mode: str) -> bool:
        result = self.shell("test -{} {} && echo 1 || echo 0".format(mode, path))
        log().spam(f"code: {result.code}, output:{result.output()}")
        if result.code == ADBCommandResult.RESULT_OK:
            return result.output().strip() == "1"
        return False

    def _connect_if_disconnected(self):
        if not self.is_connected():
            self.connect()

    def _parse_properties(self, string: str) -> Dict[str, str]:
        result = dict()
        lines = list(map(lambda x: x.split(":", 1), string.splitlines()))
        for line in lines:
            item = list(map(lambda y: y.strip()[1:-1], line))
            result[item[0]] = item[1]
        return result
