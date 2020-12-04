import sys
sys.path.append("../")

import unittest

import mercadopago
from mercadopago.config import RequestOptions

class TestIdentificationType(unittest.TestCase):
    sdk = mercadopago.SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_find_all(self):
        request_options = {
            "items": [
                {
                    "identification_types": ""
                }
            ]
        }
    
        identy = self.sdk.identification_type().get_list(request_options["response"]["identification_types"])

        self.assertEqual(identy["status", 200])
