#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Optional, Any
from enum import Enum

__all__ = ["ADBEvent", "ADBConnectionEvent"]


class ADBEvent(object):
    def __init__(self, event_type: ADBConnectionEvent, event_data: Optional[Any]):
        self._event_type = event_type
        self._event_data = event_data

    @property
    def event_type(self):
        return self._event_type

    @property
    def event_data(self):
        return self._event_data

    def __str__(self):
        return f"ADBEvent(type={self._event_type}, data={self._event_data})"


class ADBConnectionEvent(Enum):
    Reboot = "reboot"
    Connect = "connect"
    Disconnect = "disconnect"
