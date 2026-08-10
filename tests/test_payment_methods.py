"""Unit tests for the PaymentMethods resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestPaymentMethods(BaseClientTest):
    """Test Module: PaymentMethods"""

    def test_list_all(self):
        fixture = self.load_fixture("payment_methods_list_all.json")
        self.mock_get(fixture)
        result = self.sdk.payment_methods().list_all()
        self.assertEqual(200, result["status"])
        self.assertIsInstance(result["response"], list)
        self.assertGreater(len(result["response"]), 0)
        # Ensure at least one method has expected fields
        first = result["response"][0]
        self.assertIn("id", first)
        self.assertIn("name", first)
        self.mock_http.get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
