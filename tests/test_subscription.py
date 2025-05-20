"""
    Module: test_plan
"""
from datetime import datetime
import os
import unittest
import random
import mercadopago


class TestSubscription(unittest.TestCase):
    """
    Test Module: Preference
    """
    _customer_id = None
    _customer_email = None
    _plan_id = None
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    @classmethod
    def setUpClass(cls):
        customer_data = cls.create_customer()
        cls._customer_id = customer_data["response"]["id"]
        cls._customer_email = customer_data["response"]["email"]
        plan_data = cls.create_plan()
        if plan_data.get("status") != 201 or "id" not in plan_data.get("response", {}):
            raise RuntimeError(f"Failed to create plan: {plan_data}")
        cls._plan_id = plan_data["response"]["id"]

    @classmethod
    def tearDownClass(cls):
        cls.delete_customer()

    def test_all(self):
        """
        Test Module: Subscription
        """
        card_token = self.create_card_token()
        card_token_id = card_token['response']['id']

        random_reason_number = random.randint(100000, 999999)
        subscription_payload = {
            "back_url": "https://www.mercadopago.com.co/subscriptions",
            "reason": f"MercadoPago API Subscription #{random_reason_number}",
            "external_reference": "CustomIdentifier",
            "payer_email": self._customer_email,
            "preapproval_plan_id": self._plan_id,
            "card_token_id": card_token_id,
            "status": "authorized",
            "auto_recurring": {
                "frequency": 1,
                "frequency_type": "months",
                "transaction_amount": 60,
                "currency_id": "ARS"
            }
        }

        subscription_response = self.sdk.subscription().create(subscription_payload)
        self.assertEqual(subscription_response["status"], 201)

        subscription_object = subscription_response['response']
        self.assertIn('init_point', subscription_object)
        self.assertEqual(
            subscription_object["external_reference"], subscription_payload["external_reference"])
        self.assertEqual(subscription_object["status"], "authorized")

        update_payload = {
            "reason": f"MercadoPago API Subscription A #{random_reason_number}",
        }
        update_response = self.sdk.subscription().update(
            subscription_object["id"], update_payload)
        self.assertEqual(update_response["status"], 200)
        update_object = update_response["response"]
        self.assertEqual(update_object["reason"], update_payload["reason"])

        get_response = self.sdk.subscription().get(subscription_object["id"])
        self.assertEqual(get_response["status"], 200)
        get_object = get_response["response"]
        self.assertEqual(get_object["id"], subscription_object["id"])

        search_response = self.sdk.subscription().search()
        self.assertEqual(search_response["status"], 200)
        search_object = search_response["response"]
        self.assertTrue("results" in search_object)
        self.assertTrue(isinstance(search_object["results"], list))

    def test_create_subscriptions_without_a_plan(self):
        """
        Test Module: Subscription

        Test subscription creation without a plan
        """
        card_token = self.create_card_token()
        card_token_id = card_token['response']['id']

        random_reason_number = random.randint(100000, 999999)
        subscription_payload = {
            "back_url": "https://www.mercadopago.com.co/subscriptions",
            "reason": f"MercadoPago API Subscription B #{random_reason_number}",
            "external_reference": "CustomIdentifier",
            "payer_email": self._customer_email,
            "card_token_id": card_token_id,
            "auto_recurring": {
                "frequency": 1,
                "frequency_type": "months",
                "transaction_amount": 60,
                "currency_id": "ARS",
            },
            "status": "authorized"
        }

        subscription_response = self.sdk.subscription().create(subscription_payload)
        self.assertEqual(subscription_response["status"], 201)
        if subscription_response.get("status") != 201:
            raise RuntimeError(f"Failed to to create subscription: {subscription_response}")

        subscription_object = subscription_response['response']
        self.assertIn('init_point', subscription_object)
        self.assertEqual(
            subscription_object["external_reference"], subscription_payload["external_reference"])
        self.assertEqual(subscription_object["status"], "authorized")

    @classmethod
    def create_card_token(cls):
        card_token_object = {
            "card_number": "5031433215406351",
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
        return cls.sdk.card_token().create(card_token_object)

    @classmethod
    def create_customer(cls):
        random_email_id = random.randint(100000, 999999)
        customer_object = {
            "email": f"test_payer_{random_email_id}@testuser.com",
            "first_name": "Python",
            "last_name": "Mercado",
            "phone": {
                "area_code": "03492",
                "number": "432334"
            },
            "identification": {
                "type": "DNI",
                "number": "29804555"
            },
            "description": "customer description"
        }

        return cls.sdk.customer().create(customer_object)

    @classmethod
    def delete_customer(cls):
        cls.sdk.customer().delete(cls._customer_id)

    @classmethod
    def create_plan(cls):
        plan_object = {
            "auto_recurring": {
                "frequency": 1,
                "frequency_type": "months",
                "transaction_amount": 60,
                "currency_id": "BRL",
            },
            "back_url": "https://www.mercadopago.com.co/subscriptions",
            "reason": f"Test Plan #{random.randint(100000, 999999)}",
        }
        return cls.sdk.plan().create(plan_object)


if __name__ == "__main__":
    unittest.main()
