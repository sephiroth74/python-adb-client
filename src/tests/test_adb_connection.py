import logging
import os
import time
import unittest

import coloredlogs
import verboselogs
import zope.event
from adb import adb_connection

logging.basicConfig(level=logging.SPAM)
log = verboselogs.VerboseLogger("=====> test_adb_connection")

coloredlogs.install(logging.root.level, fmt='%(asctime)s %(levelname)-10s %(name)-12s %(lineno)-4d %(processName)-12s   %(message)s')

DEVICE_IP = "192.168.1.114:5555"


def handle_event(event):
    log.spam(f"Received Event: {event}")


zope.event.subscribers.append(handle_event)


class ADBConnectionTestCase(unittest.TestCase):
    def test_001(self):
        """test adb_path exists"""
        log.debug("test_001")
        adb_path = adb_connection.get_adb_path()
        self.assertIsNotNone(adb_path)
        self.assertTrue(len(adb_path) > 0)
        self.assertTrue(os.path.exists(adb_path))

    def test_002(self):
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

    def test_003(self):
        log.debug("test_003")
        if adb_connection.is_connected(ip=DEVICE_IP):
            self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

        devices = list(filter(lambda x: x.identifier == DEVICE_IP, adb_connection.devices()))
        self.assertTrue(len(devices) == 0)

        self.assertTrue(adb_connection.connect(DEVICE_IP))

        devices = list(filter(lambda x: x.identifier == DEVICE_IP, adb_connection.devices()))
        self.assertTrue(len(devices) > 0)

        self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

    @unittest.skip
    def test_004(self):
        log.debug("test_004")
        self.assertTrue(adb_connection.connect(DEVICE_IP))
        self.assertTrue(adb_connection.reboot(ip=DEVICE_IP))
        time.sleep(5)
        self.assertTrue(adb_connection.wait_for_device(ip=DEVICE_IP))

    def test_005(self):
        log.debug("test_005")
        # connect
        self.assertTrue(adb_connection.connect(DEVICE_IP))

        # should not be root
        if adb_connection.is_root(ip=DEVICE_IP):
            self.assertTrue(adb_connection.unroot(DEVICE_IP))

        # check is not root
        self.assertFalse(adb_connection.is_root(ip=DEVICE_IP))

        # adb root
        self.assertTrue(adb_connection.root(ip=DEVICE_IP))

        # check is root
        self.assertTrue(adb_connection.is_root(ip=DEVICE_IP))

        # sleep...
        log.debug("sleeping...")
        time.sleep(2)

        # check if connected...
        if not adb_connection.is_connected(ip=DEVICE_IP):
            self.assertTrue(adb_connection.connect(ip=DEVICE_IP))

        self.assertTrue(adb_connection.is_connected(ip=DEVICE_IP))

        # unroot
        adb_connection.unroot(ip=DEVICE_IP)

        # check is not root
        self.assertFalse(adb_connection.is_root(ip=DEVICE_IP))

    def test_006(self):
        log.debug("test_006")
        self.assertTrue(adb_connection.connect(DEVICE_IP))

        if not adb_connection.is_root(ip=DEVICE_IP):
            self.assertTrue(adb_connection.root(ip=DEVICE_IP))

        self.assertTrue(adb_connection.remount_as(ip=DEVICE_IP, writeable=True))
        time.sleep(2)

        self.assertTrue(adb_connection.remount_as(ip=DEVICE_IP, writeable=False))
        time.sleep(2)

        adb_connection.unroot(ip=DEVICE_IP)
        self.assertFalse(adb_connection.is_root(ip=DEVICE_IP))
        self.assertTrue(adb_connection.disconnect(ip=DEVICE_IP))

    def test_007(self):
        log.debug("test_007")
        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))
        self.assertTrue(adb_connection.wait_for_device(ip=DEVICE_IP))

    def test_008(self):
        log.debug("test_008")
        self.assertTrue(adb_connection.connect(ip=DEVICE_IP))
        self.assertTrue(adb_connection.disconnect_all())
        self.assertFalse(adb_connection.is_connected(ip=DEVICE_IP))

    #
    # def test_002(self):
    #     log.debug("test_002")
    #     self.assertTrue(adb_connection.disconnect_all())
    #     self.assertFalse(adb_connection.is_connected(DEVICE_IP))
    #
    # def test_003(self):
    #     log.debug("test_003")
    #     self.assertTrue(adb_connection.connect(DEVICE_IP))
    #     self.assertTrue(len(adb_connection.devices()) > 0)
    #     self.assertTrue(adb_connection.disconnect_all())
    #
    # def test_004(self):
    #     log.debug("test_004")
    #     self.assertTrue(adb_connection.connect(DEVICE_IP))
    #     self.assertTrue(adb_connection.wait_for_device(DEVICE_IP))
    #     self.assertTrue(adb_connection.disconnect(DEVICE_IP))


if __name__ == '__main__':
    unittest.main()
