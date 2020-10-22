#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
from pathlib import Path

from pythonadb import ADBClient, KeyCodes, packageparser
from pythonadb.adb_connection import ADBCommandResult
from . import get_logger
from .test_const import DEVICE_IP

log = get_logger("==> test_adb_client")

THIS_FILE_NAME = os.path.basename(__file__)


class ADBClientTestCase(unittest.TestCase):
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

    def test_021(self):
        print("test_021")
        result = self.client.dumpsys("package r service")
        parser = packageparser.PackageParser(result.output())
        log.debug(parser.data)


if __name__ == "__main__":
    unittest.main()
