"""
    Module: test_plan
"""
import os
import unittest
import random
import mercadopago


class TestPlan(unittest.TestCase):
    """
    Test Module: Preference
    """

    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_all(self):
        """
        Test Module: Plan
        """
        random_reason_number = random.randint(100000, 999999)
        plan_object_all_options_payload = {
            "auto_recurring": {
                "frequency": 1,
                "frequency_type": "months",
                "repetitions": 12,
                "billing_day": 5,
                "free_trial": {
                    "frequency": 2,
                    "frequency_type": "days"
                },
                "transaction_amount": 60,
                "currency_id": "BRL",
            },
            "back_url": "https://www.mercadopago.com.co/subscriptions",
            "reason": f"Test Plan #{random_reason_number}",
        }
        plan_object_mandatory_options_payload = {
            "auto_recurring": {
                "frequency": 1,
                "frequency_type": "months",
                "transaction_amount": 60,
                "currency_id": "BRL",
            },
            "back_url": "https://www.mercadopago.com.co/subscriptions",
            "reason": f"Test Plan (mandatory) #{random_reason_number}",
        }

        plan_response = self.sdk.plan().create(plan_object_all_options_payload)
        if plan_response.get("status") != 201:
            print(f"Plan creation failed: {plan_response}")
        self.assertEqual(plan_response["status"], 201)

        plan_object = plan_response["response"]
        self.assertEqual(plan_object["status"], "active")

        # Validate it works with minimal required options
        plan_mandatory_options = self.sdk.plan().create(
            plan_object_mandatory_options_payload)
        self.assertEqual(plan_mandatory_options["status"], 201)
        self.assertEqual(
            plan_mandatory_options["response"]["status"], "active")

        plan_object["reason"] = "MercadoPago API Test"
        update_response = self.sdk.plan().update(
            plan_object["id"], plan_object)
        self.assertEqual(update_response["status"], 200)
        update_object = update_response["response"]
        self.assertEqual(update_object["reason"], plan_object["reason"])
        self.assertEqual(update_object["status"], "active")

        get_response = self.sdk.plan().get(plan_object["id"])
        self.assertEqual(get_response["status"], 200)
        get_object = get_response["response"]
        self.assertEqual(get_object["id"], plan_object["id"])

        search_response = self.sdk.plan().search()
        self.assertEqual(search_response["status"], 200)
        search_object = search_response["response"]
        self.assertTrue("results" in search_object)
        self.assertTrue(isinstance(search_object["results"], list))


if __name__ == "__main__":
    unittest.main()
