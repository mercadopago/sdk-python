"""
    Module: test_user
"""
import sys
sys.path.append("../")

import unittest #pylint: disable=wrong-import-position
import mercadopago #pylint: disable=wrong-import-position

class TestUser(unittest.TestCase): #pylint: disable=missing-class-docstring
    sdk = mercadopago.SDK(
        "APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_find_user(self): #pylint: disable=missing-function-docstring
        self.assertEqual(self.sdk.user().get()["status"], 200)

if __name__ == '__main__':
    unittest.main()
