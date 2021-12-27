"""
    Module: test_card
"""
import sys
sys.path.append("../")

from datetime import datetime #pylint: disable=wrong-import-position
import unittest #pylint: disable=wrong-import-position
import mercadopago #pylint: disable=wrong-import-position

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
            "expiration_year": datetime.now().strftime("%Y"),
            "expiration_month": "12",
            "cardholder": {
                "name": "APRO",
                "identification": {
                    "CPF": "19119119100"
                }
            }
        }

        customer_id = "732515394-bphQE9s0bz0oTD"
        card_token_created = self.sdk.card_token().create(card_token_object)

        card_object = {
            "customer_id": customer_id,
            "token": card_token_created["response"]["id"]
        }

        card_created = self.sdk.card().create(customer_id, card_object)
        self.assertIn(card_created["status"], [200, 201])
        self.assertEqual(self.sdk.card()
        .get(customer_id, card_created["response"]["id"])["status"], 200)

        self.sdk.card().delete(customer_id, card_created["response"]["id"])

if __name__ == "__main__":
    unittest.main()

    #try:
    #    print(["id"])
    #except KeyError:
    #    print("this param is unknown")
