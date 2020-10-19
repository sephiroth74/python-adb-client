#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from typing import Optional, Dict

from . import adb_connection
from .adb_connection import ADBCommandResult


def log():
    from . import _logger
    logger = _logger.get_logger(__name__)
    return logger


class ADBClient(object):
    def __init__(self, identifier: Optional[str] = None):
        self._identifier = identifier

    @property
    def identifier(self):
        return self._identifier

    def wait_for_device(self) -> bool:
        return adb_connection.wait_for_device(ip=self._identifier)

    def connect(self):
        return adb_connection.connect(ip=self._identifier)

    def disconnect(self):
        return adb_connection.disconnect(ip=self._identifier)

    def is_connected(self):
        return adb_connection.is_connected(ip=self._identifier)

    def is_root(self):
        return adb_connection.is_root(ip=self._identifier)

    def root(self):
        self._connect_if_disconnected()
        if not self.is_root():
            return adb_connection.root(ip=self._identifier)
        return True

    def unroot(self):
        self._connect_if_disconnected()
        if self.is_root():
            return adb_connection.unroot(ip=self._identifier)
        return True

    def shell(self, command: str, **kwargs):
        self._connect_if_disconnected()
        return adb_connection.shell(command=command, ip=self._identifier, **kwargs)

    def capture_output(self, command: str, **kwargs):
        self._connect_if_disconnected()
        return adb_connection.capture_output(command=command, ip=self._identifier, **kwargs)

    def execute(self, command: str, **kwargs):
        self._connect_if_disconnected()
        return adb_connection.execute(command=command, ip=self._identifier, **kwargs)

    def remount_filesystem(self, writeable: bool):
        self._connect_if_disconnected()
        return adb_connection.remount_as(ip=self._identifier, writeable=writeable)

    def remount(self):
        self._connect_if_disconnected()
        return adb_connection.reboot(ip=self._identifier)

    def reboot(self, wait_device: bool = False):
        self._connect_if_disconnected()
        if adb_connection.reboot(ip=self._identifier):
            if wait_device:
                return self.wait_for_device()
            return True
        return False

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

    def get_global_settings_value(self, key: str):
        """Retrieve a value from the device global settings"""
        return self.shell(f"settings get global {key}")

    def set_global_settings_value(self, key: str, value: str):
        self.root()
        return self.shell(f"settings put global {key} {value}")

    def dumpsys_bluetooth(self):
        return self.shell("dumpsys bluetooth_manager")

    def dumpsys_meminfo(self, package: str):
        if not self.is_installed(package):
            return ADBCommandResult.from_error(ADBCommandResult.RESULT_ERROR)
        return self.shell(f"dumpsys meminfo {package}")

    def get_package_info(self, package_name: str):
        if not self.is_installed(package_name):
            return ADBCommandResult.from_error(ADBCommandResult.RESULT_ERROR)
        return self.shell(f"pm dump {package_name}")

    def ifconfig(self):
        return self.shell("ifconfig")

    def dump_package(self, package: str):
        if not self.is_installed(package):
            return ADBCommandResult.from_error(ADBCommandResult.RESULT_ERROR)
        return self.shell(f"pm dump {package}")

    def packages(self, package: Optional[str] = None):
        code, result, _ = self.list_packages(package)
        if code == ADBCommandResult.RESULT_OK and result:
            return list(map(lambda x: x.replace("package:", "").strip(), result.splitlines()))
        return []

    def is_installed(self, package: str) -> bool:
        return package in self.packages(package)

    def list_packages(self, package: Optional[str] = None, **kwargs):
        """
        list packages [-f] [-d] [-e] [-s] [-3] [-i] [-l] [-u] [-U] [--uid UID] [--user USER_ID] [FILTER]
        Prints all packages; optionally only those whose name contains
        the text in FILTER.
        Options:
        -f: see their associated file
        -d: filter to only show disabled packages
        -e: filter to only show enabled packages
        -s: filter to only show system packages
        -3: filter to only show third party packages
        -i: see the installer for the packages
        -l: ignored (used for compatibility with older releases)
        -U: also show the package UID
        -u: also include uninstalled packages
        --uid UID: filter to only show packages with the given UID
        --user USER_ID: only list packages belonging to the given user

        :param package: optional package to look for
        :param kwargs:
        :return:
        """
        return self.shell(f"cmd package list packages {package if package else ''}", **kwargs)

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

    def cat(self, filename: str) -> str:
        code, output, error = self.shell(f"cat {filename}")
        if code != ADBCommandResult.RESULT_OK:
            raise IOError(f"File {filename} not found")
        return output

    """ -----------------------------------------------------------------------"""
    """ Key Events """
    """ -----------------------------------------------------------------------"""

    def key_up(self, key: int):
        return self.shell(
            f"""
        sendevent /dev/input/event3 0004 0004 000c0042 &&
        sendevent /dev/input/event3 0001 {key} 00000000 &&
        sendevent /dev/input/event3 0000 0000 00000000
        """
        )

    def key_down(self, key: int):
        return self.shell(
            f"""
        sendevent /dev/input/event3 0004 0004 000c0042 &&
        sendevent /dev/input/event3 0001 {key} 00000001 &&
        sendevent /dev/input/event3 0000 0000 00000000
        """
        )

    def send_raw_key(self, key: int):
        """
        Most values are from CplusPlusKeyCodes
        Seee https://supportcommunity.zebra.com/s/article/Find-out-key-event-via-ADB?language=en_US
        or
        http://androidxref.com/4.4_r1/xref/prebuilts/ndk/6/platforms/android-9/arch-arm/usr/include/linux/input.h
        for help about key codes
        """
        return self.shell(
            f"""
        sendevent /dev/input/event3 0004 0004 000c0042 &&
        sendevent /dev/input/event3 0001 {key} 00000001 &&
        sendevent /dev/input/event3 0000 0000 00000000 &&
        sendevent /dev/input/event3 0004 0004 000c0042 &&
        sendevent /dev/input/event3 0001 {key} 00000000 &&
        sendevent /dev/input/event3 0000 0000 00000000        
        """
        )

    def send_key(self, key: int):
        assert type(key) is int
        log().verbose(f"Sending key: {key}")
        return self.shell(f"input keyevent {key}")

    def send_text(self, char: str):
        assert type(char) is str
        log().verbose(f"Sending {char}...")
        return self.shell(f"input text {char}")

    """ ----------------------------------------------------------------------- """
    """ Private Methods """
    """ ----------------------------------------------------------------------- """

    def _test_file(self, path: str, mode: str) -> bool:
        result = self.shell("test -{} {} && echo 1 || echo 0".format(mode, path))
        if result.code == ADBCommandResult.RESULT_OK:
            return result.output().strip() == "1"
        return False

    def _connect_if_disconnected(self):
        if not self.is_connected():
            self.connect()
