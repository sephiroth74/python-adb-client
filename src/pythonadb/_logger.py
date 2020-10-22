#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import logging

import coloredlogs
import verboselogs

__all__ = ["get_logger", "set_logging_factory"]

logging_factory_func = None

loggers = dict()


def get_logger(name: str) -> verboselogs.VerboseLogger:
    global logging_factory_func

    if logging_factory_func:
        # noinspection PyCallingNonCallable
        return logging_factory_func(name)

    global loggers
    if name not in loggers:
        logger = verboselogs.VerboseLogger(name)
    else:
        logger = loggers[name]
    return logger


def set_logging_factory(func):
    global logging_factory_func
    logging_factory_func = func
