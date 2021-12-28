"""
    Module: test_preference
"""
import unittest

import mercadopago


class TestPreference(unittest.TestCase):
    """
    Test Module: Preference
    """
    sdk = mercadopago.SDK(
        "APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_all(self):
        """
        Test Module: Preference
        """
        preference_object = {
            "items": [
                {
                    "description": "Test Update Success",
                    "id": "456",
                    "picture_url": "http://product1.image.png",
                    "quantity": 1,
                    "title": "Item 1",
                    "currency_id": "BRL",
                    "unit_price": 20.5
                }
            ]
        }
        preference_saved = self.sdk.preference().create(preference_object)
        self.assertEqual(preference_saved["status"], 201)

        preference_object["items"][0]["title"] = "Testando 1 2 3"

        preference_update = self.sdk.preference().update(
            preference_saved["response"]["id"], preference_object)
        self.assertEqual(preference_update["status"], 200)

        preference_saved = self.sdk.preference().get(
            preference_saved["response"]["id"])

        self.assertEqual(preference_saved["response"]["items"][0]["title"],
                         preference_object["items"][0]["title"])


if __name__ == "__main__":
    unittest.main()
