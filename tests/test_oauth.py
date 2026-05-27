"""
    Module: test_oauth
"""
import os
import unittest
import mercadopago


class TestOAuth(unittest.TestCase):
    """
    Test Module: OAuth
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_get_authorization_url(self):
        """
        Test Function: OAuth get_authorization_url builds correct URL
        """
        url = self.sdk.oauth().get_authorization_url(
            app_id="TEST_APP_ID",
            redirect_uri="https://example.com/callback",
            random_id="csrf_state_token",
        )
        self.assertIn("https://auth.mercadopago.com/authorization", url)
        self.assertIn("client_id=TEST_APP_ID", url)
        self.assertIn("response_type=code", url)
        self.assertIn("redirect_uri=", url)
        self.assertIn("state=csrf_state_token", url)
        self.assertIn("platform_id=mp", url)

    def test_create_raises_on_invalid_param(self):
        """
        Test Function: OAuth create raises ValueError for non-dict input
        """
        with self.assertRaises(ValueError):
            self.sdk.oauth().create("not_a_dict")

    def test_refresh_raises_on_invalid_param(self):
        """
        Test Function: OAuth refresh raises ValueError for non-dict input
        """
        with self.assertRaises(ValueError):
            self.sdk.oauth().refresh("not_a_dict")


if __name__ == "__main__":
    unittest.main()
