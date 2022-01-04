"""
    Module: test_payment_methods
"""
import unittest

import mercadopago


class TestPaymentMethods(unittest.TestCase):
    """
    Test Module: Payment Methods
    """
    sdk = mercadopago.SDK(
        "APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_find(self):
        """
        Test Function: Payment Methods
        """
        self.assertEqual(self.sdk.payment_methods().list_all()["status"], 200)


if __name__ == "__main__":
    unittest.main()
