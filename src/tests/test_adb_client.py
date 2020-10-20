import os
import unittest

from adb import KeyCodes
from adb import ADBClient
from adb.adb_connection import ADBCommandResult
from . import get_logger
from .test_const import DEVICE_IP

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
        self.assertTrue(self.client.is_installed("com.android.bluetooth"))
        self.assertFalse(self.client.is_installed("com.test.1.bluetooth"))

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
        code, output, error = self.client.get_package_info("com.android.bluetooth")
        self.assertEqual(ADBCommandResult.RESULT_OK, code)
        self.assertIsNotNone(output)
        self.assertTrue(len(output) > 0)

        code, output, error = self.client.get_package_info("invalid.package.name")
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

    if __name__ == '__main__':
        unittest.main()
