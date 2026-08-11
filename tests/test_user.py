"""Unit tests for the User resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestUser(BaseClientTest):
    """Test Module: User"""

    def test_get(self):
        fixture = self.load_fixture("user_get.json")
        self.mock_get(fixture)
        result = self.sdk.user().get()
        self.assertEqual(200, result["status"])
        self.assertEqual(12345, result["response"]["id"])
        self.assertEqual("test@example.com", result["response"]["email"])
        self.mock_http.get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
