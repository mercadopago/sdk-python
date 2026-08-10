"""Unit tests for the Preference resource using a mock HTTP client."""
import unittest
import warnings

from tests.base_client_test import BaseClientTest


class TestPreference(BaseClientTest):
    """Test Module: Preference"""

    def test_create(self):
        fixture = self.load_fixture("preference_create.json")
        self.mock_post(fixture, status=201)
        preference_object = {
            "items": [{"title": "Point Mini", "quantity": 1, "unit_price": 58.80}]
        }
        result = self.sdk.preference().create(preference_object)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual("843382748-18d90a57-a4ce-4718-bc17-1234567890", resp["id"])
        self.assertIn("init_point", resp)
        self.assertIsInstance(resp["items"], list)
        self.assertEqual("Point Mini", resp["items"][0]["title"])
        self.assertEqual(843382748, resp["collector_id"])
        self.assertIn("back_urls", resp)
        self.assertIn("payment_methods", resp)
        self.assertEqual(12, resp["payment_methods"]["installments"])
        self.mock_http.post.assert_called_once()

    def test_create_with_notification_url_warns(self):
        fixture = self.load_fixture("preference_create.json")
        self.mock_post(fixture, status=201)
        preference_object = {
            "items": [{"title": "Point Mini", "quantity": 1, "unit_price": 58.80}],
            "notification_url": "https://example.com/notify",
        }
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            self.sdk.preference().create(preference_object)
        self.assertTrue(any(issubclass(w.category, DeprecationWarning) for w in caught))

    def test_get(self):
        fixture = self.load_fixture("preference_get.json")
        self.mock_get(fixture)
        result = self.sdk.preference().get("843382748-18d90a57-a4ce-4718-bc17-1234567890")
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("843382748-18d90a57-a4ce-4718-bc17-1234567890", resp["id"])
        self.assertIn("init_point", resp)
        self.assertIsInstance(resp["items"], list)
        self.assertEqual("Point Mini", resp["items"][0]["title"])
        self.assertEqual(58.80, resp["items"][0]["unit_price"])
        self.assertEqual(843382748, resp["collector_id"])
        self.assertIn("back_urls", resp)
        self.assertEqual("https://example.com/success", resp["back_urls"]["success"])
        self.assertEqual("MP-PREF-001", resp["external_reference"])
        self.assertIn("date_created", resp)
        self.mock_http.get.assert_called_once()

    def test_update(self):
        fixture = self.load_fixture("preference_update.json")
        self.mock_put(fixture)
        result = self.sdk.preference().update(
            "843382748-18d90a57-a4ce-4718-bc17-1234567890",
            {"items": [{"title": "Updated Item"}]},
        )
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("843382748-18d90a57-a4ce-4718-bc17-1234567890", resp["id"])
        self.assertIn("items", resp)
        self.mock_http.put.assert_called_once()

    def test_search(self):
        fixture = self.load_fixture("preference_search.json")
        self.mock_get(fixture)
        result = self.sdk.preference().search()
        self.assertEqual(200, result["status"])
        self.mock_http.get.assert_called_once()

    def test_create_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.preference().create("not-a-dict")

    def test_update_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.preference().update("843382748-18d90a57-a4ce-4718-bc17-1234567890", "not-a-dict")


if __name__ == "__main__":
    unittest.main()
