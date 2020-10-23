#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import List, Dict, Optional, Union

__all__ = ["PackageParser"]


def get_line_identation(line: str) -> int:
    return len(line) - (len(line.lstrip()))


def is_line_empty(line: str) -> bool:
    return len(line.strip()) == 0


class PackageParser(object):
    """"
    Parse the dumpsys output
    """
    def __init__(self, string: str):
        lines = list(map(lambda x: x.rstrip(), string.strip().splitlines()))
        self._data = PackageParser.PackageNode.parse(lines)

    @property
    def data(self):
        return self._data

    def __contains__(self, key):
        return key in self._data

    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        else:
            return None

    """ Inner class """

    class PackageNode(object):
        def __init__(self, line: Optional[str], identation: int):
            self._data = dict()
            self._identation = identation
            if line:
                self._name = line.strip()
            else:
                self._name = None

        def __getitem__(self, key):
            return self._data[key]

        @property
        def identation(self):
            return self._identation

        def items(self):
            return self._data.items()

        def keys(self):
            return self._data.keys()

        def values(self):
            return self._data.values()

        @property
        def name(self):
            return self._name

        # noinspection PyUnresolvedReferences
        @staticmethod
        def parse(lines: List[str]) -> Dict[str, Union[dict, Dict[str, PackageNode]]]:
            result2 = dict()
            if len(lines) < 1:
                return result2

            cur_line_identation = -1
            cur_line = None
            nested_block = False

            for i in range(0, len(lines)):
                line: str = lines[i]
                if is_line_empty(line):
                    continue
                identation = get_line_identation(line)

                if i == 0 or identation == cur_line_identation:
                    line = line.strip()
                    # node = PackageParser.PackageNode(line, identation)
                    node = dict()
                    result2[line] = node
                    cur_line = line
                    cur_line_identation = identation
                    nested_block = False
                elif i > 0 and identation > cur_line_identation:
                    if not nested_block:
                        result2[cur_line] = PackageParser.PackageNode.parse(lines[i:])
                        nested_block = True
                else:
                    return result2
            return result2
