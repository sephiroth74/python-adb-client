#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import re
import tempfile
from pathlib import Path
from typing import Dict, List, Optional

from xml.etree import ElementTree

from . import ADBClient
from . import Package
from .adb_connection import ADBCommandResult, extends_extra_arguments

__all__ = ["PackageManager"]

# noinspection RegExpRedundantEscape
package_pattern = re.compile(
    r"package:(?P<apk>.*\.apk)?=?(?P<package>[a-zA-Z0-9\.]+)\s*(installer=(?P<installer>[\w\.]+))?\s*(uid:(?P<uuid>[\w]+))?"
)


def log():
    from . import _logger
    return _logger.get_logger(__name__)


class PackageManager(object):
    def __init__(self, client: ADBClient):
        self._client = client
        self._has_cmd = False
        self._has_cmd_checked = False

    @property
    def client(self):
        return self._client

    def dump(self, package: str):
        if not self.is_installed(package):
            return ADBCommandResult.from_error()
        return self.client.shell(f"pm dump {package}")

    @property
    def has_cmd(self):
        if not self._has_cmd_checked:
            self._has_cmd = self.client.which("cmd") is not None
            self._has_cmd_checked = True
        return self._has_cmd

    """ -----------------------------------------------------------------------"""
    """ Permissions """
    """ -----------------------------------------------------------------------"""

    def grant_permission(self, package: str, permission: str):
        log().verbose(f"Granting '{permission}' to '{package}'...")
        return self.client.shell(f"pm grant {package} {permission}")

    def revoke_permission(self, package: str, permission: str):
        log().verbose(f"Revoking '{permission}' from '{package}'...")
        return self.client.shell(f"pm revoke {package} {permission}")

    def has_runtime_permission(self, package: str, permission: str) -> bool:
        """Test if the given package has the runtime permission granted"""
        return any(
            x[0] == permission and x[1]
            for x in self.get_runtime_permissions(package).items()
        )

    def get_runtime_permissions(self, package: str) -> Dict[str, bool]:
        """
        Returns the package runtime permissions
        :param package:
        :return:
        """
        log().verbose(f"Fetching runtime permissions for `{package}`...")
        code, output, error = self.dump(package)
        if code == ADBCommandResult.RESULT_OK and output:
            return _parse_dump_permissions("runtime permissions:", output)
        return dict()

    def get_requested_permissions(self, package: str) -> List[str]:
        """
        Returns the package runtime permissions
        :param package:
        :return:
        """
        log().verbose(f"Fetching requested permissions for `{package}`...")
        code, output, error = self.dump(package)
        if code == ADBCommandResult.RESULT_OK and output:
            return list(
                _parse_dump_permissions("requested permissions:", output).keys()
            )
        return list()

    def get_install_permissions(self, package: str) -> Dict[str, bool]:
        """
        Returns the package runtime permissions
        :param package:
        :return:
        """
        log().verbose(f"Fetching install permissions for `{package}`...")
        code, output, error = self.dump(package)
        if code == ADBCommandResult.RESULT_OK and output:
            return _parse_dump_permissions("install permissions:", output)
        return dict()

    """ -----------------------------------------------------------------------"""
    """ Install/Uninstall/Clear """
    """ -----------------------------------------------------------------------"""

    def install(self, apk: Path, **kwargs) -> ADBCommandResult:
        log().verbose(f"install {apk}")
        return self._install_package(apk, **kwargs)

    def uninstall(self, package: str) -> ADBCommandResult:
        """
        uninstall [-k] PACKAGE
            remove this app package from the device
            '-k': keep the data and cache directories
        """
        log().verbose(f"uninstall {package}")
        if self.is_installed(package):
            if self.is_system(package):
                return self._uninstall_package(package, args=("--user 0",))
            else:
                return self._uninstall_package(package)
        else:
            log().warning(f"{package} is not installed")
            return ADBCommandResult.from_error()

    def remove_entry(self, package: str) -> bool:
        """
        Remove the package entry from packages.xml and packages.list inside /data/system
        :param package:
        :return:
        """
        return _remove_package_from_packages(self.client, package)

    def clear(self, package: str) -> ADBCommandResult:
        log().verbose(f"clear {package}")
        if self.is_installed(package):
            if self.is_system(package):
                return self._clear_package(package, args=("--user 0",))
            else:
                return self._clear_package(package)
        else:
            log().warning(f"{package} is not installed")
            return ADBCommandResult.from_error()

    def forcestop(self, package: str):
        return self.client.shell(f"am force-stop {package}")

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
        return self.client.capture_output(
            command="install-multi-package",
            **extends_extra_arguments(*list(map(lambda x: str(x), apks)), **kwargs),
        )

    """
    """

    def list(self, package: Optional[str] = None, **kwargs):
        if self.has_cmd:
            return _cmd_list(self.client, package, **kwargs)
        return _pm_list(self.client, package, **kwargs)

    def is_installed(self, package: str) -> bool:
        return any(x.name == package for x in self.list(package))

    def find(self, package: str) -> Optional[Package]:
        result = self.list(package, args=("-f", "-U", "-i"))
        log().spam(f"result: {result}")
        return next((x for x in result if x.name == package), None)

    def is_system(self, package: str):
        result = self.find(package)
        if result is not None:
            return result.is_system()
        return False

    """ -----------------------------------------------------------------------"""
    """ Private Methods """
    """ -----------------------------------------------------------------------"""

    def _uninstall_package(self, package: str, **kwargs) -> ADBCommandResult:
        return self.client.shell(
            "pm uninstall",
            **extends_extra_arguments(str(package), **kwargs),
        )

    def _clear_package(self, package: str, **kwargs) -> ADBCommandResult:
        return self.client.shell(
            "pm clear", **extends_extra_arguments(str(package), **kwargs)
        )

    def _install_package(self, apk: Path, **kwargs) -> ADBCommandResult:
        return self.client.capture_output(
            command="install",
            **extends_extra_arguments(str(apk), **kwargs),
        )


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


def _remove_package_from_packages(client: ADBClient, package) -> bool:
    if not _remove_entry_from_packages_list(client, package):
        return False
    return _remove_entry_from_packages_xml(client, package)


def _remove_entry_from_packages_list(client: ADBClient, package) -> bool:
    log().debug("Removing entry from '/data/system/packages.list'...")
    content = client.cat("/data/system/packages.list")
    splitted_content = list(filter(lambda x: not x.startswith(package), content.splitlines()))
    local_file = Path(tempfile.gettempdir()) / "packages.list"
    with open(local_file, "w") as fp:
        for line in splitted_content:
            fp.write(line)
        fp.close()

    if not client.push(Path(local_file), "/data/system/"):
        log().warning("Failed to push '%s' to '/data/system/'" % local_file)
        return False
    return True


def _remove_entry_from_packages_xml(client: ADBClient, package) -> bool:
    log().debug("Removing entry from '/data/system/packages.xml'...")
    content = client.cat("/data/system/packages.xml")

    root = ElementTree.ElementTree(ElementTree.fromstring(content))
    for elem in root.findall(".//package[@name='%s']" % package):
        log().verbose(f"Removing {elem} from node")
        root.getroot().remove(elem)

    local_file = Path(tempfile.gettempdir()) / "packages.xml"

    with open(local_file, "wb") as fp:
        root.write(fp, encoding="utf-8")

    if not client.push(Path(local_file), "/data/system/"):
        log().warning(f"Failed to push '{local_file}' to '/data/system/'")
        return False
    return True


def _pm_list(client: ADBClient, package: Optional[str] = None, **kwargs):
    """
    Uses legacy "pm list packages"
    pm list packages: prints all packages, optionally only
    those whose package name contains the text in FILTER.  Options:
        -f: see their associated file.
        -d: filter to only show disbled packages.
        -e: filter to only show enabled packages.
        -s: filter to only show system packages.
        -3: filter to only show third party packages.
        -i: see the installer for the packages.
        -u: also include uninstalled packages.
    :param client: current ADBClient
    :param package:
    :param kwargs:
    :return:
    """
    result = client.shell(
        "pm list packages",
        **extends_extra_arguments(f"{package if package else ''}", **kwargs),
    )
    if result.is_ok() and result.output():
        return _parse_packages(result.output())
    return list()


def _cmd_list(client: ADBClient, package: Optional[str] = None, **kwargs):
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

    :param client: current ADBClient
    :param package: optional package to look for
    :param kwargs:
    :return:
    """
    result = client.shell(
        "cmd package list packages",
        **extends_extra_arguments(f"{package if package else ''}", **kwargs),
    )
    if result.is_ok() and result.output():
        return _parse_packages(result.output())
    return list()


def _parse_packages(output: str) -> List[Package]:
    packages = list()
    for line in output.splitlines():
        match = re.match(package_pattern, line)
        if match:
            packages.append(Package(match.groupdict()))
    return packages
