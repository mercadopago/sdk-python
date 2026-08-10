"""Unit tests for the Plan resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestPlan(BaseClientTest):
    """Test Module: Plan"""

    def test_get(self):
        fixture = self.load_fixture("plan_get.json")
        self.mock_get(fixture)
        result = self.sdk.plan().get("2c938084726fca480172750000000002")
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("2c938084726fca480172750000000002", resp["id"])
        self.assertEqual("active", resp["status"])
        self.assertEqual("Monthly Plan - Basic", resp["reason"])
        self.assertIn("auto_recurring", resp)
        self.assertEqual(1, resp["auto_recurring"]["frequency"])
        self.assertEqual("months", resp["auto_recurring"]["frequency_type"])
        self.assertEqual(29.90, resp["auto_recurring"]["transaction_amount"])
        self.assertEqual("BRL", resp["auto_recurring"]["currency_id"])
        self.assertIn("init_point", resp)
        self.assertIn("date_created", resp)
        self.assertIn("last_modified", resp)
        self.mock_http.get.assert_called_once()

    def test_create(self):
        fixture = self.load_fixture("plan_create.json")
        self.mock_post(fixture, status=201)
        plan_object = {
            "reason": "Monthly Plan - Basic",
            "auto_recurring": {
                "frequency": 1,
                "frequency_type": "months",
                "transaction_amount": 29.90,
                "currency_id": "BRL",
            },
            "back_url": "https://example.com/back",
        }
        result = self.sdk.plan().create(plan_object)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual("2c938084726fca480172750000000002", resp["id"])
        self.assertEqual("active", resp["status"])
        self.assertIn("auto_recurring", resp)
        self.assertIn("init_point", resp)
        self.mock_http.post.assert_called_once()

    def test_update(self):
        fixture = self.load_fixture("plan_update.json")
        self.mock_put(fixture)
        result = self.sdk.plan().update("2c938084726fca480172750000000002", {"status": "inactive"})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("2c938084726fca480172750000000002", resp["id"])
        self.assertEqual("inactive", resp["status"])
        self.assertIn("last_modified", resp)
        self.mock_http.put.assert_called_once()

    def test_search(self):
        fixture = self.load_fixture("plan_search.json")
        self.mock_get(fixture)
        result = self.sdk.plan().search()
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIn("results", resp)
        self.assertEqual("2c938084726fca480172750000000002", resp["results"][0]["id"])
        self.assertEqual("active", resp["results"][0]["status"])
        self.mock_http.get.assert_called_once()

    def test_create_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.plan().create("not-a-dict")

    def test_update_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.plan().update("2c938084726fca480172750000000002", "not-a-dict")


if __name__ == "__main__":
    unittest.main()
