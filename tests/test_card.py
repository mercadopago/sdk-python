import sys
sys.path.append('../')

import unittest
from datetime import datetime

import mercadopago

class TestCard(unittest.TestCase):
    sdk = mercadopago.SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_all(self):
        customer_object = {
            "email": "test_payer_999857@testuser.com",
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
                "zip_code": "2300",
                "street_name": "some street"
            },
            "description": "customer description"
        }

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

        customer_saved = self.sdk.customer().create(customer_object)
        card_token_created = self.sdk.card_token().create(card_token_object)

        card_object = {
            "customer_id": customer_saved["response"]["id"],
            "token": card_token_created["response"]["id"]
        }

        card_created = self.sdk.card().create(customer_saved["response"]["id"], card_object)
        self.assertEqual(card_created["status"], 201)
        self.assertEqual(self.sdk.card().get(customer_saved["response"]["id"], card_created["response"]["id"])["status"], 200)

        self.sdk.card().delete(customer_saved["response"]["id"], card_created["response"]["id"])
        self.sdk.customer().delete(customer_saved["response"]["id"])

if __name__ == '__main__':
    unittest.main()
