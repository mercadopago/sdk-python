import sys
sys.path.append("../")

import unittest

import mercadopago

class TestIdentificationType(unittest.TestCase):
    sdk = mercadopago.SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_find_all(self):
        identifications = self.sdk.identification_type().get_list()

        self.assertEqual(identifications["status"], 200)

if __name__ == '__main__':
    unittest.main()
