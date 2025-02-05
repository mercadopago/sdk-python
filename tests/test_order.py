"""
    Module: test_order
"""
import json
import os
import unittest
import random
import mercadopago


class TestOrder(unittest.TestCase):
    """
    Test Module: Order
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def create_test_card(self, status="APRO"):
        card_token_object = {
            "card_number": "5031433215406351",
            "security_code": "123",
            "expiration_year": "2030",
            "expiration_month": "11",
            "cardholder": {"name": status}
        }
        card_token_created = self.sdk.card_token().create(card_token_object)
        return card_token_created["response"]["id"]

    """teste ok"""
    def test_create_order_and_get_by_id(self):
        """
        Test Function: Create an Order and Get an Order by ID
        """
        card_token_id = self.create_test_card()
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
                    "token": card_token_id,
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

        order_get =  self.sdk.order().get(order_created["response"]["id"])
        self.assertEqual(order_get["status"], 200)

    """teste ok"""
    def test_process_order(self):
        card_token_id = self.create_test_card()
        random_email_id = random.randint(100000, 999999)
        order_object = {
            "type": "online",
            "processing_mode": "manual",
            "external_reference": "ext_ref_1234",
            "total_amount": "200.00",
            "transactions": {
                "payments": [
                    {
                        "amount": "200.00",
                        "payment_method": {
                            "id": "master",
                            "type": "credit_card",
                            "token": card_token_id,
                            "installments": 1
                        }
                    }
                ]
            },
            "payer": {
                "email": f"test_payer_{random_email_id}@testuser.com"
            }
        }

        order_created = self.sdk.order().create(order_object)
        order_id = order_created["response"]["id"]
        process_response = self.sdk.order().process(order_id)
        if process_response.get("status") != 200 or not process_response.get("response"):
            self.fail(f"Failed to create an order: {process_response}")
        self.assertEqual(process_response["status"], 200, "Status HTTP inválido ao processar o pedido")
        print("Order processed successfully.")

    def create_order_canceled_or_captured(self, card_token_id):
        random_email_id = random.randint(100000, 999999)
        order_object_cc = {
            "type": "online",
            "processing_mode": "automatic",
            "total_amount": "200.00",
            "external_reference": "ext_ref_1234",
            "payer": {
                "email": f"test_payer_{random_email_id}@testuser.com"
            },
            "capture_mode": "manual",
            "transactions": {
                "payments": [
                    {
                        "amount": "200.00",
                        "payment_method": {
                            "id": "master",
                            "type": "credit_card",
                            "token": card_token_id,
                            "installments": 1
                        }
                    }
                ]
            }
        }
        order_created = self.sdk.order().create(order_object_cc)
        if order_created.get("status") != 201 or not order_created.get("response"):
            self.fail(f"Failed to create order: {order_created}")
        return order_created["response"]["id"]

    """teste ok"""
    def test_cancel_order(self):
        card_token_id = self.create_test_card()
        order_id = self.create_order_canceled_or_captured(card_token_id)
        order_canceled = self.sdk.order().cancel(order_id)
        self.assertEqual(order_canceled["status"], 200)
        self.assertEqual(order_canceled["response"]["status"], "canceled")

    """teste ok"""
    def test_capture_order(self):
        card_token_id = self.create_test_card()
        order_id = self.create_order_canceled_or_captured(card_token_id)
        order_captured = self.sdk.order().capture(order_id)
        self.assertEqual(order_captured["status"], 200)
        self.assertEqual(order_captured["response"]["status"], "processed")

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

    """teste ok"""
    def test_add_transaction(self):
        card_token_id = self.create_test_card()
        print("Card token ID:", card_token_id)

        order_id = self.create_order_builder_mode(card_token_id)
        print("Order ID:", order_id)

        transaction_object = {
            "payments": [
                {
                    "amount": "200.00",
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
        transaction_added = self.sdk.order().create_transaction(order_id, transaction_object)
        print("Transaction addition response:", transaction_added)

        self.assertEqual(transaction_added["status"], 201)

    def create_order_builder_mode_complete(self, card_token_id):
        random_email_id = random.randint(100000, 999999)
        order_mode_builder_complete = {
            "type": "online",
            "processing_mode": "manual",
            "total_amount": "200.00",
            "external_reference": "ext_ref_1234",
            "transactions": {
                "payments": [
                    {
                        "amount": "200.00",
                        "payment_method": {
                            "id": "master",
                            "type": "credit_card",
                            "token": card_token_id,
                            "installments": 12
                        }
                    }
                ]
            },
            "payer": {
                "email": f"test_payer_{random_email_id}@testuser.com"
            }
        }

        order_created = self.sdk.order().create(order_mode_builder_complete)


        if order_created.get("status") != 201 or not order_created.get("response"):
            self.fail(f"Failed to create order: {order_created}")
        return order_created["response"]

    def test_update_transaction(self):
        card_token_id = self.create_test_card()
        order_created = self.create_order_builder_mode_complete(card_token_id)
        order_id = order_created["id"]
        print("orderID :", order_id)
        transaction_id = order_created["transactions"]["payments"][0]["id"]
        print("transactionID :" ,transaction_id)


        transaction_update = {
            "payment_method": {
                "type": "credit_card",
                "installments": 5
            }
        }

        transaction_updated = self.sdk.order().update_transaction(order_id, transaction_id, transaction_update)
        self.assertEqual(transaction_updated["status"], 200)


if __name__ == "__main__":
    unittest.main()