import sys
sys.path.append('../')

import unittest

import mercadopago
from mercadopago.config.request_options import RequestOptions

class TestUser(unittest.TestCase):
    sdk = mercadopago.SDK(access_token="APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")
    #sdk.access_token="abc"
    sdk.corporation_id="MEU_CORP_ID"

    def test_find_user(self):
        self.assertEqual(self.sdk.user().get()["status"], 200)

if __name__ == '__main__':
    unittest.main()
