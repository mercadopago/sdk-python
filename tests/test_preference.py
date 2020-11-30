import sys
sys.path.append('../')

import unittest

import mercadopago
from mercadopago.config import RequestOptions

class TestPreference(unittest.TestCase):
    sdk = mercadopago.SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_save_and_find(self):
        preference_object = {
            "items": [
                {
                    "title": "Test",
                    "quantity": 1,
                    "currency_id": "R$",
                    "unit_price": 10.4
                }
            ]
        }
        preference_saved = self.sdk.preference().save(preference_object)
        self.assertEqual(preference_saved["status"], 201)
        self.assertEqual(self.sdk.preference().find_by_id(preference_saved["response"]["id"])["status"], 200)

if __name__ == '__main__':
    unittest.main()
