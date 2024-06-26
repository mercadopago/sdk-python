"""
    Module: test_chargeback
"""
import os
import unittest
import mercadopago


class TestChargeback(unittest.TestCase):
    """
    Test Module: Chargeback
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_search_chargeback(self):
        """
        Test Function: Chargeback
        """
        filters_chargeback = {
            "payment_id": "12345"
        }

        chargebacks = self.sdk.chargeback().search(filters=filters_chargeback)
        self.assertEqual(chargebacks["status"], 200)


if __name__ == "__main__":
    unittest.main()
