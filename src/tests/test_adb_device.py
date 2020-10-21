#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from pathlib import Path

from adb import ADBClient, KeyCodes, ADBDevice
from adb.adb_connection import ADBCommandResult
from . import get_logger
from .test_const import DEVICE_IP, DEBUG_APK, DEBUG_APK_PACKAGE

log = get_logger("==> test_adb_device")

THIS_FILE_NAME = os.path.basename(__file__)


class ADBDeviceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        ADBClient.disconnect_all()

    def setUp(self) -> None:
        self.device = ADBDevice(ADBClient(DEVICE_IP))
        self.assertTrue(self.device.client.connect())

    def test_001(self):
        print("test_001")
        properties = self.device.build_prop
        print(properties.keys())
        print(properties.items())


if __name__ == '__main__':
    unittest.main()
