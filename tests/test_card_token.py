"""
    Module: test_card_token
"""
import sys
sys.path.append('../')

import unittest
from datetime import datetime

import mercadopago

class TestCardToken(unittest.TestCase): #pylint: disable=missing-class-docstring
    sdk = mercadopago.SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966") #pylint: disable=line-too-long

    def test_all(self): #pylint: disable=missing-function-docstring
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

        card_token_created = self.sdk.card_token().create(card_token_object)

        self.assertEqual(card_token_created["status"], 201)
        self.assertEqual(self.sdk.card_token()
        .get(card_token_created["response"]["id"])["status"], 200)

if __name__ == '__main__':
    unittest.main()
