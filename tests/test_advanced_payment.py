"""Unit tests for the AdvancedPayment resource using a mock HTTP client."""
import unittest
from datetime import datetime

from tests.base_client_test import BaseClientTest


class TestAdvancedPayment(BaseClientTest):
    """Test Module: AdvancedPayment"""

    def test_get(self):
        fixture = self.load_fixture("advanced_payment_get.json")
        self.mock_get(fixture)
        result = self.sdk.advanced_payment().get(999)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual(999, resp["id"])
        self.assertEqual("approved", resp["status"])
        self.assertEqual("accredited", resp["status_detail"])
        self.assertEqual("test_user@testuser.com", resp["payer"]["email"])
        self.assertIsInstance(resp["payments"], list)
        self.assertEqual(1001, resp["payments"][0]["id"])
        self.assertEqual("approved", resp["payments"][0]["status"])
        self.assertIsInstance(resp["disbursements"], list)
        self.assertIn("date_created", resp)
        self.mock_http.get.assert_called_once()

    def test_create(self):
        fixture = self.load_fixture("advanced_payment_create.json")
        self.mock_post(fixture, status=201)
        advanced_payment_object = {
            "application_id": "app-001",
            "payments": [{"payment_method_id": "visa", "token": "token-001", "transaction_amount": 100.0, "installments": 1}],
            "disbursements": [{"collector_id": 843382748, "amount": 100.0, "external_reference": "ref-001"}],
            "payer": {"email": "test_user@testuser.com"},
        }
        result = self.sdk.advanced_payment().create(advanced_payment_object)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual(999, resp["id"])
        self.assertEqual("pending", resp["status"])
        self.assertIsInstance(resp["payments"], list)
        self.assertIsInstance(resp["disbursements"], list)
        self.mock_http.post.assert_called_once()

    def test_search(self):
        fixture = self.load_fixture("advanced_payment_search.json")
        self.mock_get(fixture)
        result = self.sdk.advanced_payment().search({"status": "approved"})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIn("results", resp)
        self.assertIn("paging", resp)
        self.assertEqual(999, resp["results"][0]["id"])
        self.assertEqual("approved", resp["results"][0]["status"])
        self.mock_http.get.assert_called_once()

    def test_update(self):
        fixture = self.load_fixture("advanced_payment_update.json")
        self.mock_put(fixture)
        result = self.sdk.advanced_payment().update(999, {"status": "approved"})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual(999, resp["id"])
        self.assertEqual("approved", resp["status"])
        self.mock_http.put.assert_called_once()

    def test_capture(self):
        fixture = self.load_fixture("advanced_payment_update.json")
        self.mock_put(fixture)
        result = self.sdk.advanced_payment().capture(999)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual(999, resp["id"])
        self.assertEqual("approved", resp["status"])
        self.mock_http.put.assert_called_once()

    def test_cancel(self):
        self.mock_put({"id": 999, "status": "cancelled"})
        result = self.sdk.advanced_payment().cancel(999)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual(999, resp["id"])
        self.assertEqual("cancelled", resp["status"])
        self.mock_http.put.assert_called_once()

    def test_update_release_date(self):
        self.mock_post({"id": 999, "money_release_date": "2026-09-01 00:00:00.000000"}, status=201)
        release_date = datetime(2026, 9, 1)
        result = self.sdk.advanced_payment().update_release_date(999, release_date)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual(999, resp["id"])
        self.assertIn("money_release_date", resp)
        self.mock_http.post.assert_called_once()

    def test_update_release_date_raises_for_non_datetime(self):
        with self.assertRaises(ValueError):
            self.sdk.advanced_payment().update_release_date(999, "2026-09-01")

    def test_create_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.advanced_payment().create("not-a-dict")

    def test_update_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.advanced_payment().update(999, "not-a-dict")


if __name__ == "__main__":
    unittest.main()
