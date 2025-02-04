"""
    Module: test_order
"""
from datetime import datetime
import os
import unittest
import random
import mercadopago


class TestOrder(unittest.TestCase):
    """
    Test Module: Order
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_create(self):
        """
        Test Function: Order
        """
        card_token_object = {
            "card_number": "5031433215406351",
            "security_code": "123",
            "expiration_year": "2025",
            "expiration_month": "11",
            "cardholder": {
                "name": "APRO"
            }
        }

        card_token_created = self.sdk.card_token().create(card_token_object)
        random_email_id = random.randint(100000, 999999)
        order_object = {
            "type": "online",
            "total_amount": "1000.00",
            "external_reference": "ext_ref_1234",
            "transactions": {
            "payments": [
                {
                "amount": "1000.00",
                "payment_method": {
                    "id": "master",
                    "type": "credit_card",
                    "token": card_token_created["response"]["id"],
                    "installments": 12
                }
                }
            ]
            },
            "payer": {
            "email": f"test_payer_{random_email_id}@testuser.com"
            }
        }
        
        order_created = self.sdk.order().create(order_object)
        self.assertEqual(order_created["status"], 201)
        self.assertEqual(order_created["response"]["status"], "processed")


class TestsTransaction(unittest.TestCase):
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def create_card_token(self):
        card_token_object = {
            "card_number": "5031433215406351",
            "security_code": "123",
            "expiration_year": "2025",
            "expiration_month": "11",
            "cardholder": {
                "name": "APRO"
            }
        }
        print("Creating card token...")
        card_token_created = self.sdk.card_token().create(card_token_object)
        print("Card token creation response:", card_token_created)

        if card_token_created.get("status") != 201 or not card_token_created.get("response"):
            self.fail(f"Failed to create card token: {card_token_created}")
        return card_token_created["response"]["id"]

    def create_order_builder_mode(self, card_token_id):
        random_email_id = random.randint(100000, 999999)
        order_object_cc = {
            "type": "online",
            "processing_mode": "manual",
            "total_amount": "200.00",
            "external_reference": "ext_ref_1234",
            "payer": {
                "email": f"test_payer_{random_email_id}@testuser.com"
            },
        }
        print("Creating order in builder mode...")
        order_created = self.sdk.order().create(order_object_cc)
        print("Order creation response:", order_created)

        if order_created.get("status") != 201 or not order_created.get("response"):
            self.fail(f"Failed to create order: {order_created}")
        return order_created["response"]["id"]

    def test_add_transaction(self):
        card_token_id = self.create_card_token()
        print("Card token ID:", card_token_id)

        order_id = self.create_order_builder_mode(card_token_id)
        print("Order ID:", order_id)

        transaction_object = {
            "payments": [
                {
                    "amount": "1000.00",
                    "payment_method": {
                        "id": "master",
                        "type": "credit_card",
                        "token": card_token_id,
                        "installments": 12
                    }
                }
            ]
        }

        print("Adding transaction...")
        transaction_added = self.sdk.order().add_transaction(order_id, transaction_object)
        print("Transaction addition response:", transaction_added)

        self.assertEqual(transaction_added["status"], 201)
        self.assertEqual(transaction_added["response"]["status"], "processed")

    def test_cancel_transaction(self):
        card_token_id = self.create_card_token()
        order_id = self.create_order_builder_mode(card_token_id)

        transaction_object = {
            "payments": [
                {
                    "amount": "1000.00",
                    "payment_method": {
                        "id": "master",
                        "type": "credit_card",
                        "token": card_token_id,
                        "installments": 12
                    }
                }
            ]
        }

        print("Adding transaction for cancellation...")
        transaction_added = self.sdk.order().add_transaction(order_id, transaction_object)
        print("Transaction addition response:", transaction_added)

        transaction_id = transaction_added["response"]["id"]
        print("Transaction ID:", transaction_id)

        print("Cancelling transaction...")
        transaction_canceled = self.sdk.order().cancel_transaction(order_id, transaction_id)
        print("Transaction cancellation response:", transaction_canceled)

        self.assertEqual(transaction_canceled["status"], 200)
        self.assertEqual(transaction_canceled["response"]["status"], "canceled")


if __name__ == "__main__":
    unittest.main()