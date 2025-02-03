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

    def test_create_order_and_get_by_id(self):
        """
        Test Function: Order
        """
        card_token_object = {
            "card_number": "5031433215406351",
            "security_code": "123",
            "expiration_year": "2055",
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

        order_get =  self.sdk.order().get(
            order_created["response"]["id"])
        self.assertEqual(order_get["status"], 200)

if __name__ == "__main__":
    unittest.main()


class TestOrderProcess(unittest.TestCase):
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_process_order(self):
        card_token_object = {
            "card_number": "5031433215406351",
            "security_code": "123",
            "expiration_year": "2055",
            "expiration_month": "11",
            "cardholder": {
                "name": "APRO"
            }
        }
        card_token_created = self.sdk.card_token().create(card_token_object)
        if card_token_created.get("status") != 201 or not card_token_created.get("response"):
            self.fail(f"Falha ao criar card token: {card_token_created}")

        card_token_id = card_token_created["response"]["id"]
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
        if order_created.get("status") != 201 or not order_created.get("response"):
            self.fail(f"Falha ao criar pedido: {order_created}")

        order_id = order_created["response"]["id"]
        print("Pedido criado com ID:", order_id)

        process_response = self.sdk.order().process(order_id)
        if process_response.get("status") != 200 or not process_response.get("response"):
            self.fail(f"Falha ao processar pedido: {process_response}")

        self.assertEqual(process_response["status"], 200, "Status HTTP inválido ao processar o pedido")
        print("Pedido processado com sucesso.")

    if __name__ == "__main__":
        unittest.main()
