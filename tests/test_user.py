import sys
sys.path.append('../')

import unittest

import mercadopago
from mercadopago.config import RequestOptions

#TODO VERIFICAR SE ESSE TESTE É NECESSÁRIO
class TestUser(unittest.TestCase):
    sdk = mercadopago.SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_find_user(self):
        request_options = {
            "items": [
                {
                    "user": "1234"
                }
            ]
        }
        
        self.assertEqual(self.sdk.user().get(["response"])["status"], 200)
