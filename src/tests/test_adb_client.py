#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from pathlib import Path

from adb import ADBClient, KeyCodes, packageparser
from adb.adb_connection import ADBCommandResult
from . import get_logger
from .test_const import DEVICE_IP, DEBUG_APK, DEBUG_APK_PACKAGE

log = get_logger("==> test_adb_client")

THIS_FILE_NAME = os.path.basename(__file__)


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        ADBClient.disconnect_all()

    def setUp(self) -> None:
        self.client = ADBClient(DEVICE_IP)
        self.assertTrue(DEVICE_IP, self.client.identifier)
        self.assertTrue(self.client.connect())
        self.assertTrue(self.client.is_connected())

    @unittest.skip
    def test_000(self):
        print("test_000")
        self.client.root()
        self.assertTrue(self.client.is_root())
        self.client.unroot()
        self.assertFalse(self.client.is_root())
        self.assertTrue(self.client.is_package_installed("com.android.bluetooth"))

    @unittest.skip
    def test_001(self):
        print("test_001")
        packages = self.client.list_packages()
        self.assertTrue(len(packages) > 0)
        self.assertIsNotNone(packages[0].name)

        packages = self.client.list_packages(args=("-f",))
        self.assertIsNotNone(packages[0].apk)
        self.assertIsNone(packages[0].uuid)
        self.assertIsNone(packages[0].installer)

        packages = self.client.list_packages(args=("-U",))
        self.assertIsNotNone(packages[0].uuid)
        self.assertIsNone(packages[0].apk)
        self.assertIsNone(packages[0].installer)

        packages = self.client.list_packages("com.android.bluetooth")
        self.assertTrue(len(packages) == 1)
        self.assertEqual("com.android.bluetooth", packages[0].name)

        packages = self.client.list_packages("com.android.bla.bla")
        self.assertTrue(len(packages) == 0)

    @unittest.skip
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

    @unittest.skip
    def test_005(self):
        print("test_005")
        address = self.client.get_mac_address()
        log.debug(f"mac address: {address}")

        # self.assertIsNotNone(address)
        # self.assertTrue(len(address) > 0)

        client_id = self.client.get_id()
        log.debug(f"id: {client_id}")
        self.assertIsNotNone(client_id)
        self.assertTrue(len(client_id) > 0)

    @unittest.skip
    def test_006(self):
        print("test_006")
        output = self.client.get_global_settings()
        self.assertIsNotNone(output)
        self.assertIn("adb_enabled", output)
        self.assertEqual("1", output["adb_enabled"])

    @unittest.skip
    def test_007(self):
        print("test_007")
        code, output, error = self.client.dump_package("com.android.bluetooth")
        self.assertEqual(ADBCommandResult.RESULT_OK, code)
        self.assertIsNotNone(output)
        self.assertTrue(len(output) > 0)

        code, output, error = self.client.dump_package("invalid.package.name")
        self.assertEqual(ADBCommandResult.RESULT_ERROR, code)
        self.assertIsNone(output)

    @unittest.skip
    def test_008(self):
        print("test_008")
        result = self.client.dumpsys_bluetooth()
        if result.is_ok() and result.output() is not None:
            self.assertIsNotNone(result.output())
        else:
            self.assertIsNotNone(result.error())

        result = self.client.dumpsys("battery")
        self.assertTrue(result.code == ADBCommandResult.RESULT_OK)
        self.assertTrue(result.is_ok())
        self.assertFalse(result.is_error())
        self.assertIsNotNone(result.output())

    @unittest.skip
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
        output = self.client.getprop()
        self.assertIsNotNone(output)
        self.assertIsInstance(output, dict)
        self.assertTrue("ro.product.model" in output)
        self.assertTrue("ro.product.name" in output)
        self.assertTrue("ro.product.device" in output)

        for key, value in output.items():
            log.debug(f"{key} = {value}")

        log.debug(f"model: {output['ro.product.model']}")
        log.debug(f"name: {output['ro.product.name']}")
        log.debug(f"device: {output['ro.product.device']}")
        # persist.sys.stb.name

    @unittest.skip
    def test_011(self):
        print("test_011")
        result = self.client.send_text("a")
        self.assertEqual(ADBCommandResult.RESULT_OK, result.code)

        result = self.client.send_key(KeyCodes.KEYCODE_WAKEUP.value)
        self.assertEqual(ADBCommandResult.RESULT_OK, result.code)

    @unittest.skip
    def test_012(self):
        print("test_012")
        result = self.client.ls("/sdcard")
        self.assertTrue(result.is_ok())
        log.debug(f"result: {result.output()}")

        if self.client.has_busybox():
            result1 = self.client.busybox(
                "ls", args=("-lHha", "--color=none", "/sdcard")
            )
            self.assertTrue(result1.is_ok())
            log.debug(f"result1: {result1.output()}")
            self.assertNotEqual(result.output(), result1.output())
        else:
            result1 = self.client.ls("/sdcard", args=("-lHha", "--color=none"))
            log.debug(f"result1: {result1.output()}")
            self.assertNotEqual(result.output(), result1.output())

    @unittest.skip
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

    @unittest.skip
    def test_014(self):
        print("test_014")
        self.assertTrue(self.client.push(__file__, f"/sdcard/{THIS_FILE_NAME}"))

        dest_file = Path(os.path.expanduser("~")) / "Desktop" / THIS_FILE_NAME
        if dest_file.exists():
            dest_file.unlink(True)

        # test dry run
        self.client.pull(
            f"/sdcard/{THIS_FILE_NAME}",
            Path(os.path.expanduser("~")) / "Desktop",
            args=("-n",),
        )
        self.assertFalse(dest_file.exists())

        self.client.pull(
            f"/sdcard/{THIS_FILE_NAME}",
            Path(os.path.expanduser("~")) / "Desktop",
            args=(
                "-z",
                "brotli",
            ),
        )
        self.assertTrue(dest_file.exists())
        dest_file.unlink()

    @unittest.skip
    def test_015(self):
        print("test_015")
        result = self.client.get_runtime_permissions("com.android.bluetooth")
        log.spam(f"permissions: {result.keys()}")
        self.assertTrue(len(result) > 0)

    @unittest.skip
    def test_016(self):
        print("test_016")
        result = self.client.get_package("com.android.bluetooth")
        log.debug(f"package: {result}")
        self.assertIsNotNone(result)
        self.assertTrue(result.is_system())
        self.assertEqual("com.android.bluetooth", result.name)
        self.assertIsNotNone(result.uuid)

    def test_017(self):
        apk_file = Path(DEBUG_APK)

        if self.client.is_package_installed(DEBUG_APK_PACKAGE):
            self.assertEqual(
                ADBCommandResult.RESULT_OK,
                self.client.uninstall_package(DEBUG_APK_PACKAGE).code,
            )

        self.assertFalse(self.client.is_package_installed(DEBUG_APK_PACKAGE))

        result = self.client.install_package(apk_file)
        log.debug(f"result = {result}")
        self.assertTrue(result.is_ok())
        self.assertTrue(self.client.is_package_installed(DEBUG_APK_PACKAGE))
        self.assertFalse(self.client.is_system_package(DEBUG_APK_PACKAGE))

        log.debug("runtime permissions:")
        for key, value in self.client.get_runtime_permissions(
            DEBUG_APK_PACKAGE
        ).items():
            log.spam(f"{key} = {value}")

        log.debug("install permissions:")
        for key, value in self.client.get_install_permissions(
            DEBUG_APK_PACKAGE
        ).items():
            log.spam(f"{key} = {value}")

        log.debug("requested permissions:")
        for line in self.client.get_requested_permissions(DEBUG_APK_PACKAGE):
            log.spam(f"permission={line}")

        result = self.client.has_runtime_permission(DEBUG_APK_PACKAGE, "android.permission.ACCESS_COARSE_LOCATION")
        result = self.client.has_runtime_permission(DEBUG_APK_PACKAGE, "android.permission.SYSTEM_ALERT_WINDOW")

    @unittest.skip
    def test_018(self):
        print("test_018")
        model = self.client.getprop("ro.product.model")
        self.assertIsNotNone(model)
        self.assertTrue(isinstance(model, str))

        result = self.client.getprop("persist.scm.dialog.allow")
        if result is None:
            result = "false"

        self.client.setprop("persist.scm.dialog.allow", "false" if result else "true")
        self.assertEqual(
            "false" if result else "true",
            self.client.getprop("persist.scm.dialog.allow"),
        )
        self.client.setprop("persist.scm.dialog.allow", "true" if result else "false")
        self.assertEqual(result, self.client.getprop("persist.scm.dialog.allow"))

    def test_019(self):
        print("test_019")
        self.assertTrue(self.client.reload_package("com.android.bluetooth").is_ok())

    def test_020(self):
        print("test_20")
        result = self.client.is_system_package("com.android.bluetooth")
        self.assertTrue(result)
        self.assertFalse(self.client.is_system_package(DEBUG_APK_PACKAGE))

    def test_021(self):
        print("test_021")
        result = self.client.dumpsys("package r service")
        parser = packageparser.PackageParser(result.output())
        log.debug(parser.data)

if __name__ == "__main__":
    unittest.main()
