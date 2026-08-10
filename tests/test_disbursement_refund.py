"""Unit tests for the DisbursementRefund resource using a mock HTTP client."""
import unittest

from tests.base_client_test import BaseClientTest


class TestDisbursementRefund(BaseClientTest):
    """Test Module: DisbursementRefund"""

    def test_list_all(self):
        fixture = self.load_fixture("disbursement_refund_list_all.json")
        self.mock_get(fixture)
        result = self.sdk.disbursement_refund().list_all(999)
        self.assertEqual(200, result["status"])
        resp = result["response"]
        self.assertIsInstance(resp, list)
        self.assertEqual(1, resp[0]["id"])
        self.assertEqual(999, resp[0]["advanced_payment_id"])
        self.assertEqual(50.0, resp[0]["amount"])
        self.assertEqual("approved", resp[0]["status"])
        self.mock_http.get.assert_called_once()

    def test_create_all(self):
        fixture = self.load_fixture("disbursement_refund_create_all.json")
        self.mock_post(fixture, status=201)
        disbursement_refund_object = {"metadata": {"reason": "Full refund"}}
        result = self.sdk.disbursement_refund().create_all(999, disbursement_refund_object)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual(1, resp["id"])
        self.assertEqual(999, resp["advanced_payment_id"])
        self.assertEqual("approved", resp["status"])
        self.mock_http.post.assert_called_once()

    def test_create(self):
        fixture = self.load_fixture("disbursement_refund_create.json")
        self.mock_post(fixture, status=201)
        result = self.sdk.disbursement_refund().create(999, 10, 25.0)
        self.assertEqual(201, result["status"])
        resp = result["response"]
        self.assertEqual(2, resp["id"])
        self.assertEqual(10, resp["disbursement_id"])
        self.assertEqual(25.0, resp["amount"])
        self.assertEqual("approved", resp["status"])
        self.mock_http.post.assert_called_once()

    def test_create_raises_for_non_float_amount(self):
        with self.assertRaises(ValueError):
            self.sdk.disbursement_refund().create(999, 10, 25)

    def test_create_all_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.disbursement_refund().create_all(999, "not-a-dict")

    def test_save(self):
        fixture = self.load_fixture("disbursement_refund_create.json")
        self.mock_post(fixture, status=201)
        disbursement_refund_object = {"amount": 25.0}
        result = self.sdk.disbursement_refund().save(999, 10, disbursement_refund_object)
        self.assertEqual(201, result["status"])
        self.mock_http.post.assert_called_once()

    def test_save_raises_for_non_dict(self):
        with self.assertRaises(ValueError):
            self.sdk.disbursement_refund().save(999, 10, "not-a-dict")


if __name__ == "__main__":
    unittest.main()
