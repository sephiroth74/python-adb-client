#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Dict

__all__ = ["Package"]


class Package(object):
    # noinspection PyShadowingBuiltins
    def __init__(self, input: Dict[str, str]):
        self._name = input["package"]
        self._apk = input.get("apk", None)
        self._installer = input.get("installer", None)
        self._uuid = input.get("uuid", None)

    @property
    def name(self):
        return self._name

    @property
    def apk(self):
        return self._apk

    @property
    def installer(self):
        return self._installer

    @property
    def uuid(self):
        return self._uuid

    def is_system(self):
        return self._apk.startswith("/system/") if self._apk else False

    def __repr__(self):
        return f"Package<id: {id(self)}, name: {self.name}>"

    def __str__(self):
        return f"Package({self.name})"

    def __eq__(self, other):
        if isinstance(other, (Package,)):
            return self.name == other.name
        return False
