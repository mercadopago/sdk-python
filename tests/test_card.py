"""Unit tests for the Card resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestCard(BaseClientTest):
    """Test Module: Card"""

    def test_list_all(self):
        fixture = self.load_fixture("card_list_all.json")
        self.mock_get(fixture)
        result = self.sdk.card().list_all("1068193981-pXRewrKqlP6pnn")
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIsInstance(resp, list)
        self.assertEqual("1562188766852", resp[0]["id"])
        self.assertEqual("503143", resp[0]["first_six_digits"])
        self.assertEqual("6351", resp[0]["last_four_digits"])
        self.assertIn("payment_method", resp[0])
        self.mock_http.get.assert_called_once()

    def test_get(self):
        fixture = self.load_fixture("card_get.json")
        self.mock_get(fixture)
        result = self.sdk.card().get("1068193981-pXRewrKqlP6pnn", "1562188766852")
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("1562188766852", resp["id"])
        self.assertEqual("1068193981-pXRewrKqlP6pnn", resp["customer_id"])
        self.assertEqual("503143", resp["first_six_digits"])
        self.assertEqual("6351", resp["last_four_digits"])
        self.assertEqual(11, resp["expiration_month"])
        self.assertEqual(2030, resp["expiration_year"])
        self.assertIn("cardholder", resp)
        self.assertEqual("APRO", resp["cardholder"]["name"])
        self.assertIn("payment_method", resp)
        self.assertEqual("master", resp["payment_method"]["id"])
        self.assertEqual("credit_card", resp["payment_method"]["payment_type_id"])
        self.assertIn("issuer", resp)
        self.assertIn("security_code", resp)
        self.assertIn("date_created", resp)
        self.assertIn("date_last_updated", resp)
        self.mock_http.get.assert_called_once()

    def test_create(self):
        fixture = self.load_fixture("card_create.json")
        self.mock_post(fixture, status=201)
        card_object = {"token": "token-001"}
        result = self.sdk.card().create("1068193981-pXRewrKqlP6pnn", card_object)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual("1562188766852", resp["id"])
        self.assertEqual("503143", resp["first_six_digits"])
        self.assertEqual("6351", resp["last_four_digits"])
        self.assertEqual(2030, resp["expiration_year"])
        self.assertIn("cardholder", resp)
        self.assertIn("payment_method", resp)
        self.assertIn("issuer", resp)
        self.mock_http.post.assert_called_once()

    def test_update(self):
        fixture = self.load_fixture("card_update.json")
        self.mock_put(fixture)
        result = self.sdk.card().update(
            "1068193981-pXRewrKqlP6pnn", "1562188766852", {"expiration_year": 2030})
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("1562188766852", resp["id"])
        self.assertEqual(2030, resp["expiration_year"])
        self.assertIn("date_last_updated", resp)
        self.mock_http.put.assert_called_once()

    def test_delete(self):
        self.mock_delete({"id": "1562188766852"}, status=200)
        result = self.sdk.card().delete("1068193981-pXRewrKqlP6pnn", "1562188766852")
        self.assertEqual(200, result["status"])
        self.mock_http.delete.assert_called_once()

    def test_create_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.card().create("1068193981-pXRewrKqlP6pnn", "not-a-dict")

    def test_update_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.card().update("1068193981-pXRewrKqlP6pnn", "1562188766852", "not-a-dict")


if __name__ == "__main__":
    unittest.main()
