#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from pathlib import Path

from pythonadb import ADBClient, PackageManager
from pythonadb.adb_connection import ADBCommandResult
from . import get_logger
from .test_const import DEVICE_IP, DEBUG_APK, DEBUG_APK_PACKAGE

log = get_logger("==> test_pm")

THIS_FILE_NAME = os.path.basename(__file__)


class PmTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        ADBClient.disconnect_all()

    def setUp(self) -> None:
        self.pm = PackageManager(ADBClient(DEVICE_IP))
        self.assertTrue(self.pm.client.connect())
        self.assertTrue(self.pm.client.is_connected())

    def test_001(self):
        print("test_001")
        packages = self.pm.list()
        self.assertTrue(len(packages) > 0)
        self.assertIsNotNone(packages[0].name)

        packages = self.pm.list(args=("-f",))
        self.assertIsNotNone(packages[0].apk)
        self.assertIsNone(packages[0].uuid)
        self.assertIsNone(packages[0].installer)

        packages = self.pm.list(args=("-U",))
        self.assertIsNotNone(packages[0].uuid)
        self.assertIsNone(packages[0].apk)
        self.assertIsNone(packages[0].installer)

        packages = self.pm.list("com.android.bluetooth")
        self.assertTrue(len(packages) == 1)
        self.assertEqual("com.android.bluetooth", packages[0].name)

        packages = self.pm.list("com.android.bla.bla")
        self.assertTrue(len(packages) == 0)

    def test_007(self):
        print("test_007")
        code, output, error = self.pm.dump("com.android.bluetooth")
        self.assertEqual(ADBCommandResult.RESULT_OK, code)
        self.assertIsNotNone(output)
        self.assertTrue(len(output) > 0)

        code, output, error = self.pm.dump("invalid.package.name")
        self.assertEqual(ADBCommandResult.RESULT_ERROR, code)
        self.assertIsNone(output)

    def test_015(self):
        print("test_015")
        result = self.pm.get_runtime_permissions("com.android.bluetooth")
        log.spam(f"permissions: {result.keys()}")
        self.assertTrue(len(result) > 0)

    def test_016(self):
        print("test_016")
        result = self.pm.find("com.android.bluetooth")
        log.debug(f"package: {result}")
        self.assertIsNotNone(result)
        self.assertTrue(result.is_system())
        self.assertEqual("com.android.bluetooth", result.name)
        self.assertIsNotNone(result.uuid)

    def test_017(self):
        apk_file = Path(DEBUG_APK)

        if self.pm.is_installed(DEBUG_APK_PACKAGE):
            self.assertEqual(
                ADBCommandResult.RESULT_OK,
                self.pm.uninstall(DEBUG_APK_PACKAGE).code,
            )

        self.assertFalse(self.pm.is_installed(DEBUG_APK_PACKAGE))

        result = self.pm.install(apk_file)
        log.debug(f"result = {result}")
        self.assertTrue(result.is_ok())
        self.assertTrue(self.pm.is_installed(DEBUG_APK_PACKAGE))
        self.assertFalse(self.pm.is_system(DEBUG_APK_PACKAGE))

        log.debug("runtime permissions:")
        for key, value in self.pm.get_runtime_permissions(DEBUG_APK_PACKAGE).items():
            log.spam(f"{key} = {value}")

        log.debug("install permissions:")
        for key, value in self.pm.get_install_permissions(DEBUG_APK_PACKAGE).items():
            log.spam(f"{key} = {value}")

        log.debug("requested permissions:")
        for line in self.pm.get_requested_permissions(DEBUG_APK_PACKAGE):
            log.spam(f"permission={line}")

        result = self.pm.has_runtime_permission(
            DEBUG_APK_PACKAGE, "android.permission.ACCESS_COARSE_LOCATION"
        )
        result = self.pm.has_runtime_permission(
            DEBUG_APK_PACKAGE, "android.permission.SYSTEM_ALERT_WINDOW"
        )

    def test_019(self):
        print("test_019")
        self.assertTrue(self.pm.forcestop("com.android.bluetooth").is_ok())

    def test_020(self):
        print("test_20")
        result = self.pm.is_system("com.android.bluetooth")
        self.assertTrue(result)
        self.assertFalse(self.pm.is_system(DEBUG_APK_PACKAGE))


if __name__ == "__main__":
    unittest.main()
