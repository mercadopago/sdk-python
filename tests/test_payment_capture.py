"""
    Module: test_payment_capture
"""
import json
import unittest
from unittest.mock import MagicMock, patch

import mercadopago
from mercadopago.http.http_client import HttpClient


PAYMENT_ID = 123456789

CAPTURED_PAYMENT_RESPONSE = {
    "id": PAYMENT_ID,
    "status": "approved",
    "captured": True,
    "transaction_amount": 100.0,
}


class TestPaymentCapture(unittest.TestCase):
    """
    Test Module: Payment.capture
    """

    def _make_sdk_with_mock_put(self, return_value):
        mock_http = MagicMock(spec=HttpClient)
        mock_http.put.return_value = return_value
        return mercadopago.SDK("TEST_ACCESS_TOKEN", http_client=mock_http), mock_http

    def test_capture_full(self):
        """Captures the full authorized amount when no amount is given."""
        sdk, mock_http = self._make_sdk_with_mock_put(
            {"status": 200, "response": CAPTURED_PAYMENT_RESPONSE}
        )

        result = sdk.payment().capture(PAYMENT_ID)

        self.assertEqual(result["status"], 200)
        self.assertTrue(result["response"]["captured"])

        mock_http.put.assert_called_once()
        call_kwargs = mock_http.put.call_args
        url = call_kwargs[1]["url"] if "url" in call_kwargs[1] else call_kwargs[0][0]
        self.assertIn(str(PAYMENT_ID), url)

        body = json.loads(call_kwargs[1]["data"])
        self.assertTrue(body["capture"])
        self.assertNotIn("transaction_amount", body)

    def test_capture_partial(self):
        """Captures a specific amount and includes transaction_amount in the request body."""
        partial_amount = 50.0
        response_body = dict(CAPTURED_PAYMENT_RESPONSE, transaction_amount=partial_amount)
        sdk, mock_http = self._make_sdk_with_mock_put(
            {"status": 200, "response": response_body}
        )

        result = sdk.payment().capture(PAYMENT_ID, amount=partial_amount)

        self.assertEqual(result["status"], 200)

        mock_http.put.assert_called_once()
        call_kwargs = mock_http.put.call_args
        body = json.loads(call_kwargs[1]["data"])
        self.assertTrue(body["capture"])
        self.assertEqual(body["transaction_amount"], partial_amount)


if __name__ == "__main__":
    unittest.main()
