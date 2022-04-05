"""
    Module: test_chargeback
"""
import unittest

import mercadopago


class TestChargeback(unittest.TestCase):
    """
    Test Module: Chargeback
    """
    sdk = mercadopago.SDK(
        "APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

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
