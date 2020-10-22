#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Optional, List, Dict, Any

__all__ = ["Intent"]


class Intent(object):
    """
    See https://developer.android.com/studio/command-line/adb#IntentSpec
    """

    class Extras(object):
        def __init__(self):
            self.es: Dict[str, str] = dict()
            self.ez: Dict[str, bool] = dict()
            self.ei: Dict[str, int] = dict()
            self.el: Dict[str, int] = dict()
            self.ef: Dict[str, float] = dict()
            self.eu: Dict[str, str] = dict()
            self.ecn: Dict[str, str] = dict()
            self.eia: Dict[str, List[int]] = dict()
            self.ela: Dict[str, List[int]] = dict()
            self.efa: Dict[str, List[float]] = dict()
            self.grant_read_uri_permission = False
            self.grant_write_uri_permission = False
            self.exclude_stopped_packages = False
            self.include_stopped_packages = False
            self.raw_extras: Optional[str] = None

        def build(self) -> str:
            if self.raw_extras:
                return self.raw_extras

            args: List[str] = list()
            append_dict_argument(args, "--es", self.es)
            append_dict_argument(args, "--ez", self.ez)
            append_dict_argument(args, "--ei", self.ei)
            append_dict_argument(args, "--el", self.el)
            append_dict_argument(args, "--ef", self.ef)
            append_dict_argument(args, "--eu", self.eu)
            append_dict_argument(args, "--ecn", self.ecn)
            append_dict_argument(args, "--eia", self.eia)
            append_dict_argument(args, "--ela", self.ela)
            append_dict_argument(args, "--efa", self.efa)
            if self.grant_read_uri_permission:
                args.append("--grant-read-uri-permission")
            if self.grant_write_uri_permission:
                args.append("--grant-write-uri-permission")
            if self.exclude_stopped_packages:
                args.append("--exclude-stopped-packages")
            if self.include_stopped_packages:
                args.append("--include-stopped-packages")
            return " ".join(args)

    def __init__(self, action: str, extras: Optional[Extras] = Extras()):
        self.action = action
        self.data_uri: Optional[str] = None
        self.mime_type: Optional[str] = None
        self.category: Optional[str] = None
        self.component: Optional[str] = None
        self.flags: int = 0
        self.wait: bool = False
        self.user_id: int = 0
        self.extras = extras

    def waitforlaunchtocomplete(self, value: bool):
        self.wait = value

    def build(self) -> str:
        args = list()

        if self.wait:
            args.append("-W")

        if self.user_id > 0:
            args.append(f"--user {self.user_id}")

        args.append(f"-a {self.action}")
        append_str_argument(args, "-n", self.component)
        append_str_argument(args, "-d", self.data_uri)
        append_str_argument(args, "-t", self.mime_type)
        append_str_argument(args, "-c", self.category)
        append_int_argument(args, "-f", self.flags, 0)
        if self.extras:
            args.append(self.extras.build())
        return " ".join(args)


def append_dict_argument(target: List[str], key: str, option: Dict[str, Any]):
    if option:
        for k, v in option.items():
            string = f"{key} {k} "
            if isinstance(v, list):
                string += " ".join(str(x) for x in v)
            else:
                string += v
            target.append(string)


def append_str_argument(target: List[str], key: str, value: Optional[str]):
    if value:
        target.append(f"{key} {value}")


def append_int_argument(target: List[str], key: str, value: int, nullvalue: int):
    if value != nullvalue:
        target.append(f"{key} {value}")
