"""
    Module: test_identification_type
"""
import sys
sys.path.append("../")

import unittest #pylint: disable=wrong-import-position
import mercadopago #pylint: disable=wrong-import-position

class TestIdentificationType(unittest.TestCase):
    """
    Test Module: Identification Type
    """
    sdk = mercadopago.SDK(
        "APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_find_all(self):
        """
        Test Function: Identification Type
        """
        identifications = self.sdk.identification_type().search()
        self.assertEqual(identifications["status"], 200)

if __name__ == '__main__':
    unittest.main()
