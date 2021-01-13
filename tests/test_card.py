"""
    Module: test_card
"""
import sys
from datetime import datetime
import unittest
import mercadopago
sys.path.insert("..", 0)

class TestCard(unittest.TestCase):
    """
    Test Module: Card
    """
    sdk = mercadopago.SDK(
        "APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_all(self):
        """
        Test Function: Card
        """
        card_token_object = {
            "card_number": "4074090000000004",
            "security_code": "123",
            "expiration_year": datetime.now().strftime('%Y'),
            "expiration_month": "12",
            "cardholder": {
                "name": "APRO",
                "identification": {
                    "CPF": "19119119100"
                }
            }
        }

        customer_id = "685810954-vbrXmBzkHl4UJ9"
        card_token_created = self.sdk.card_token().create(card_token_object)

        card_object = {
            "customer_id": customer_id,
            "token": card_token_created["response"]["id"]
        }

        card_created = self.sdk.card().create(customer_id, card_object)
        self.assertEqual(card_created["status"], 200)
        self.assertEqual(self.sdk.card()
        .get(customer_id, card_created["response"]["id"])["status"], 200)

        self.sdk.card().delete(customer_id, card_created["response"]["id"])
        self.sdk.customer().delete(customer_id)

if __name__ == '__main__':
    unittest.main()
