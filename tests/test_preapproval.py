"""
    Module: test_preapproval
"""
import sys
sys.path.append("../")

import unittest #pylint: disable=wrong-import-position
import mercadopago #pylint: disable=wrong-import-position

class TestPreApproval(unittest.TestCase):
    """
    Test Module: PreApproval
    """
    sdk = mercadopago.SDK(
        "APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_create(self):
        """
            Function: xoxoxoxo
        """

if __name__ == "__main__":
    unittest.main()
