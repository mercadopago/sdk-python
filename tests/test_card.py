"""
    Module: test_card
"""
import sys
import unittest
import mercadopago
from datetime import datetime

sys.path.append("../")


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
        customer_object = {
            "email": "test_payer_999940@testuser.com",
            "first_name": "Rafa",
            "last_name": "Williner",
            "phone": {
                "area_code": "03492",
                "number": "432334"
            },
            "identification": {
                "type": "DNI",
                "number": "29804555"
            },
            "address": {
                "zip_code": "47807078",
                "street_name": "some street",
                "street_number": 123
            },
            "description": "customer description"
        }

        customer_created = self.sdk.customer().create(customer_object)
        customer_id = customer_created["response"]["id"]

        card_token_object = {
            "card_number": "4074090000000004",
            "security_code": "123",
            "expiration_year": datetime.now().strftime("%Y"),
            "expiration_month": "12",
            "cardholder": {
                "name": "APRO",
                "identification": {
                    "CPF": "19119119100"
                }
            }
        }

        card_token_created = self.sdk.card_token().create(card_token_object)

        card_object = {
            "customer_id": customer_id,
            "token": card_token_created["response"]["id"]
        }

        card_created = self.sdk.card().create(customer_id, card_object)
        self.assertIn(card_created["status"], [200, 201])
        self.assertEqual(self.sdk.card().get(customer_id, card_created["response"]["id"])["status"], 200)

        self.sdk.card().delete(customer_id, card_created["response"]["id"])
        self.sdk.customer().delete(customer_id)


if __name__ == "__main__":
    unittest.main()
