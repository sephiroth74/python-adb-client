#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

import os

DEVICE_IP = "192.168.1.43:5555"
# DEVICE_IP = "emulator-5554"

DEBUG_APK = os.path.join(os.path.dirname(__file__), "assets/app-debug.apk")
DEBUG_APK_PACKAGE = "it.sephiroth.android.library.uigestures.demo"

DESKTOP_FOLDER = Path(os.path.expanduser("~")) / "Desktop"
