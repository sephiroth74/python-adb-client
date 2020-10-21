#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import logging

import verboselogs

# import coloredlogs

__all__ = ["get_logger", "logging"]


def _fmt_filter(record):
    record.levelname = "[%s]" % record.levelname
    record.funcName = "[%s]" % record.funcName
    return True


def get_logger(name: str) -> verboselogs.VerboseLogger:
    logger = verboselogs.VerboseLogger(name)
    # logger.addFilter(_fmt_filter)
    return logger
