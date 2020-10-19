import unittest

from adb import ADBClient
from adb.adb_connection import ADBCommandResult
from . import get_logger
from .test_const import DEVICE_IP

log = get_logger("==> test_adb_client")

TV_LIB_PACKAGE_NAME = "com.swisscom.android.tv.library"


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ADBClient(DEVICE_IP)

    def test_001(self):
        print("test_001")
        self.client.connect()
        code, stdout, stderr = self.client.list_packages()
        self.assertEqual(ADBCommandResult.RESULT_OK, code)
        self.assertIsNotNone(stdout)
        self.assertIsNone(stderr)

        code, stdout, stderr = self.client.list_packages(package="com.android.bluetooth")
        self.assertEqual("package:com.android.bluetooth", stdout)

    def test_002(self):
        print("test_002")
        packages = self.client.packages("com.android.bluetooth")
        self.assertEqual(list, type(packages))
        self.assertTrue(len(packages) > 0)
        self.assertTrue(self.client.is_installed("com.android.bluetooth"))
        self.assertFalse(self.client.is_installed("com.test.1.bluetooth"))

    def test_003(self):
        print("test_003")
        self.assertTrue(self.client.is_file("/init.rc"))
        self.assertTrue(self.client.exists("/init.rc"))

        self.assertTrue(self.client.is_dir("/sdcard"))
        self.assertTrue(self.client.exists("/sdcard"))
        self.assertTrue(self.client.is_symlink("/sdcard"))

        self.assertFalse(self.client.is_file("/a.file.that/does.not.exist/I_hope"))
        self.assertFalse(self.client.exists("/a.file.that/does.not.exist/I_hope"))
        self.assertFalse(self.client.is_dir("/a.file.that/does.not.exist/I_hope"))
        self.assertFalse(self.client.is_symlink("/a.file.that/does.not.exist/I_hope"))

    def test_004(self):
        print("test_004")
        output = self.client.cat("/init.rc")
        self.assertIsNotNone(output)
        self.assertTrue(len(output) > 0)

        with self.assertRaises(IOError):
            self.client.cat("/hello.world.bats")

    def test_005(self):
        print("test_005")
        address = self.client.get_mac_address()
        log.debug(f"mac address: {address}")
        self.assertIsNotNone(address)
        self.assertTrue(len(address) > 0)

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
        code, output, error = self.client.dumpsys_bluetooth()
        self.assertEqual(ADBCommandResult.RESULT_OK, code)
        self.assertIsNotNone(output)

    def test_009(self):
        print("test_009")
        code, output, error = self.client.dumpsys_meminfo("com.android.bluetooth")
        self.assertEqual(ADBCommandResult.RESULT_OK, code)
        self.assertIsNotNone(output)
        log.debug(f"meminfo: {output}")

        code, result, error = self.client.dumpsys_meminfo("invalid.package")
        self.assertEqual(ADBCommandResult.RESULT_ERROR, code)

    if __name__ == '__main__':
        unittest.main()
