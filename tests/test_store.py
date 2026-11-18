"""Unit tests for the Store resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestStore(BaseClientTest):
    """Test Module: Store"""

    def test_get(self):
        self.mock_get({"id": "store-001", "name": "Main Store"})
        result = self.sdk.store().get("store-001")
        self.assertEqual(200, result["status"])
        self.assertEqual("store-001", result["response"]["id"])
        self.mock_http.get.assert_called_once()

    def test_search(self):
        self.mock_get({"results": [{"id": "store-001"}], "paging": {"total": 1}})
        result = self.sdk.store().search(123, {"limit": 10})
        self.assertEqual(200, result["status"])
        self.assertEqual("store-001", result["response"]["results"][0]["id"])
        self.mock_http.get.assert_called_once()

    def test_update(self):
        self.mock_put({"id": "store-001", "name": "Updated"})
        result = self.sdk.store().update(123, "store-001", {"name": "Updated"})
        self.assertEqual(200, result["status"])
        self.assertEqual("Updated", result["response"]["name"])
        self.mock_http.put.assert_called_once()

    def test_delete(self):
        self.mock_delete({})
        result = self.sdk.store().delete(123, "store-001")
        self.assertEqual(204, result["status"])
        self.mock_http.delete.assert_called_once()

    def test_create(self):
        self.mock_post({"id": "store-001", "name": "New Store"}, status=201)
        result = self.sdk.store().create(123, {"name": "New Store"})
        self.assertEqual(201, result["status"])
        self.assertEqual("store-001", result["response"]["id"])
        self.mock_http.post.assert_called_once()
        self.assertEqual(
            "https://api.mercadopago.com/users/123/stores",
            self.mock_http.post.call_args.kwargs["url"],
        )

    def test_create_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.store().create(123, "not-a-dict")

    def test_update_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.store().update(123, "store-001", "not-a-dict")


if __name__ == "__main__":
    unittest.main()
