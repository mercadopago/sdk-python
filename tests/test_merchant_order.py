"""Unit tests for the MerchantOrder resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestMerchantOrder(BaseClientTest):
    """Test Module: MerchantOrder"""

    def test_get(self):
        fixture = self.load_fixture("merchant_order_get.json")
        self.mock_get(fixture)
        result = self.sdk.merchant_order().get(4049696864)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual(4049696864, resp["id"])
        self.assertEqual("opened", resp["status"])
        self.assertEqual("ext-ref-001", resp["external_reference"])
        self.assertEqual("843382748-18d90a57-a4ce-4718", resp["preference_id"])
        self.assertIsInstance(resp["payments"], list)
        self.assertIsInstance(resp["items"], list)
        self.assertEqual("Point Mini", resp["items"][0]["title"])
        self.assertEqual(58.80, resp["total_amount"])
        self.assertEqual(0.0, resp["paid_amount"])
        self.assertIn("date_created", resp)
        self.assertIn("notification_url", resp)
        self.mock_http.get.assert_called_once()

    def test_create(self):
        fixture = self.load_fixture("merchant_order_create.json")
        self.mock_post(fixture, status=201)
        merchant_order_object = {
            "preference_id": "843382748-18d90a57-a4ce-4718",
            "site_id": "MLB",
        }
        result = self.sdk.merchant_order().create(merchant_order_object)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual(4049696864, resp["id"])
        self.assertEqual("opened", resp["status"])
        self.assertEqual(58.80, resp["total_amount"])
        self.assertIsInstance(resp["items"], list)
        self.assertIn("date_created", resp)
        self.mock_http.post.assert_called_once()

    def test_update(self):
        fixture = self.load_fixture("merchant_order_update.json")
        self.mock_put(fixture)
        result = self.sdk.merchant_order().update(4049696864, {"external_reference": "ext-updated"})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual(4049696864, resp["id"])
        self.assertEqual("ext-updated", resp["external_reference"])
        self.assertIn("last_updated", resp)
        self.mock_http.put.assert_called_once()

    def test_search(self):
        fixture = self.load_fixture("merchant_order_search.json")
        self.mock_get(fixture)
        result = self.sdk.merchant_order().search({"preference_id": "843382748-18d90a57-a4ce-4718"})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIn("elements", resp)
        self.assertEqual(4049696864, resp["elements"][0]["id"])
        self.mock_http.get.assert_called_once()

    def test_create_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.merchant_order().create("not-a-dict")

    def test_update_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.merchant_order().update(4049696864, "not-a-dict")


if __name__ == "__main__":
    unittest.main()
