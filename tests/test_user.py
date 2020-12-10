import sys
sys.path.append('../')

import unittest

import mercadopago

class TestUser(unittest.TestCase):
    sdk = mercadopago.SDK(access_token="APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

    def test_find_user(self):
        self.assertEqual(self.sdk.user().get()["status"], 200)

if __name__ == '__main__':
    unittest.main()
