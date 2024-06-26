"""
    Module: test_card_token
"""
from datetime import datetime
import os
import unittest
import mercadopago


class TestCardToken(unittest.TestCase):
    """
    Test Module: Card Token
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_all(self):
        """
        Test Function: Card Token
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

        self.assertEqual(card_token_created["status"], 201)
        self.assertEqual(self.sdk.card_token()
                         .get(card_token_created["response"]["id"])["status"], 200)


if __name__ == "__main__":
    unittest.main()
