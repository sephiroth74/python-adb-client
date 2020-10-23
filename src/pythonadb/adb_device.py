#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import multiprocessing
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Optional, IO, Dict

from .packageparser import PackageParser
from . import ADBClient
from . import ActivityManager
from . import PackageManager
from . import adb_connection
from . import propertyparser

__all__ = ["ADBDevice"]


def log():
    from . import _logger
    logger = _logger.get_logger(__name__)
    return logger


class ADBDevice(object):
    def __init__(self, client: ADBClient):
        self._client = client
        self._name: Optional[str] = None
        self._am = ActivityManager(self._client)
        self._pm = PackageManager(self._client)
        self._executor = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())

    @property
    def client(self) -> ADBClient:
        return self._client

    @property
    def am(self) -> ActivityManager:
        return self._am

    @property
    def pm(self) -> PackageManager:
        return self._pm

    @property
    def name(self) -> Optional[str]:
        if self._name is None:
            self._name = self.client.getprop("ro.build.product")
        return self._name

    @property
    def api_level(self):
        return int(self.client.getprop("ro.build.version.sdk"))

    @property
    def android_release_version(self):
        return self.client.getprop("ro.build.version.release")

    @property
    def build_prop(self) -> propertyparser.PropertyParser:
        return self._read_build_prop()

    def quit(self):
        log().info("Quitting...")
        self._executor.shutdown()
        self._client = None

    def write_screencap(self, fp: IO) -> bool:
        log().verbose("write screencap")
        return self.client.execute("exec-out screencap -p", stdout=fp)

    def save_screencap(self, output: str):
        log().verbose(f"save screencap to {output}")
        return self.client.shell("screencap -p %s" % output)

    def screenrecord(
            self,
            file: str,
            bugreport: bool = False,
            bitrate: int = 8000000,
            timelimit: int = 0,
            **kwargs,
    ) -> bool:
        log().verbose(f"screenrecord to {file}")

        args = ["--bit-rate", str(bitrate)]
        if bugreport:
            args.append("--bugreport")
        if timelimit > 0:
            args.extend(("--time-limit", str(timelimit)))
        args.append(file)

        return self.client.shell(
            "screenrecord", **adb_connection.extends_extra_arguments(*args, **kwargs)
        )

    """ -----------------------------------------------------------------------"""
    """ Events """
    """ -----------------------------------------------------------------------"""

    def async_send_key(self, key: int):
        return self._executor.submit(self.client.send_key, key)

    def async_send_text(self, char: str):
        assert type(char) is str
        return self._executor.submit(self.client.send_text, char)

    """ -----------------------------------------------------------------------"""
    """ Activities """
    """ -----------------------------------------------------------------------"""

    def open_settings(self):
        log().verbose("Opening Settings Activity...")
        return self.client.shell(
            "am start -a android.intent.action.MAIN -n com.android.settings/.Settings"
        )

    def open_bluetooth_settings(self):
        log().verbose("Opening Blueooth Settings Activity...")
        return self.client.shell("am start -a android.settings.BLUETOOTH_SETTINGS")

    def open_monitor_client(self):
        log().verbose("Opening Monitor Client...")
        return self.client.shell(
            "am start -a android.intent.action.MAIN -n com.iwedia.stbmclient/com.example.stbmclient.STBMonitorClientActivity"
        )

    """ DumpSys Wrapper """

    def get_services_info(self) -> Optional[Dict]:
        result = self.client.dumpsys("package r service")
        if result.is_ok():
            p = PackageParser(result.output())
            if 'Service Resolver Table:' in p:
                if 'Non-Data Actions:' in p['Service Resolver Table:']:
                    return p['Service Resolver Table:']['Non-Data Actions:']
        return None

    def get_receivers_info(self) -> Optional[Dict]:
        """
        Executes `dumpsys package r receiver` on the connected device and return a table
        with all the registered receivers
        :return:
        """
        result = self.client.dumpsys("package r receiver")
        if result.is_ok():
            p = PackageParser(result.output())
            if 'Receiver Resolver Table:' in p:
                if 'Non-Data Actions:' in p['Receiver Resolver Table:']:
                    return p['Receiver Resolver Table:']['Non-Data Actions:']
        return None

    """ -----------------------------------------------------------------------"""
    """ Private Methods """
    """ -----------------------------------------------------------------------"""

    def _read_build_prop(self) -> propertyparser.PropertyParser:
        parser = propertyparser.PropertyParser()
        if self.client.root():
            properties = self.client.cat("/system/build.prop")
            if properties:
                return parser.read_string(properties)
        return parser
