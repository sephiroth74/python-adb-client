#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import configparser

from pathlib import Path
from typing import Optional, Dict

from . import adb_connection
from . import ADBClient
from . import propertyparser

__all__ = ['ADBDevice']


class ADBDevice(object):
    def __init__(self, client: ADBClient):
        self._client = client
        self._buid_prop = None

    @property
    def client(self):
        return self._client

    @property
    def build_prop(self):
        if self._buid_prop is None:
            self._buid_prop = self._read_build_prop()
        return self._buid_prop

    def _read_build_prop(self):
        if self.client.root():
            properties = self.client.cat("/system/build.prop")
            if properties:
                return propertyparser.PropertyParser().read_string(properties)
        return None
