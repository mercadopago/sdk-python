"""
    Module: test_payment_methods
"""
import os
import unittest
import mercadopago


class TestPaymentMethods(unittest.TestCase):
    """
    Test Module: Payment Methods
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_find(self):
        """
        Test Function: Payment Methods
        """
        self.assertEqual(self.sdk.payment_methods().list_all()["status"], 200)


if __name__ == "__main__":
    unittest.main()
