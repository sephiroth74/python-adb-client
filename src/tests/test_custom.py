#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python3 -m tests.test_pm
"""

import os
import unittest

from pythonadb import ADBClient, ADBDevice
from . import get_logger
from .test_const import DEVICE_IP

log = get_logger("==> test_custom")

THIS_FILE_NAME = os.path.basename(__file__)


class CustomTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        ADBClient.disconnect_all()

    def setUp(self) -> None:
        self.device = ADBDevice(ADBClient(DEVICE_IP))
        self.assertTrue(self.device.client.connect())

    def test_001(self):
        print("test_001")

        self.assertTrue(self.device.client.has_busybox())
        self.assertTrue(self.device.client.hash_which())
        self.assertFalse(self.device.client.exists("something"))

        cat = self.device.client.which("cat")
        self.assertIsNotNone(cat)
        log.debug(f"cat: {cat}")

        cat = self.device.client.busybox("which cat")
        self.assertIsNotNone(cat)
        log.debug(f"cat: {cat}")

        packages = self.device.pm.list()
        self.assertTrue(len(packages) > 0)
        self.assertIsNotNone(packages[0].name)

        for line in packages:
            log.debug(f"package: {line}")

        self.assertTrue(self.device.pm.is_installed("com.swisscom.swisscomTv"))

        #
        # packages = self.device.pm.list(args=("-f",))
        # self.assertIsNotNone(packages[0].apk)
        # self.assertIsNone(packages[0].uuid)
        # self.assertIsNone(packages[0].installer)
        #
        # packages = self.device.pm.list(args=("-U",))
        # self.assertIsNotNone(packages[0].uuid)
        # self.assertIsNone(packages[0].apk)
        # self.assertIsNone(packages[0].installer)
        #
        # packages = self.device.pm.list("com.android.bluetooth")
        # self.assertTrue(len(packages) == 1)
        # self.assertEqual("com.android.bluetooth", packages[0].name)
        #
        # packages = self.device.pm.list("com.android.bla.bla")
        # self.assertTrue(len(packages) == 0)


if __name__ == "__main__":
    unittest.main()
