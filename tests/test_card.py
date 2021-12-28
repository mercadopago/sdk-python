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

    @classmethod
    def setUpClass(cls):
        cls._customer_id = cls.createCustomer(cls())["response"]["id"]

    @classmethod
    def tearDownClass(cls):
        cls.deleteCustomer(cls())

    def test_all(self):
        """
        Test Function: Card
        """

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
        print(self._customer_id)

        card_object = {
            "customer_id": self._customer_id,
            "token": card_token_created["response"]["id"]
        }

        card_created = self.sdk.card().create(self._customer_id, card_object)
        self.assertIn(card_created["status"], [200, 201])
        self.assertEqual(self.sdk.card().get(self._customer_id, card_created["response"]["id"])["status"], 200)

        self.sdk.card().delete(self._customer_id, card_created["response"]["id"])

    def createCustomer(self):
        customer_object = {
            "email": "test_payer_999942@testuser.com",
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

        return self.sdk.customer().create(customer_object)

    def deleteCustomer(self):
        self.sdk.customer().delete(self._customer_id)


if __name__ == "__main__":
    unittest.main()
