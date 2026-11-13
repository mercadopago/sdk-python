"""Unit tests for the Store resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestStore(BaseClientTest):
    """Test Module: Store"""

    def test_create(self):
        fixture = self.load_fixture("store_create.json")
        self.mock_post(fixture, status=201)
        store_object = {
            "name": "Sucursal Instore",
            "external_id": "STORE-001",
            "location": {
                "address_line": "Av Caseros 3039",
                "reference": "3er piso",
                "city": {"id": "TUxBQ0NBUGZlZG1zY3VA", "name": "Belgrano"},
                "latitude": -34.571148,
                "longitude": -58.459713,
                "zip_code": "1425",
            },
        }
        result = self.sdk.store().create(843382748, store_object)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual(1234567, resp["id"])
        self.assertEqual("Sucursal Instore", resp["name"])
        self.assertEqual("STORE-001", resp["external_id"])
        self.assertEqual(843382748, resp["user_id"])
        self.assertIn("location", resp)
        self.assertIn("date_created", resp)
        self.mock_http.post.assert_called_once()
        url = self.mock_http.post.call_args.kwargs["url"]
        self.assertEqual("https://api.mercadopago.com/users/843382748/stores", url)

    def test_get(self):
        fixture = self.load_fixture("store_get.json")
        self.mock_get(fixture)
        result = self.sdk.store().get(48091823)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual(1234567, resp["id"])
        self.assertEqual("Loja Teste", resp["name"])
        self.assertEqual("store-001", resp["external_id"])
        self.assertIn("location", resp)
        self.mock_http.get.assert_called_once()
        url = self.mock_http.get.call_args.kwargs["url"]
        self.assertEqual("https://api.mercadopago.com/stores/48091823", url)

    def test_search(self):
        fixture = self.load_fixture("store_search.json")
        self.mock_get(fixture)
        result = self.sdk.store().search(843382748, {"external_id": "store-001"})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIn("results", resp)
        self.assertEqual(1234567, resp["results"][0]["id"])
        self.assertEqual("Loja Teste", resp["results"][0]["name"])
        self.mock_http.get.assert_called_once()
        url = self.mock_http.get.call_args.kwargs["url"]
        self.assertEqual(
            "https://api.mercadopago.com/users/843382748/stores/search", url)

    def test_update(self):
        fixture = self.load_fixture("store_update.json")
        self.mock_put(fixture)
        result = self.sdk.store().update(
            843382748, 301, {"name": "Updated Store"})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual(1234567, resp["id"])
        self.assertEqual("Loja Teste", resp["name"])
        self.assertIn("date_last_updated", resp)
        self.mock_http.put.assert_called_once()
        url = self.mock_http.put.call_args.kwargs["url"]
        self.assertEqual(
            "https://api.mercadopago.com/users/843382748/stores/301", url)

    def test_delete(self):
        fixture = self.load_fixture("store_delete.json")
        self.mock_delete(fixture)
        result = self.sdk.store().delete(843382748, 3016406555)
        self.assertEqual(204, result["status"])
        resp = result["response"]
        self.assertEqual(1234567, resp["id"])
        self.mock_http.delete.assert_called_once()
        url = self.mock_http.delete.call_args.kwargs["url"]
        self.assertEqual(
            "https://api.mercadopago.com/users/843382748/stores/3016406555", url)

    def test_create_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.store().create(843382748, "not-a-dict")

    def test_update_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.store().update(843382748, 301, "not-a-dict")


if __name__ == "__main__":
    unittest.main()
