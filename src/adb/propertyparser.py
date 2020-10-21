#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

__all__ = ["PropertyParser"]

from typing import KeysView, Optional, ItemsView


class PropertyParser:
    def __init__(self):
        self.propDict = dict()

    def read_string(self, string: str) -> PropertyParser:
        for propLine in string.splitlines():
            prop_def = propLine.strip()
            if len(prop_def) == 0:
                continue
            if prop_def[0] in ("!", "#"):
                continue
            punctuation = [prop_def.find(c) for c in ":= "] + [len(prop_def)]
            found = min([pos for pos in punctuation if pos != -1])
            name = prop_def[:found].rstrip()
            value = prop_def[found:].lstrip(":= ").rstrip()
            self.propDict[name] = value
        return self

    def parse_file(self, filename: str) -> PropertyParser:
        with open(filename, "r") as propFile:
            data = propFile.read()
        return self.read_string(data)

    def keys(self) -> KeysView[str]:
        return self.propDict.keys()

    def items(self) -> ItemsView[str, str]:
        return self.propDict.items()

    def write(self, fp):
        for key in self.propDict.keys():
            fp.write("%s=%s\n" % (key, self.propDict[key]))

    def has_option(self, name: str) -> bool:
        return name in self.propDict

    def get_option(self, name: str) -> Optional[str]:
        if self.has_option(name):
            return self.propDict[name]
        else:
            return None

    def set_option(self, name: str, value: str):
        self.propDict[name] = value

    def replace_option(self, name: str, value: str) -> bool:
        if self.has_option(name):
            if self.get_option(name) == value:
                return False
        self.set_option(name, value)
        return True

    def __eq__(self, other) -> bool:
        if isinstance(other, PropertyParser):
            return self.keys() == other.keys()
        return False
