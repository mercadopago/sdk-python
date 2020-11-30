import sys
sys.path.append('../')

import unittest

import mercadopago
from mercadopago.config import RequestOptions

class TestCard(unittest.TestCase):
    sdk = mercadopago.SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_find_all(self):
        self.assertEqual(self.sdk.card().find_all("67243")["status"], 404)
        self.assertEqual(self.sdk.card().find_all("67243", request_options=RequestOptions(access_token=""))["status"], 401)

if __name__ == '__main__':
    unittest.main()
