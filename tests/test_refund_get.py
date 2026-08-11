"""Unit tests for the Refund resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestRefund(BaseClientTest):
    """Test Module: Refund"""

    def test_list_all(self):
        fixture = self.load_fixture("refund_list_all.json")
        self.mock_get(fixture)
        result = self.sdk.refund().list_all(17014025134)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIsInstance(resp, list)
        self.assertEqual(1091618291, resp[0]["id"])
        self.assertEqual(17014025134, resp[0]["payment_id"])
        self.assertEqual(58.80, resp[0]["amount"])
        self.assertEqual("approved", resp[0]["status"])
        self.mock_http.get.assert_called_once()

    def test_get(self):
        fixture = self.load_fixture("refund_get.json")
        self.mock_get(fixture)
        result = self.sdk.refund().get(17014025134, 1091618291)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual(1091618291, resp["id"])
        self.assertEqual(17014025134, resp["payment_id"])
        self.assertEqual(58.80, resp["amount"])
        self.assertEqual("approved", resp["status"])
        self.assertEqual("standard", resp["refund_mode"])
        self.assertIn("date_created", resp)
        self.assertIn("source", resp)
        self.assertEqual("Test User", resp["source"]["name"])
        self.assertEqual("operator", resp["source"]["type"])
        self.mock_http.get.assert_called_once()

    def test_create_full_refund(self):
        fixture = self.load_fixture("refund_create.json")
        self.mock_post(fixture, status=201)
        result = self.sdk.refund().create(17014025134)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual(1091618291, resp["id"])
        self.assertEqual(17014025134, resp["payment_id"])
        self.assertEqual(58.80, resp["amount"])
        self.assertEqual("approved", resp["status"])
        self.assertEqual("standard", resp["refund_mode"])
        self.mock_http.post.assert_called_once()

    def test_create_partial_refund(self):
        fixture = self.load_fixture("refund_create.json")
        self.mock_post(fixture, status=201)
        result = self.sdk.refund().create(17014025134, {"amount": 50.0})
        self.assertEqual(201, result["status"])
        self.assertIn("date_created", result["response"])
        self.mock_http.post.assert_called_once()

    def test_create_raises_for_non_dict_refund_object(self):
        with self.assertRaises(ValueError):
            self.sdk.refund().create(17014025134, "not-a-dict")


if __name__ == "__main__":
    unittest.main()
