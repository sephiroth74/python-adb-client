#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python3 -m tests.test_intent_builder
"""

import unittest

from pythonadb import Intent
from . import get_logger

log = get_logger("==> test_intent")


class ItentBuilderTestCase(unittest.TestCase):
    def test_001(self):
        print("test_001")

        log.debug("sending android.intent.action.VIEW...")

        i = Intent(action="android.intent.action.VIEW")
        i.waitforlaunchtocomplete(True)
        i.component = "com.my.component/.internal.ComponentName"
        i.data_uri = "http://www.google.com"
        i.extras.es["navigation_path"] = "/test/1"
        i.extras.es["another_one"] = "2"
        i.extras.eia["input_array_int"] = [1, 2, 3]

        string = i.build()

        self.assertEqual(
            "-W -a android.intent.action.VIEW -n com.my.component/.internal.ComponentName -d http://www.google.com --es "
            "navigation_path /test/1 --es another_one 2 --eia input_array_int 1 2 3",
            string,
        )

    def test_002(self):
        print("test_002")

        i = Intent(action="custom")
        i.waitforlaunchtocomplete(True)
        i.extras.es["primo"] = "uno"
        i.extras.ez["secondo"] = True

        print(i.build())

        i = Intent(action="second_custom")
        i.waitforlaunchtocomplete(True)
        i.extras.ei["ei.1"] = 1
        print(i.build())


if __name__ == "__main__":
    unittest.main()
