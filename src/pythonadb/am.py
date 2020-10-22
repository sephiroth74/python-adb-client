#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

from . import Intent
from . import ADBClient

__all__ = ["ActivityManager"]


def log():
    from . import _logger
    return _logger.get_logger(__name__)


class ActivityManager(object):
    def __init__(self, client: ADBClient):
        self._client = client

    @property
    def client(self):
        return self._client

    def broadcast(self, intent: Intent):
        arguments = intent.build()
        log().verbose(f"broadcast with arguments {arguments}")
        return self.client.shell(f"am broadcast {arguments}")

    def startservice(self, intent: Intent):
        arguments = intent.build()
        log().verbose(f"startservice with arguments {arguments}")
        return self.client.shell(f"am startservice {arguments}")

    def start(self, intent: Intent):
        arguments = intent.build()
        log().verbose(f"start with arguments {arguments}")
        return self.client.shell(f"am start {arguments}")
