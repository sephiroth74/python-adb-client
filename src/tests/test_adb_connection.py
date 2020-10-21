import os
import time
import unittest
from pathlib import Path

import zope.event

from adb import adb_connection
from . import get_logger
from .test_const import DEVICE_IP

log = get_logger("==> test_adb_connection")

SKIP_TESTS = True
SKIP_REASON = "skip"


# coverage run -m unittest discover
# coverage report -m
# coverage html

def handle_event(event):
    log.verbose(f"Received Event: {event}")


def sleep(amount: float):
    log.debug(f"sleeping for {amount}...")
    time.sleep(amount)


zope.event.subscribers.append(handle_event)


class ADBConnectionTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('setUp')
        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))

    def tearDown(self) -> None:
        print('tearDown')
        adb_connection.disconnect(ip=DEVICE_IP)

    def test_001(self):
        print("test_001")
        adb_path = adb_connection.get_adb_path()
        self.assertIsNotNone(adb_path)
        self.assertTrue(len(adb_path) > 0)
        self.assertTrue(os.path.exists(adb_path))

    def test_002(self):
        print("test_002")
        devices = adb_connection.devices(args=("-l",))
        self.assertIsNotNone(devices)
        self.assertTrue(len(devices) > 0)

        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))
        devices = adb_connection.devices()
        self.assertIsNotNone(devices)
        self.assertTrue(len(devices) > 0)

        for device in devices:
            log.debug(f"attached device: {device}")

    def test_003(self):
        print("test_003")
        if adb_connection.is_connected(ip=DEVICE_IP):
            self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

        devices = list(filter(lambda x: DEVICE_IP in x, adb_connection.devices()))
        self.assertTrue(len(devices) == 0)
        self.assertTrue(adb_connection.connect(DEVICE_IP))

        devices = list(filter(lambda x: DEVICE_IP in x, adb_connection.devices()))
        self.assertTrue(len(devices) > 0)
        self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

    def test_005(self):
        print("test_005")
        # connect
        self.assertTrue(adb_connection.connect(DEVICE_IP))

        # should not be root
        if adb_connection.is_root(ip=DEVICE_IP):
            adb_connection.unroot(DEVICE_IP)
            adb_connection.reconnect_device(ip=DEVICE_IP)
            sleep(2)

        # check is not root
        self.assertFalse(adb_connection.is_root(ip=DEVICE_IP))

        # adb root
        adb_connection.root(ip=DEVICE_IP)
        adb_connection.reconnect_device(ip=DEVICE_IP)
        if not adb_connection.is_connected(DEVICE_IP): adb_connection.wait_for_device(DEVICE_IP)
        sleep(2)

        # check is root
        self.assertTrue(adb_connection.is_root(ip=DEVICE_IP))
        sleep(2)

        # check if connected...
        if not adb_connection.is_connected(ip=DEVICE_IP):
            self.assertTrue(adb_connection.connect(ip=DEVICE_IP))

        self.assertTrue(adb_connection.is_connected(ip=DEVICE_IP))

        # unroot
        adb_connection.unroot(ip=DEVICE_IP)
        adb_connection.reconnect_device(ip=DEVICE_IP)
        sleep(2)

        # check is not root
        self.assertFalse(adb_connection.is_root(ip=DEVICE_IP))
        self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

    def test_006(self):
        print("test_006")
        self.assertTrue(adb_connection.connect(DEVICE_IP))

        if not adb_connection.is_root(ip=DEVICE_IP):
            self.assertTrue(adb_connection.root(ip=DEVICE_IP))
            adb_connection.reconnect_device(ip=DEVICE_IP)
            if not adb_connection.is_connected(DEVICE_IP): adb_connection.wait_for_device(DEVICE_IP)

        self.assertTrue(adb_connection.remount_as(ip=DEVICE_IP, writeable=True))
        sleep(2)

        self.assertTrue(adb_connection.remount_as(ip=DEVICE_IP, writeable=False))
        sleep(2)

        adb_connection.unroot(ip=DEVICE_IP)
        adb_connection.reconnect_device(ip=DEVICE_IP)
        if not adb_connection.is_connected(DEVICE_IP): adb_connection.wait_for_device(DEVICE_IP)
        sleep(2)

        self.assertTrue(adb_connection.is_connected(ip=DEVICE_IP))
        self.assertFalse(adb_connection.is_root(ip=DEVICE_IP))
        self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

    def test_008(self):
        print("test_008")
        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))
        self.assertTrue(adb_connection.disconnect_all())
        self.assertFalse(adb_connection.is_connected(ip=DEVICE_IP))

    def test_009(self):
        print("test_009")
        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))
        self.assertEqual("/system/bin/cat", adb_connection.which("cat", ip=DEVICE_IP))
        self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

    def test_010(self):
        print("test_010")
        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))

        if adb_connection.is_root(ip=DEVICE_IP):
            if adb_connection.unroot(ip=DEVICE_IP):
                adb_connection.reconnect_device(DEVICE_IP)
                if not adb_connection.is_connected(DEVICE_IP): adb_connection.wait_for_device(DEVICE_IP)

        self.assertTrue(adb_connection.is_connected(ip=DEVICE_IP))
        self.assertFalse(adb_connection.is_root(ip=DEVICE_IP))

        if adb_connection.which("busybox", ip=DEVICE_IP):
            result: adb_connection.ADBCommandResult = adb_connection.busybox("whoami", ip=DEVICE_IP)
            self.assertEqual(adb_connection.ADBCommandResult.RESULT_OK, result.code)
            self.assertEqual("shell", result.output())

    def test_011(self):
        print("test_011")
        version = adb_connection.version()
        self.assertIsNotNone(version)
        for line in version.splitlines():
            log.debug(line)

    def test_012(self):
        print("test_012")
        mdns_check = adb_connection.mdns_check()
        log.debug(f"mdns_check: {mdns_check}")
        if mdns_check.code == 0:
            mdns_services = adb_connection.mdns_services()
            log.debug(f"mdns_services: {mdns_services}")
            self.assertIsNotNone(mdns_services.output())

    def test_013(self):
        print("test_013")
        dest_file = Path(os.path.dirname(__file__)) / "bugreport.zip"
        dest_file.unlink(True)
        self.assertFalse(dest_file.exists())
        self.assertTrue(adb_connection.bugreport(str(dest_file), ip=DEVICE_IP))
        self.assertTrue(dest_file.exists())
        dest_file.unlink(True)

    def test_014(self):
        print("test_004")
        self.assertTrue(adb_connection.connect(DEVICE_IP))
        self.assertTrue(adb_connection.reboot(ip=DEVICE_IP))
        sleep(5)
        self.assertTrue(adb_connection.wait_for_device(ip=DEVICE_IP))
        self.assertTrue(adb_connection.is_connected(ip=DEVICE_IP))


if __name__ == '__main__':
    unittest.main()
