"""
    Module: test_user
"""
import os
import unittest
import mercadopago


class TestUser(unittest.TestCase):
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_find_user(self):
        self.assertEqual(self.sdk.user().get()["status"], 200)


if __name__ == "__main__":
    unittest.main()
