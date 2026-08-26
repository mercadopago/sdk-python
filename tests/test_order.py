"""Unit tests for the Order resource using a mock HTTP client."""
import unittest
from dataclasses import asdict

from mercadopago.resources.order_automatic_payments import OrderAutomaticPayments
from tests.base_client_test import BaseClientTest


class TestOrder(BaseClientTest):
    """Test Module: Order"""

    def test_create(self):
        fixture = self.load_fixture("order_create.json")
        self.mock_post(fixture, status=201)
        order_object = {
            "type": "online",
            "processing_mode": "automatic",
            "total_amount": "1000.00",
            "payer": {"email": "test_user@testuser.com"},
        }
        result = self.sdk.order().create(order_object)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual("01JKXTQ2AZVE0RANCPYA6WBNPW", resp["id"])
        self.assertEqual("online", resp["type"])
        self.assertEqual("automatic", resp["processing_mode"])
        self.assertEqual("processed", resp["status"])
        self.assertEqual("1000.00", resp["total_amount"])
        self.assertIsInstance(resp["items"], list)
        self.assertEqual("Point Mini", resp["items"][0]["title"])
        self.assertIn("transactions", resp)
        self.assertIn("payments", resp["transactions"])
        self.assertEqual("BR", resp["country_code"])
        self.mock_http.post.assert_called_once()

    def test_get(self):
        fixture = self.load_fixture("order_get.json")
        self.mock_get(fixture)
        result = self.sdk.order().get("01JKXTQ2AZVE0RANCPYA6WBNPW")
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("01JKXTQ2AZVE0RANCPYA6WBNPW", resp["id"])
        self.assertEqual("processed", resp["status"])
        self.assertEqual("fully_processed", resp["status_detail"])
        self.assertEqual("1000.00", resp["total_amount"])
        self.assertEqual("1000.00", resp["total_paid_amount"])
        self.assertIn("payer", resp)
        self.assertEqual("test_user@testuser.com", resp["payer"]["email"])
        self.assertIsInstance(resp["items"], list)
        self.assertIn("transactions", resp)
        self.assertIn("payments", resp["transactions"])
        self.assertEqual("pay-001", resp["transactions"]["payments"][0]["id"])
        self.assertIn("created_date", resp)
        self.assertIn("last_updated_date", resp)
        self.mock_http.get.assert_called_once()

    def test_get_raises_for_non_string(self):
        with self.assertRaises(ValueError):
            self.sdk.order().get(123)

    def test_process(self):
        fixture = self.load_fixture("order_process.json")
        self.mock_post(fixture, status=200)
        result = self.sdk.order().process("01JKXTQ2AZVE0RANCPYA6WBNPW")
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("01JKXTQ2AZVE0RANCPYA6WBNPW", resp["id"])
        self.assertEqual("processed", resp["status"])
        self.mock_http.post.assert_called_once()

    def test_process_raises_for_non_string(self):
        with self.assertRaises(ValueError):
            self.sdk.order().process(123)

    def test_cancel(self):
        fixture = self.load_fixture("order_cancel.json")
        self.mock_post(fixture, status=200)
        result = self.sdk.order().cancel("01JKXTQ2AZVE0RANCPYA6WBNPW")
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("01JKXTQ2AZVE0RANCPYA6WBNPW", resp["id"])
        self.assertEqual("canceled", resp["status"])
        self.mock_http.post.assert_called_once()

    def test_capture(self):
        fixture = self.load_fixture("order_capture.json")
        self.mock_post(fixture, status=200)
        result = self.sdk.order().capture("01JKXTQ2AZVE0RANCPYA6WBNPW")
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertEqual("01JKXTQ2AZVE0RANCPYA6WBNPW", resp["id"])
        self.assertEqual("processed", resp["status"])
        self.mock_http.post.assert_called_once()

    def test_refund(self):
        fixture = self.load_fixture("order_refund.json")
        self.mock_post(fixture, status=201)
        result = self.sdk.order().refund("01JKXTQ2AZVE0RANCPYA6WBNPW")
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual("approved", resp["status"])
        self.assertIn("date_created", resp)
        self.mock_http.post.assert_called_once()

    def test_refund_with_object(self):
        fixture = self.load_fixture("order_refund.json")
        self.mock_post(fixture, status=201)
        refund_object = {"transactions": [{"id": "tx-001", "amount": "25.00"}]}
        result = self.sdk.order().refund("01JKXTQ2AZVE0RANCPYA6WBNPW", refund_object)
        self.assertEqual(201, result["status"])
        self.mock_http.post.assert_called_once()

    def test_search(self):
        fixture = self.load_fixture("order_search.json")
        self.mock_get(fixture)
        result = self.sdk.order().search()
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIn("data", resp)
        self.assertIsInstance(resp["data"], list)
        self.assertEqual("01JKXTQ2AZVE0RANCPYA6WBNPW", resp["data"][0]["id"])
        self.mock_http.get.assert_called_once()

    def test_create_transaction(self):
        self.mock_post({"id": "tx-001"}, status=201)
        transaction_object = {
            "payments": [{"amount": "1000.00", "payment_method": {"id": "visa"}}]
        }
        result = self.sdk.order().create_transaction("01JKXTQ2AZVE0RANCPYA6WBNPW", transaction_object)
        self.assertEqual(201, result["status"])
        self.mock_http.post.assert_called_once()

    def test_update_transaction(self):
        self.mock_put({"id": "tx-001"})
        result = self.sdk.order().update_transaction(
            "01JKXTQ2AZVE0RANCPYA6WBNPW", "tx-001", {"payment_method": {"id": "master"}}
        )
        self.assertEqual(200, result["status"])
        self.mock_http.put.assert_called_once()

    def test_delete_transaction(self):
        self.mock_delete(None, status=204)
        result = self.sdk.order().delete_transaction("01JKXTQ2AZVE0RANCPYA6WBNPW", "tx-001")
        self.assertEqual(204, result["status"])
        self.mock_http.delete.assert_called_once()

    def test_create_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.order().create("not-a-dict")

    def test_automatic_payments_subscription_payload(self):
        automatic_payments = OrderAutomaticPayments(
            subscription={
                "id": "subscription-1",
                "sequence": {"number": 1, "total": 12},
                "invoice": {
                    "id": "invoice-1",
                    "billing_date": "2026-08-26",
                    "period": {"interval": 1, "type": "month"},
                },
            }
        )

        payload = asdict(automatic_payments)

        self.assertEqual("subscription-1", payload["subscription"]["id"])
        self.assertEqual(12, payload["subscription"]["sequence"]["total"])
        self.assertEqual("month", payload["subscription"]["invoice"]["period"]["type"])


if __name__ == "__main__":
    unittest.main()
