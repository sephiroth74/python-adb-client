import logging
import os
import time
import unittest
from pathlib import Path

import verboselogs
import zope.event
from adb import adb_connection

from . import get_logger

logging.basicConfig(level=verboselogs.SPAM)

log = get_logger("==> test_adb_connection", verboselogs.SPAM)

DEVICE_IP = "192.168.1.114:5555"

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
        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))

    def tearDown(self) -> None:
        adb_connection.disconnect(ip=DEVICE_IP)

    @unittest.skipIf(SKIP_TESTS, SKIP_REASON)
    def test_001(self):
        print()
        log.debug("test_001")
        adb_path = adb_connection.get_adb_path()
        self.assertIsNotNone(adb_path)
        self.assertTrue(len(adb_path) > 0)
        self.assertTrue(os.path.exists(adb_path))

    @unittest.skipIf(SKIP_TESTS, SKIP_REASON)
    def test_002(self):
        print()
        log.debug("test_002")
        devices = adb_connection.devices()
        self.assertIsNotNone(devices)

        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))
        devices = adb_connection.devices()
        self.assertIsNotNone(devices)
        self.assertTrue(len(devices) > 0)

        for device in devices:
            log.debug(f"attached device: {device}")
            log.debug(f"is_usb:{device.is_usb()}, is_emulator:{device.is_emulator()}, is_wifi:{device.is_wifi()}")
            transport_id = device.transport_id
            self.assertTrue(transport_id is not None and len(transport_id) > 0)
            if device.is_wifi():
                self.assertTrue(adb_connection.is_connected(ip=device.identifier))
            else:
                self.assertTrue(adb_connection.is_connected(transport_id=device.transport_id))

    @unittest.skipIf(SKIP_TESTS, SKIP_REASON)
    def test_003(self):
        print()
        log.debug("test_003")
        if adb_connection.is_connected(ip=DEVICE_IP):
            self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

        devices = list(filter(lambda x: x.identifier == DEVICE_IP, adb_connection.devices()))
        self.assertTrue(len(devices) == 0)

        self.assertTrue(adb_connection.connect(DEVICE_IP))

        devices = list(filter(lambda x: x.identifier == DEVICE_IP, adb_connection.devices()))
        self.assertTrue(len(devices) > 0)

        self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

    @unittest.skipIf(SKIP_TESTS, SKIP_REASON)
    def test_004(self):
        log.debug("test_004")
        self.assertTrue(adb_connection.connect(DEVICE_IP))
        self.assertTrue(adb_connection.reboot(ip=DEVICE_IP))
        sleep(5)
        self.assertTrue(adb_connection.wait_for_device(ip=DEVICE_IP))
        self.assertTrue(adb_connection.is_connected(ip=DEVICE_IP))

    @unittest.skipIf(SKIP_TESTS, SKIP_REASON)
    def test_005(self):
        print()
        log.debug("test_005")
        # connect
        self.assertTrue(adb_connection.connect(DEVICE_IP))

        # should not be root
        if adb_connection.is_root(ip=DEVICE_IP):
            adb_connection.unroot(DEVICE_IP)
            sleep(2)

        # check is not root
        self.assertFalse(adb_connection.is_root(ip=DEVICE_IP))

        # adb root
        adb_connection.root(ip=DEVICE_IP)
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
        sleep(2)

        # check is not root
        self.assertFalse(adb_connection.is_root(ip=DEVICE_IP))
        self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

    @unittest.skipIf(SKIP_TESTS, SKIP_REASON)
    def test_006(self):
        print()
        log.debug("test_006")
        self.assertTrue(adb_connection.connect(DEVICE_IP))

        if not adb_connection.is_root(ip=DEVICE_IP):
            self.assertTrue(adb_connection.root(ip=DEVICE_IP))

        self.assertTrue(adb_connection.remount_as(ip=DEVICE_IP, writeable=True))
        sleep(2)

        self.assertTrue(adb_connection.remount_as(ip=DEVICE_IP, writeable=False))
        sleep(2)

        adb_connection.unroot(ip=DEVICE_IP)
        sleep(2)

        self.assertTrue(adb_connection.is_connected(ip=DEVICE_IP))
        self.assertFalse(adb_connection.is_root(ip=DEVICE_IP))
        self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

    @unittest.skipIf(SKIP_TESTS, SKIP_REASON)
    def test_007(self):
        print()
        log.debug("test_007")
        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))
        self.assertTrue(adb_connection.wait_for_device(ip=DEVICE_IP))

    @unittest.skipIf(SKIP_TESTS, SKIP_REASON)
    def test_008(self):
        print()
        log.debug("test_008")
        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))
        self.assertTrue(adb_connection.disconnect_all())
        self.assertFalse(adb_connection.is_connected(ip=DEVICE_IP))

    @unittest.skipIf(SKIP_TESTS, SKIP_REASON)
    def test_009(self):
        print()
        log.debug("test_009")
        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))
        self.assertEqual("/system/bin/cat", adb_connection.which("cat", ip=DEVICE_IP))
        self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

    @unittest.skipIf(SKIP_TESTS, SKIP_REASON)
    def test_010(self):
        print()
        log.debug("test_010")
        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))

        if adb_connection.is_root(ip=DEVICE_IP):
            if adb_connection.unroot(ip=DEVICE_IP):
                adb_connection.wait_for_device(ip=DEVICE_IP)

        self.assertTrue(adb_connection.is_connected(ip=DEVICE_IP))
        self.assertFalse(adb_connection.is_root(ip=DEVICE_IP))

        if adb_connection.which("busybox", ip=DEVICE_IP):
            result: adb_connection.ADBCommandResult = adb_connection.busybox("whoami", ip=DEVICE_IP)
            self.assertEqual(adb_connection.ADBCommandResult.RESULT_OK, result.code)
            self.assertEqual("shell", result.result)

    def test_011(self):
        print()
        log.debug("test_011")
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
            self.assertIsNotNone(mdns_services.result)

    def test_013(self):
        print("test_013")
        dest_file = Path(os.path.dirname(__file__)) / "bugreport.zip"
        dest_file.unlink(True)
        self.assertFalse(dest_file.exists())
        self.assertTrue(adb_connection.bugreport(dest_file, ip=DEVICE_IP))
        self.assertTrue(dest_file.exists())
        dest_file.unlink(True)


if __name__ == '__main__':
    unittest.main()
