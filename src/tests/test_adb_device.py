#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import threading
import time
import unittest
from pathlib import Path

from adb import ADBClient, ADBDevice, KeyCodes, Intent
from . import get_logger
from .test_const import DEVICE_IP, DESKTOP_FOLDER

log = get_logger("==> test_adb_device")

THIS_FILE_NAME = os.path.basename(__file__)


class ADBDeviceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        ADBClient.disconnect_all()

    def setUp(self) -> None:
        self.device = ADBDevice(ADBClient(DEVICE_IP))
        self.assertTrue(self.device.client.connect())

    @unittest.skip
    def test_001(self):
        print("test_001")
        properties = self.device.build_prop
        self.assertIsNotNone(properties)
        self.assertTrue(len(properties.keys()) > 0)
        print(properties.keys())
        print(properties.items())

    def test_002(self):
        print("test_002")
        device_name = self.device.name
        log.debug(f"device name: {device_name}")
        self.assertIsNotNone(device_name)

    def test_003(self):
        """Screenshot"""
        print("test_003")
        api_level = self.device.api_level
        log.debug(f"api level: {api_level}")

        release = self.device.android_release_version
        self.assertIsNotNone(release)
        log.debug(f"release: {release}")

        local_screenshot = DESKTOP_FOLDER / "screenshot.png"
        local_screenshot.unlink(True)

        if api_level >= 26:
            with open(local_screenshot, "w") as fp:
                result = self.device.write_screencap(fp)
                self.assertTrue(result)
            self.assertTrue(local_screenshot.exists())
            local_screenshot.unlink(True)

    def test_007(self):
        print("test_007")
        self.assertTrue(
            self.device.async_send_key(KeyCodes.KEYCODE_DPAD_CENTER.value)
            .result()
            .is_ok()
        )
        time.sleep(1)
        self.assertTrue(
            self.device.async_send_key(KeyCodes.KEYCODE_DPAD_DOWN.value)
            .result()
            .is_ok()
        )

    def test_008(self):
        print("test_008")
        future = self.device.async_send_text("a")
        self.assertTrue(future.result().is_ok())

    def test_009(self):
        print("test_009")
        self.assertTrue(self.device.clear_package("com.android.bluetooth"))

    def test_098(self):
        """Remote screenshot"""
        print("test_004")
        local_screenshot = DESKTOP_FOLDER / "screenshot.png"
        local_screenshot.unlink(True)
        tmp_dir = Path("/data/local/tmp")
        tmp_file = tmp_dir / local_screenshot.name

        if self.device.client.exists(str(tmp_file)):
            self.device.client.remove(str(tmp_file))

        result = self.device.save_screencap(str(tmp_file))
        log.debug(result)
        self.assertTrue(result.is_ok())
        self.assertTrue(self.device.client.exists(str(tmp_file)))

        self.assertTrue(self.device.client.pull(str(tmp_file), DESKTOP_FOLDER))
        self.assertTrue(local_screenshot.exists())
        local_screenshot.unlink(True)

    def test_099(self):
        """Screen Record"""
        print("test_005")

        local_screen_record = DESKTOP_FOLDER / "screen_record.mp4"
        local_screen_record.unlink(True)

        tmp_dir = Path("/sdcard")
        tmp_file = str(tmp_dir / local_screen_record.name)

        if self.device.client.exists(tmp_file):
            self.device.client.remove(tmp_file)
            time.sleep(1)

        log.debug("record screen few seconds...")
        self.device.screenrecord(file=tmp_file, bugreport=False, timelimit=6)
        log.debug("wait for the device to write the file...")
        time.sleep(5)

        self.device.client.pull(tmp_file, DESKTOP_FOLDER)
        self.assertTrue(local_screen_record.exists())
        local_screen_record.unlink(True)


if __name__ == "__main__":
    unittest.main()
