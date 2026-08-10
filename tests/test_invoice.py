"""Unit tests for the Invoice resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestInvoice(BaseClientTest):
    """Test Module: Invoice"""

    def test_get(self):
        fixture = self.load_fixture("invoice_get.json")
        self.mock_get(fixture)
        result = self.sdk.invoice().get("inv-001")
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("inv-001", resp["id"])
        self.assertEqual("processed", resp["status"])
        self.assertEqual(29.90, resp["transaction_amount"])
        self.assertEqual("BRL", resp["currency_id"])
        self.assertEqual("2c938084726fca480172750000000000", resp["preapproval_id"])
        self.assertIn("date_created", resp)
        self.mock_http.get.assert_called_once()

    def test_search(self):
        fixture = self.load_fixture("invoice_search.json")
        self.mock_get(fixture)
        result = self.sdk.invoice().search({"preapproval_id": "2c938084726fca480172750000000000"})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIn("results", resp)
        self.assertEqual("inv-001", resp["results"][0]["id"])
        self.assertEqual("processed", resp["results"][0]["status"])
        self.mock_http.get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
