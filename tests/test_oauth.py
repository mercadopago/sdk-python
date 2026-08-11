"""Unit tests for the OAuth resource using a mock HTTP client."""
import unittest
from urllib.parse import (
    parse_qs,
    urlparse,
)

from tests.base_client_test import BaseClientTest


class TestOAuth(BaseClientTest):
    """Test Module: OAuth"""

    def test_get_authorization_url(self):
        url = self.sdk.oauth().get_authorization_url(
            app_id="my-app-id",
            redirect_uri="https://example.com/callback",
            random_id="csrf-state-123",
        )
        self.assertIn("https://auth.mercadopago.com/authorization", url)
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        self.assertEqual(["my-app-id"], params["client_id"])
        self.assertEqual(["code"], params["response_type"])
        self.assertEqual(["csrf-state-123"], params["state"])
        self.assertEqual(["https://example.com/callback"], params["redirect_uri"])

    def test_create(self):
        fixture = self.load_fixture("oauth_create.json")
        self.mock_post(fixture, status=200)
        oauth_object = {
            "client_secret": "TEST_TOKEN",
            "code": "auth-code-123",
            "redirect_uri": "https://example.com/callback",
            "grant_type": "authorization_code",
        }
        result = self.sdk.oauth().create(oauth_object)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("APP_USR-001", resp["access_token"])
        self.assertEqual("bearer", resp["token_type"])
        self.assertEqual(15552000, resp["expires_in"])
        self.assertIn("refresh_token", resp)
        self.assertIn("scope", resp)
        self.mock_http.post.assert_called_once()

    def test_refresh(self):
        fixture = self.load_fixture("oauth_create.json")
        self.mock_post(fixture, status=200)
        oauth_object = {
            "client_secret": "TEST_TOKEN",
            "refresh_token": "TG-001-test-refresh-token",
            "grant_type": "refresh_token",
        }
        result = self.sdk.oauth().refresh(oauth_object)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIn("access_token", resp)
        self.assertIn("token_type", resp)
        self.assertIn("expires_in", resp)
        self.mock_http.post.assert_called_once()

    def test_create_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.oauth().create("not-a-dict")

    def test_refresh_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.oauth().refresh("not-a-dict")


if __name__ == "__main__":
    unittest.main()
