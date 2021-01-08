"""
    Module: test_identification_type
"""
import sys
sys.path.append("../")

import unittest

import mercadopago

class TestIdentificationType(unittest.TestCase): #pylint: disable=missing-class-docstring
    sdk = mercadopago.SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966") #pylint: disable=line-too-long

    def test_find_all(self): #pylint: disable=missing-function-docstring
        identifications = self.sdk.identification_type().search()

        self.assertEqual(identifications["status"], 200)

if __name__ == '__main__':
    unittest.main()
