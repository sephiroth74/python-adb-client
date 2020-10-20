#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from pathlib import Path

from adb import KeyCodes
from adb import ADBClient
from adb.adb_connection import ADBCommandResult
from . import get_logger
from .test_const import DEVICE_IP, DEBUG_APK, DEBUG_APK_PACKAGE

log = get_logger("==> test_adb_client")

THIS_FILE_NAME = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ADBClient(DEVICE_IP)
        self.assertTrue(DEVICE_IP, self.client.identifier)
        self.assertTrue(self.client.connect())
        self.assertTrue(self.client.is_connected())
        if self.client.is_root():
            self.client.unroot()

    def test_001(self):
        print("test_001")
        code, stdout, stderr = self.client.list_packages()
        self.assertEqual(ADBCommandResult.RESULT_OK, code)
        self.assertIsNotNone(stdout)
        self.assertIsNone(stderr)

        code, stdout, stderr = self.client.list_packages(package="com.android.bluetooth")
        self.assertTrue(len(stdout) > 0)
        self.assertTrue("com.android.bluetooth" in stdout)

    def test_002(self):
        print("test_002")
        packages = self.client.packages("com.android.bluetooth")
        self.assertEqual(list, type(packages))
        self.assertTrue(len(packages) > 0)
        self.assertTrue(self.client.is_package_installed("com.android.bluetooth"))
        self.assertFalse(self.client.is_package_installed("com.test.1.bluetooth"))

    def test_003(self):
        print("test_003")
        self.assertTrue(self.client.is_dir("/sdcard"))
        self.assertTrue(self.client.exists("/sdcard"))
        self.assertTrue(self.client.is_symlink("/sdcard"))

        self.assertFalse(self.client.is_file("/a.file.that/does.not.exist/I_hope"))
        self.assertFalse(self.client.exists("/a.file.that/does.not.exist/I_hope"))
        self.assertFalse(self.client.is_dir("/a.file.that/does.not.exist/I_hope"))
        self.assertFalse(self.client.is_symlink("/a.file.that/does.not.exist/I_hope"))

    @unittest.skip
    def test_004(self):
        print("test_004")
        self.client.root()

        self.assertTrue(self.client.is_file("/system/build.prop"))
        self.assertTrue(self.client.exists("/system/build.prop"))

        output = self.client.cat("/init.rc")
        self.assertIsNotNone(output)
        self.assertTrue(len(output) > 0)

        self.client.unroot()

        with self.assertRaises(IOError):
            self.client.cat("/hello.world.bats")

    def test_005(self):
        print("test_005")
        address = self.client.get_mac_address()
        log.debug(f"mac address: {address}")

        # self.assertIsNotNone(address)
        # self.assertTrue(len(address) > 0)

        id = self.client.get_id()
        log.debug(f"id: {id}")
        self.assertIsNotNone(id)
        self.assertTrue(len(id) > 0)

    def test_006(self):
        print("test_006")
        output = self.client.get_global_settings()
        self.assertIsNotNone(output)
        self.assertIn("adb_enabled", output)
        self.assertEqual('1', output['adb_enabled'])

    def test_007(self):
        print("test_007")
        code, output, error = self.client.dump_package("com.android.bluetooth")
        self.assertEqual(ADBCommandResult.RESULT_OK, code)
        self.assertIsNotNone(output)
        self.assertTrue(len(output) > 0)

        code, output, error = self.client.dump_package("invalid.package.name")
        self.assertEqual(ADBCommandResult.RESULT_ERROR, code)
        self.assertIsNone(output)

    def test_008(self):
        print("test_008")
        result = self.client.dumpsys_bluetooth()
        if result.is_ok() and result.output() is not None:
            log.debug(f"result: {result}")
            self.assertIsNotNone(result.output())
        else:
            self.assertIsNotNone(result.error())

        result = self.client.dumpsys("battery")
        self.assertTrue(result.code == ADBCommandResult.RESULT_OK)
        self.assertTrue(result.is_ok())
        self.assertFalse(result.is_error())
        self.assertIsNotNone(result.output())

    def test_009(self):
        print("test_009")
        code, output, error = self.client.dumpsys_meminfo("com.android.bluetooth")
        self.assertEqual(ADBCommandResult.RESULT_OK, code)
        self.assertIsNotNone(output)
        log.debug(f"meminfo: {output}")

        code, result, error = self.client.dumpsys_meminfo("invalid.package")
        self.assertEqual(ADBCommandResult.RESULT_ERROR, code)

    def test_010(self):
        print("test_010")
        output = self.client.get_properties()
        self.assertIsNotNone(output)
        self.assertIsInstance(output, dict)
        self.assertTrue("ro.product.model" in output)
        self.assertTrue("ro.product.name" in output)
        self.assertTrue("ro.product.device" in output)

        log.debug(f"model: {output['ro.product.model']}")
        log.debug(f"name: {output['ro.product.name']}")
        log.debug(f"device: {output['ro.product.device']}")

    def test_011(self):
        print("test_011")
        result = self.client.send_text('a')
        self.assertEqual(ADBCommandResult.RESULT_OK, result.code)

        result = self.client.send_key(KeyCodes.KEYCODE_WAKEUP.value)
        self.assertEqual(ADBCommandResult.RESULT_OK, result.code)

    def test_012(self):
        print("test_012")
        result = self.client.ls("/sdcard")
        self.assertTrue(result.is_ok())
        log.debug(f"result: {result.output()}")

        if self.client.has_busybox():
            result1 = self.client.busybox("ls", args=("-lHha", "--color=none", "/sdcard"))
            self.assertTrue(result1.is_ok())
            log.debug(f"result1: {result1.output()}")
            self.assertNotEqual(result.output(), result1.output())
        else:
            result1 = self.client.ls("/sdcard", args=("-lHha", "--color=none"))
            log.debug(f"result1: {result1.output()}")
            self.assertNotEqual(result.output(), result1.output())

    def test_013(self):
        print("test_013")

        if self.client.exists(f"/sdcard/{THIS_FILE_NAME}"):
            self.client.remove(f"/sdcard/{THIS_FILE_NAME}")
            self.assertFalse(self.client.exists(f"/sdcard/{THIS_FILE_NAME}"))

        self.assertTrue(self.client.push(__file__, f"/sdcard/{THIS_FILE_NAME}"))
        self.assertTrue(self.client.exists(f"/sdcard/{THIS_FILE_NAME}"))
        self.assertTrue(self.client.is_file(f"/sdcard/{THIS_FILE_NAME}"))

        result = self.client.cat(f"/sdcard/{THIS_FILE_NAME}")
        self.assertIsNotNone(result)

        with open(__file__, "r") as fp:
            this_text = fp.read().strip()
            self.assertTrue(result == this_text)

    def test_014(self):
        print("test_014")

        self.assertTrue(self.client.push(__file__, f"/sdcard/{THIS_FILE_NAME}"))

        dest_file = Path(os.path.expanduser("~")) / "Desktop" / THIS_FILE_NAME
        if dest_file.exists():
            dest_file.unlink(True)

        # test dry run
        self.client.pull(f"/sdcard/{THIS_FILE_NAME}", Path(os.path.expanduser("~")) / "Desktop", args=("-n",))
        self.assertFalse(dest_file.exists())
        self.client.pull(f"/sdcard/{THIS_FILE_NAME}", Path(os.path.expanduser("~")) / "Desktop", args=("-z", "brotli",))

        self.assertTrue(dest_file.exists())
        dest_file.unlink()

    def test_015(self):
        print("test_015")
        result = self.client.get_runtime_permissions("com.android.bluetooth")
        self.assertTrue(len(result) > 0)

    def test_016(self):
        print("test_016")
        result = self.client.get_package_apk("com.android.bluetooth")
        log.debug(f"apk location: {result}")
        self.assertIsNotNone(result)
        self.assertTrue(result.endswith(".apk"))

    def test_017(self):
        apk_file = Path(DEBUG_APK)

        if self.client.is_package_installed(DEBUG_APK_PACKAGE):
            self.assertEqual(ADBCommandResult.RESULT_OK, self.client.uninstall_package(DEBUG_APK_PACKAGE).code)

        self.assertFalse(self.client.is_package_installed(DEBUG_APK_PACKAGE))

        result = self.client.install_package(apk_file)
        log.debug(f"result = {result}")
        self.assertTrue(result.is_ok())
        self.assertTrue(self.client.is_package_installed(DEBUG_APK_PACKAGE))

        log.debug("runtime permissions:")
        for key, value in self.client.get_runtime_permissions(DEBUG_APK_PACKAGE).items():
            log.spam(f"{key} = {value}")

        log.debug("install permissions:")
        for key, value in self.client.get_install_permissions(DEBUG_APK_PACKAGE).items():
            log.spam(f"{key} = {value}")

        log.debug("requested permissions:")
        for line in self.client.get_requested_permissions(DEBUG_APK_PACKAGE):
            log.spam(f"permission={line}")

        if self.client.grant_runtime_permission(DEBUG_APK_PACKAGE, "android.permission.ACCESS_FINE_LOCATION").is_ok():
            permissions = dict(filter(lambda x: x[0] == "android.permission.ACCESS_FINE_LOCATION" and x[1],
                                      self.client.get_runtime_permissions(DEBUG_APK_PACKAGE).items()))
            log.debug(f"granted: {permissions}")
            self.assertTrue(len(permissions) == 1)
        else:
            log.warning("failed to grant permission")


if __name__ == '__main__':
    unittest.main()
