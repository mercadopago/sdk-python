"""Unit tests for the Store resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestStore(BaseClientTest):
    """Test Module: Store"""

    def test_create(self):
        fixture = self.load_fixture("store_create.json")
        self.mock_post(fixture, status=201)
        store_object = {"name": "Official Store", "location": {"address_line": "Av Paulista 1000"}}
        result = self.sdk.store().create(123456789, store_object)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual(123456789, resp["id"])
        self.assertEqual("Official Store", resp["name"])
        self.mock_http.post.assert_called_once()
        _, kwargs = self.mock_http.post.call_args
        self.assertEqual("https://api.mercadopago.com/users/123456789/stores", kwargs["url"])

    def test_get(self):
        fixture = self.load_fixture("store_get.json")
        self.mock_get(fixture)
        result = self.sdk.store().get(123456789)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual(123456789, resp["id"])
        self.assertEqual("Official Store", resp["name"])
        self.mock_http.get.assert_called_once()
        _, kwargs = self.mock_http.get.call_args
        self.assertEqual("https://api.mercadopago.com/stores/123456789", kwargs["url"])

    def test_search(self):
        fixture = self.load_fixture("store_search.json")
        self.mock_get(fixture)
        result = self.sdk.store().search(123456789)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIn("results", resp)
        self.assertEqual(123456789, resp["results"][0]["id"])
        self.mock_http.get.assert_called_once()
        _, kwargs = self.mock_http.get.call_args
        self.assertEqual("https://api.mercadopago.com/users/123456789/stores/search", kwargs["url"])

    def test_update(self):
        fixture = self.load_fixture("store_update.json")
        self.mock_put(fixture)
        result = self.sdk.store().update(123456789, 987654321, {"name": "Updated Store"})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual(987654321, resp["id"])
        self.assertEqual("Updated Store", resp["name"])
        self.mock_http.put.assert_called_once()
        _, kwargs = self.mock_http.put.call_args
        self.assertEqual("https://api.mercadopago.com/users/123456789/stores/987654321", kwargs["url"])

    def test_delete(self):
        fixture = self.load_fixture("store_delete.json")
        self.mock_delete(fixture)
        result = self.sdk.store().delete(123456789, 987654321)
        self.assertEqual(200, result["status"])
        self.mock_http.delete.assert_called_once()
        _, kwargs = self.mock_http.delete.call_args
        self.assertEqual("https://api.mercadopago.com/users/123456789/stores/987654321", kwargs["url"])


if __name__ == "__main__":
    unittest.main()
