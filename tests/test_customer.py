import sys
sys.path.append('../')

import unittest

import mercadopago
from mercadopago.config import RequestOptions

class TestCustomer(unittest.TestCase):
    sdk = mercadopago.SDK(
        "APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_search_customer(self):
        customer_object = {
            "items": [
                {
                    "id": "1234",
                    "limit": 1,
                    "offset": 0,
                    "filters": {
                        "email": "test_customer@email.com"
                    }
                }
            ]
        }
        customer_saved = self.sdk.customer().create(customer_object)
        self.assertEqual(customer_saved["status"], 201)

        customer_object["items"][0]["limit"] = "3"
        print(customer_saved["response"]["items"][0]["limit"], "3")

        customer_update = self.sdk.customer().update(customer_saved["response"]["id"], customer_object)
        self.assertEqual(customer_update["status"], 200)

        customer_saved = self.sdk.customer().get(customer_saved["response"]["id"])

        #self.assertEqual(self.sdk.customer().search(customer_saved["response"]["id"])["status"], 200)
