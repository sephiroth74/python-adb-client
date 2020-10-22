import unittest

from adb import Intent


class ItentBuilderTestCase(unittest.TestCase):
    def test_001(self):
        print("test_001")

        i = Intent(action="android.intent.action.VIEW")
        i.waitforlaunchtocomplete(True)
        i.component = "com.my.component/.internal.ComponentName"
        i.data_uri = "http://www.google.com"
        i.extras.es["navigation_path"] = "/test/1"
        i.extras.es["another_one"] = "2"
        i.extras.eia["input_array_int"] = [1, 2, 3]

        string = i.build()

        self.assertEqual(
            "-W -a android.intent.action.VIEW -n com.my.component/.internal.ComponentName -d http://www.google.com --es navigation_path /test/1 --es another_one 2 --eia input_array_int 1 2 3",
            string,
        )


if __name__ == "__main__":
    unittest.main()
