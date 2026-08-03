"""Unit tests for Refund.get() using MagicMock."""
import unittest
from unittest.mock import MagicMock

from mercadopago.config.request_options import RequestOptions
from mercadopago.resources.refund import Refund


class TestRefundGet(unittest.TestCase):
    """Unit tests for Refund.get()."""

    def _make_refund(self, http_client):
        request_options = RequestOptions(access_token="TEST_TOKEN")
        return Refund(request_options, http_client)

    def test_get_returns_refund_by_id(self):
        """Verifies get() returns the correct refund and calls the expected URL."""
        http_client = MagicMock()
        http_client.get.return_value = {"status": 200, "response": {"id": 99, "status": "approved"}}

        refund = self._make_refund(http_client)
        result = refund.get(payment_id=123, refund_id=99)

        self.assertEqual(result["status"], 200)
        self.assertEqual(result["response"]["id"], 99)
        http_client.get.assert_called_once()
        call_args = http_client.get.call_args
        called_url = (
            call_args.kwargs.get("url")
            or call_args[1].get("url")
            or call_args[0][0]
        )
        self.assertIn("/v1/payments/123/refunds/99", called_url)

    def test_get_passes_request_options(self):
        """Verifies custom request_options are forwarded to the HTTP client."""
        http_client = MagicMock()
        http_client.get.return_value = {"status": 200, "response": {"id": 55}}

        custom_options = RequestOptions(access_token="CUSTOM_TOKEN")
        refund = self._make_refund(http_client)
        result = refund.get(payment_id=10, refund_id=55, request_options=custom_options)

        self.assertEqual(result["status"], 200)
        http_client.get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
