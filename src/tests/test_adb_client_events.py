#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import unittest

from pythonadb import ADBClient, KeyCodes, CPlusPlusKeyCodes
from . import get_logger
from .test_const import DEVICE_IP

log = get_logger("==> test_adb_client_event")

THIS_FILE_NAME = os.path.basename(__file__)


class ADBClientEventsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        ADBClient.disconnect_all()

    def setUp(self) -> None:
        self.client = ADBClient(DEVICE_IP)
        self.assertTrue(DEVICE_IP, self.client.identifier)
        self.assertTrue(self.client.connect())
        self.assertTrue(self.client.is_connected())

    def test_000(self):
        print("test_000")
        events = self.client.getevent()
        log.debug(f"events: {events}")
        self.assertIsNotNone(events)
        self.assertTrue(len(events) > 0)

    def test_001(self):
        print("test_001")
        events = self.client.getevent()
        event = next(map(lambda y: y[0], filter(lambda x: x[1] == 'SCTV RC2000', events)), '/dev/input/event0')
        self.assertIsNotNone(event)

        self.client.send_key(KeyCodes.KEYCODE_HOME.value)
        time.sleep(1)

        self.client.send_raw_key(CPlusPlusKeyCodes.KEY_HOMEPAGE.value, event)
        time.sleep(1)


    # def test_002(self):
    #     print("test_001")
    #     self.client.key_down(CPlusPlusKeyCodes.KEY_UP.value)
    #     time.sleep(0.1)
    #     self.client.key_up(CPlusPlusKeyCodes.KEY_UP.value)
    #     time.sleep(1)


if __name__ == "__main__":
    unittest.main()
