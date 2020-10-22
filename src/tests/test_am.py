#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
import time

from adb import ADBClient, Intent, ActivityManager, KeyCodes
from . import get_logger
from .test_const import DEVICE_IP

log = get_logger("==> test_am")

THIS_FILE_NAME = os.path.basename(__file__)


class ActivityManagerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        ADBClient.disconnect_all()

    def setUp(self) -> None:
        self.am = ActivityManager(ADBClient(DEVICE_IP))
        self.assertTrue(self.am.client.connect())
        self.am.client.send_key(KeyCodes.KEYCODE_HOME.value)
        time.sleep(1)

    def test_001(self):
        print("test_001")
        intent = Intent("swisscom.android.tv.action.NAVIGATE", extras=Intent.Extras())
        intent.waitforlaunchtocomplete(True)
        intent.extras.es['swisscom.android.tv.extra.NAVIGATION_PATH'] = '/sport'
        result = self.am.broadcast(intent)
        log.debug(result)
        self.assertTrue(result.is_ok())

    def test_002(self):
        print("test_002")
        time.sleep(1)
        self.am.client.send_key(KeyCodes.KEYCODE_BACK.value)
        time.sleep(1)

    def test_003(self):
        print("test_003")
        package = self.am.client.get_package("com.swisscom.android.tv.library")
        user_id = package.uuid
        log.debug(f"user_id: {user_id}")

        intent = Intent("swisscom.android.tv.action.HANDLE_NOTIFICATION")
        intent.component = "com.swisscom.android.tv.library/.internal.services.NotificationService"
        intent.extras.es["swisscom.android.tv.extra.NOTIFICATION_EVENT"] = "Eleanor.Notification.Show.LoginCode"
        intent.extras.es["swisscom.android.tv.extra.NOTIFICATION_DATA"] = '{}'
        result = self.am.startservice(intent)
        log.debug(result)
        self.assertTrue(result.is_ok())

        time.sleep(1)
        self.am.client.send_key(KeyCodes.KEYCODE_BACK.value)

    def test_004(self):
        print("test_005")
        intent = Intent("android.intent.action.VIEW")
        intent.data_uri = "http://www.google.com"
        intent.waitforlaunchtocomplete(True)
        result = self.am.broadcast(intent)
        log.debug(result)
        self.assertTrue(result.is_ok())


if __name__ == '__main__':
    unittest.main()
