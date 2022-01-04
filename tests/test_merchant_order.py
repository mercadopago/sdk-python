"""
    Module: test_merchant_order
"""
import unittest
import uuid

import mercadopago


class TestMerchantOrder(unittest.TestCase):
    """
    Test Module: Merchant Order
    """
    sdk = mercadopago.SDK(
        "APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_all(self):
        """
        Test Function: Merchant Order
        """
        preference_object = {
            "items": [
                {
                    "description": "Test Update Success",
                    "id": "5678",
                    "picture_url": "http://product1.image.png",
                    "quantity": 1,
                    "title": "Item 1",
                    "currency_id": "R$",
                    "unit_price": 20.5
                }
            ]
        }

        preference_saved = self.sdk.preference().create(preference_object)

        merchant_order_object = {
            "preference_id": preference_saved["response"]["id"],
            "site_id": "MLB",
            "notification_url": "https://seller/notification",
            "additional_info": "Aditional info",
            "external_reference": str(uuid.uuid4().int),
            "marketplace": "NONE",
            "items": [{
                "description": "Test Update Success",
                "id": "5678",
                "picture_url": "http://product1.image.png",
                "quantity": 1,
                "title": "Item 1",
                "currency_id": "BRL",
                "unit_price": 20.5
            }]
        }

        merchant_order_created = self.sdk.merchant_order().create(merchant_order_object)
        self.assertEqual(merchant_order_created["status"], 201)

        merchant_order_updated = self.sdk.merchant_order().update(
            merchant_order_created["response"]["id"], {"additional_info": "Info 2"})
        self.assertEqual(merchant_order_updated["status"], 200)

        merchant_order_finded = self.sdk.merchant_order().get(
            merchant_order_created["response"]["id"])
        self.assertEqual(merchant_order_finded["status"], 200)
        self.assertEqual(
            merchant_order_finded["response"]["additional_info"], "Info 2")


if __name__ == "__main__":
    unittest.main()
