"""Unit tests for the PreApproval resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestPreApproval(BaseClientTest):
    """Test Module: PreApproval"""

    def test_get(self):
        fixture = self.load_fixture("preapproval_get.json")
        self.mock_get(fixture)
        result = self.sdk.preapproval().get("2c938084726fca480172750000000000")
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("2c938084726fca480172750000000000", resp["id"])
        self.assertEqual("authorized", resp["status"])
        self.assertEqual("Monthly subscription", resp["reason"])
        self.assertEqual("test_user@testuser.com", resp["payer_email"])
        self.assertEqual(123456789, resp["payer_id"])
        self.assertIn("auto_recurring", resp)
        self.assertEqual(1, resp["auto_recurring"]["frequency"])
        self.assertEqual("months", resp["auto_recurring"]["frequency_type"])
        self.assertEqual(29.90, resp["auto_recurring"]["transaction_amount"])
        self.assertEqual("BRL", resp["auto_recurring"]["currency_id"])
        self.assertIn("next_payment_date", resp)
        self.assertIn("init_point", resp)
        self.assertIn("date_created", resp)
        self.mock_http.get.assert_called_once()

    def test_create(self):
        fixture = self.load_fixture("preapproval_create.json")
        self.mock_post(fixture, status=201)
        preapproval_object = {
            "reason": "Monthly subscription",
            "auto_recurring": {"frequency": 1, "frequency_type": "months", "transaction_amount": 29.90, "currency_id": "BRL"},
            "payer_email": "test_user@testuser.com",
            "back_url": "https://example.com/back",
        }
        result = self.sdk.preapproval().create(preapproval_object)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual("2c938084726fca480172750000000000", resp["id"])
        self.assertEqual("pending", resp["status"])
        self.assertIn("auto_recurring", resp)
        self.assertIn("init_point", resp)
        self.assertEqual("test_user@testuser.com", resp["payer_email"])
        self.mock_http.post.assert_called_once()

    def test_update(self):
        fixture = self.load_fixture("preapproval_update.json")
        self.mock_put(fixture)
        result = self.sdk.preapproval().update("2c938084726fca480172750000000000", {"status": "cancelled"})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("2c938084726fca480172750000000000", resp["id"])
        self.assertEqual("cancelled", resp["status"])
        self.assertIn("last_modified", resp)
        self.mock_http.put.assert_called_once()

    def test_search(self):
        fixture = self.load_fixture("preapproval_search.json")
        self.mock_get(fixture)
        result = self.sdk.preapproval().search({"status": "authorized"})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIn("results", resp)
        self.assertIn("paging", resp)
        self.assertEqual(1, resp["paging"]["total"])
        self.assertEqual("2c938084726fca480172750000000000", resp["results"][0]["id"])
        self.assertEqual("authorized", resp["results"][0]["status"])
        self.mock_http.get.assert_called_once()

    def test_create_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.preapproval().create("not-a-dict")

    def test_update_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.preapproval().update("2c938084726fca480172750000000000", "not-a-dict")


if __name__ == "__main__":
    unittest.main()
