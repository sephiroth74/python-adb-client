from ._version import __version__
from .types import *
from .intent import Intent
from .keycodes import KeyCodes, CPlusPlusKeyCodes
from . import adb_connection
from .adb_client import ADBClient
from .am import ActivityManager
from .pm import PackageManager
from .adb_device import ADBDevice
from ._logger import set_logging_factory

__author__ = "Alessandro Crugnola"

__doc__ = f"""
Python ADB Client
version: {__version__}
author: {__author__}
"""
