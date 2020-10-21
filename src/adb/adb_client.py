#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path
from typing import Optional, Dict

from . import adb_connection
from .adb_connection import ADBCommandResult

__all__ = ['ADBClient', 'Package']


def log():
    from . import _logger
    logger = _logger.get_logger(__name__)
    return logger


# noinspection RegExpRedundantEscape
package_pattern = re.compile(
    r"package:(?P<apk>.*\.apk)?=?(?P<package>[a-zA-Z0-9\.]+)\s*(installer=(?P<installer>[\w\.]+))?\s*(uid:(?P<uuid>[\w]+))?")


class Package(object):
    # noinspection PyShadowingBuiltins
    def __init__(self, input: Dict[str, str]):
        self._name = input['package']
        self._apk = input.get('apk', None)
        self._installer = input.get('installer', None)
        self._uuid = input.get('uuid', None)

    @property
    def name(self): return self._name

    @property
    def apk(self): return self._apk

    @property
    def installer(self): return self._installer

    @property
    def uuid(self): return self._uuid

    def is_system(self): return self._apk.startswith("/system/") if self._apk else False

    def __repr__(self):
        return f'Package<id: {id(self)}, name: {self.name}>'

    def __str__(self):
        return f'Package({self.name})'

    def __eq__(self, other):
        if isinstance(other, (Package,)):
            return self.name == other.name
        return False


def _parse_dump_permissions(headline: str, input_str: str) -> Dict[str, bool]:
    found = False
    leading_spaces = 0
    permissions = dict()
    for line in input_str.splitlines():
        if line.strip() == headline:
            leading_spaces = len(line) - len(line.lstrip())
            found = True
            continue

        if found:
            if len(line) - len(line.lstrip()) == leading_spaces:
                found = False
                continue

            line = line.strip()
            if len(line) == 0:
                found = False
                continue

            splitted_line = line.split(":")
            if len(splitted_line) == 2:
                name = splitted_line[0]
                granted = splitted_line[1].split("=")[1].strip()
                permissions[name] = granted == "true"
            else:
                permissions[splitted_line[0]] = False
    return permissions


class ADBClient(object):
    def __init__(self, identifier: Optional[str] = None):
        self._identifier = identifier

    @property
    def identifier(self):
        return self._identifier

    def has_busybox(self):
        return self.which("busybox") is not None

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

    def get_properties(self) -> Dict[str, str]:
        code, output, error = self.shell("getprop")
        result = dict()
        if code == ADBCommandResult.RESULT_OK and output:
            lines = list(map(lambda x: x.split(':', 1), output.splitlines()))
            for line in lines:
                item = list(map(lambda y: y.strip()[1:-1], line))
                result[item[0]] = item[1]
        return result

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
        return self.dumpsys("bluetooth_manager")

    def dumpsys(self, which: str, **kwargs):
        """
        For a list of arguments see: https://developer.android.com/studio/command-line/dumpsys
        :param which:   which system service to dump
        :param kwargs:  additional arguments
        :return:
        """
        return self.shell(command=f"dumpsys",
                          **adb_connection.extends_extra_arguments(which, **kwargs))

    def dumpsys_meminfo(self, package: str):
        if not self.is_package_installed(package):
            return ADBCommandResult.from_error(ADBCommandResult.RESULT_ERROR)
        return self.shell(f"dumpsys meminfo {package}")

    def ifconfig(self):
        return self.shell("ifconfig")

    def dump_package(self, package: str):
        if not self.is_package_installed(package):
            return ADBCommandResult.from_error(ADBCommandResult.RESULT_ERROR)
        return self.shell(f"pm dump {package}")

    def is_package_installed(self, package: str) -> bool:
        return Package({'package': package}) in self.list_packages(package)

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
        result = self.shell(f"cmd package list packages",
                            **adb_connection.extends_extra_arguments(f"{package if package else ''}", **kwargs))
        packages = list()
        if result.is_ok() and result.output():
            for line in result.output().splitlines():
                match = re.match(package_pattern, line)
                if match:
                    packages.append(Package(match.groupdict()))

        return packages

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

    def cat(self, filename: str) -> str:
        code, output, error = self.shell(f"cat {filename}")
        if code != ADBCommandResult.RESULT_OK:
            raise IOError(f"File {filename} not found")
        return output

    def which(self, command: str) -> Optional[str]:
        self._connect_if_disconnected()
        return adb_connection.which(command=command, ip=self._identifier)

    def ls(self, dirname: str, **kwargs):
        args = adb_connection.expand_extra_arguments(**kwargs)
        args.append(dirname)
        return self.shell(f"ls", args=args)

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
        return adb_connection.pull(ip=self._identifier, src=src, dst=str(final_dst), **kwargs)

    def get_package(self, package: str) -> Optional[Package]:
        # noinspection RegExpRedundantEscape
        result = self.list_packages(package, args=("-f", "-U", "-i"))
        for line in result:
            if line.name == package:
                return line
        return None

    def install_package(self, apk: Path, **kwargs):
        """

        :param apk:
        :param kwargs:
        :return:
        """
        log().info(f"Installing {apk}...")
        return self.capture_output(command="install",
                                   **adb_connection.extends_extra_arguments(str(apk), **kwargs))

    def install_multi_package(self, *apks, **kwargs):
        """
        Not available on all adb clients

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
        :param apks:
        :param kwargs:
        :return:
        """
        return self.capture_output(command="install-multi-package",
                                   **adb_connection.extends_extra_arguments(*list(map(lambda x: str(x), apks)), **kwargs))

    def uninstall_package(self, package: str, **kwargs):
        """
        uninstall [-k] PACKAGE
            remove this app package from the device
            '-k': keep the data and cache directories
        """
        log().info(f"Uninstalling {package}...")
        return self.shell("pm uninstall",
                          **adb_connection.extends_extra_arguments(str(package), **kwargs))

    def clear_package(self, package: str, **kwargs):
        log().info(f"Clearing {package}")

        return self.shell("pm clear",
                          **adb_connection.extends_extra_arguments(str(package), **kwargs))

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

    """ -----------------------------------------------------------------------"""
    """ Permissions """
    """ -----------------------------------------------------------------------"""

    def grant_runtime_permission(self, package: str, permission: str):
        log().verbose(f"Granting '{permission}' to '{package}'...")
        return self.shell(f"pm grant {package} {permission}")

    def revoke_runtime_permission(self, package: str, permission: str):
        log().verbose(f"Revoking '{permission}' from '{package}'...")
        return self.shell(f"pm revoke {package} {permission}")

    def get_runtime_permissions(self, package: str):
        """
        Returns the package runtime permissions
        :param package:
        :return:
        """
        log().verbose(f"Fetching runtime permissions for `{package}`...")
        code, output, error = self.dump_package(package)
        if code == ADBCommandResult.RESULT_OK and output:
            return _parse_dump_permissions("runtime permissions:", output)
        return dict()

    def get_requested_permissions(self, package: str):
        """
        Returns the package runtime permissions
        :param package:
        :return:
        """
        log().verbose(f"Fetching requested permissions for `{package}`...")
        code, output, error = self.dump_package(package)
        if code == ADBCommandResult.RESULT_OK and output:
            return list(_parse_dump_permissions("requested permissions:", output).keys())
        return list()

    def get_install_permissions(self, package: str):
        """
        Returns the package runtime permissions
        :param package:
        :return:
        """
        log().verbose(f"Fetching install permissions for `{package}`...")
        code, output, error = self.dump_package(package)
        if code == ADBCommandResult.RESULT_OK and output:
            return _parse_dump_permissions("install permissions:", output)
        return dict()

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
