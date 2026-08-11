"""Unit tests for the Order resource — Checkout Pro scenarios.

Checkout Pro uses the same Order resource but exercises the
``processing_mode: manual`` (builder) flow and multi-transaction orders.
"""
import unittest

from tests.base_client_test import BaseClientTest


class TestOrderCheckoutPro(BaseClientTest):
    """Test Module: Order (Checkout Pro scenarios)"""

    def test_create_builder_mode(self):
        self.mock_post({"id": "order-cp-001", "status": "open"}, status=201)
        order_object = {
            "type": "online",
            "processing_mode": "manual",
            "total_amount": "500.00",
            "payer": {"email": "buyer@example.com"},
        }
        result = self.sdk.order().create(order_object)
        self.assertEqual(201, result["status"])
        self.assertEqual("order-cp-001", result["response"]["id"])

    def test_process_builder_order(self):
        self.mock_post({"id": "order-cp-001", "status": "processed"}, status=200)
        result = self.sdk.order().process("order-cp-001")
        self.assertEqual(200, result["status"])
        self.assertEqual("processed", result["response"]["status"])

    def test_refund_transaction_partial(self):
        self.mock_post({"id": "refund-cp-001", "status": "approved"}, status=201)
        refund_object = {
            "transactions": [{"id": "tx-cp-001", "amount": "100.00"}]
        }
        result = self.sdk.order().refund_transaction("order-cp-001", refund_object)
        self.assertEqual(201, result["status"])

    def test_refund_transaction_full(self):
        self.mock_post({"id": "refund-cp-002", "status": "approved"}, status=201)
        result = self.sdk.order().refund_transaction("order-cp-001")
        self.assertEqual(201, result["status"])


if __name__ == "__main__":
    unittest.main()
