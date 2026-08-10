"""Unit tests for the IdentificationType resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestIdentificationType(BaseClientTest):
    """Test Module: IdentificationType"""

    def test_list_all(self):
        fixture = self.load_fixture("identification_type_list_all.json")
        self.mock_get(fixture)
        result = self.sdk.identification_type().list_all()
        self.assertEqual(200, result["status"])
        self.assertIsInstance(result["response"], list)
        self.assertGreater(len(result["response"]), 0)
        self.mock_http.get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
