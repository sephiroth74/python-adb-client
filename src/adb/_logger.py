#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import logging
import verboselogs

# import coloredlogs

__all__ = ['get_logger', 'logging']

FMT = '%(asctime)s %(levelname)-10s %(name)-12s %(lineno)-4d %(processName)-12s   %(message)s'


def _fmt_filter(record):
    record.levelname = '[%s]' % record.levelname
    record.funcName = '[%s]' % record.funcName
    return True


def get_logger(name: str) -> verboselogs.VerboseLogger:
    logger = verboselogs.VerboseLogger(name)
    # coloredlogs.install(logging.root.level, logger=logger,
    #                     fmt='%(levelname)-10s %(name)-12s %(lineno)-4d %(processName)-12s   %(message)s')
    f = logging.Formatter(FMT)
    h = logging.StreamHandler()
    h.setFormatter(f)
    logger.addFilter(_fmt_filter)
    return logger
