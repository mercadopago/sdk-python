"""
    Module: test_customer
"""
import unittest

import mercadopago


class TestCustomer(unittest.TestCase):
    """
    Test Module: Customer
    """
    sdk = mercadopago.SDK(
        "APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_all(self):
        """
        Test Function: Customer
        """
        customer_object = {
            "email": "test_payer_999945@testuser.com",
            "first_name": "Katniss",
            "last_name": "Everdeen",
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

        customer_saved = self.sdk.customer().create(customer_object)
        self.assertEqual(customer_saved["status"], 201)

        customer_update = self.sdk.customer().update(
            customer_saved["response"]["id"], {"last_name": "Payer"})
        self.assertEqual(customer_update["status"], 200)

        customer_updated = self.sdk.customer().get(
            customer_saved["response"]["id"])
        self.assertEqual(customer_updated["response"]["last_name"], "Payer")

        customer_deleted = self.sdk.customer().delete(
            customer_saved["response"]["id"])
        self.assertEqual(customer_deleted["status"], 200)


if __name__ == "__main__":
    unittest.main()
