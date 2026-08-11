"""Unit tests for the Point resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestPoint(BaseClientTest):
    """Test Module: Point"""

    def test_get_devices(self):
        fixture = self.load_fixture("point_get_devices.json")
        self.mock_get(fixture)
        result = self.sdk.point().get_devices()
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIn("devices", resp)
        self.assertIsInstance(resp["devices"], list)
        self.assertEqual("device-001", resp["devices"][0]["id"])
        self.assertEqual("PDV", resp["devices"][0]["operating_mode"])
        self.assertEqual("store-001", resp["devices"][0]["store_id"])
        self.mock_http.get.assert_called_once()

    def test_get_devices_with_filters(self):
        fixture = self.load_fixture("point_get_devices.json")
        self.mock_get(fixture)
        result = self.sdk.point().get_devices(filters={"store_id": "store-001"})
        self.assertEqual(200, result["status"])
        self.assertIn("devices", result["response"])
        self.mock_http.get.assert_called_once()

    def test_create(self):
        fixture = self.load_fixture("point_create.json")
        self.mock_post(fixture, status=201)
        payment_intent_object = {
            "amount": 58.80,
            "additional_info": {"external_reference": "ref-001"},
            "description": "Test payment",
            "payment": {"installments": 1, "type": "credit_card"},
        }
        result = self.sdk.point().create("device-001", payment_intent_object)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual("intent-001", resp["id"])
        self.assertEqual("OPEN", resp["state"])
        self.assertEqual("device-001", resp["device_id"])
        self.assertEqual(58.80, resp["amount"])
        self.mock_http.post.assert_called_once()

    def test_get(self):
        fixture = self.load_fixture("point_get.json")
        self.mock_get(fixture)
        result = self.sdk.point().get("intent-001")
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("intent-001", resp["id"])
        self.assertEqual("FINISHED", resp["state"])
        self.assertEqual("device-001", resp["device_id"])
        self.assertEqual(58.80, resp["amount"])
        self.mock_http.get.assert_called_once()

    def test_cancel(self):
        self.mock_delete({"id": "intent-001"}, status=200)
        result = self.sdk.point().cancel("device-001", "intent-001")
        self.assertEqual(200, result["status"])
        self.mock_http.delete.assert_called_once()

    def test_create_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.point().create("device-001", "not-a-dict")


if __name__ == "__main__":
    unittest.main()
