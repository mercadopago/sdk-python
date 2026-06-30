"""
    Module: test_order_checkout_pro
"""
import json
import os
import random
import unittest

import mercadopago
from mercadopago.config import RequestOptions
from mercadopago.http import HttpClient
from mercadopago.resources.order_checkout_pro import (
    OrderCheckoutProConfig,
    OrderCheckoutProInstallments,
    OrderCheckoutProInterestFree,
    OrderCheckoutProOnlineConfig,
    OrderCheckoutProPaymentMethod,
    OrderCheckoutProTrack,
    OrderCheckoutProDict,
)


class FakeHttpClient(HttpClient):
    """Captures requests without sending them to the API."""

    def __init__(self):
        self.post_calls = []
        self.get_calls = []

    def post(self, url, headers, data=None, params=None, timeout=None, maxretries=None):
        self.post_calls.append({
            "url": url,
            "headers": headers,
            "data": data,
            "params": params,
            "timeout": timeout,
            "maxretries": maxretries,
        })
        return {
            "status": 201,
            "response": {
                "id": "ORDTST01KS5AJ6HTK2HRQ3XJ3C2JCKP9",
                "status": "created",
                "type": "online",
                "processing_mode": "manual",
                "checkout_url": "https://www.mercadopago.com/checkout/v1/redirect",
            },
        }

    def get(self, url, headers, params=None, timeout=None, maxretries=None):
        self.get_calls.append({
            "url": url,
            "headers": headers,
            "params": params,
            "timeout": timeout,
            "maxretries": maxretries,
        })
        return {"status": 200, "response": {"id": "ORD123"}}


class TestOrderCheckoutPro(unittest.TestCase):
    """
    Test Module: Order Checkout Pro
    """

    def build_checkout_pro_config(self):
        return OrderCheckoutProConfig(
            statement_descriptor="MYSTORE",
            default_payment_due_date="P1D",
            online=OrderCheckoutProOnlineConfig(
                available_from="2027-01-01T00:00:00Z",
                allowed_user_type="account_only",
                success_url="https://example.com/success",
                failure_url="https://example.com/failure",
                pending_url="https://example.com/pending",
                auto_return="approved",
                tracks=[
                    OrderCheckoutProTrack(
                        type="google_ad",
                        values={
                            "conversion_id": "21312312312123",
                            "conversion_label": "TEST",
                        },
                    ),
                    OrderCheckoutProTrack(
                        type="facebook_ad",
                        values={"pixel_id": "21312312312123"},
                    ),
                ],
            ),
            payment_method=OrderCheckoutProPaymentMethod(
                max_installments=12,
                not_allowed_ids=["amex"],
                not_allowed_types=["ticket"],
                installments=OrderCheckoutProInstallments(
                    interest_free=OrderCheckoutProInterestFree(
                        type="range",
                        values=[2, 6],
                    ),
                ),
            ),
        )

    def build_order_object(self, payer_email="buyer@mercadopago.com"):
        return {
            "type": "online",
            "total_amount": "500.00",
            "external_reference": "ext_ref_orders_online",
            "processing_mode": "manual",
            "capture_mode": "automatic",
            "marketplace_fee": "5.00",
            "description": "Travel package SAO-RIO with insurance",
            "expiration_time": "P1D",
            "payer": {
                "email": payer_email,
                "first_name": "John",
                "last_name": "Smith",
                "phone": {
                    "area_code": "11",
                    "number": "999998888",
                },
                "identification": {
                    "type": "CPF",
                    "number": "12345678909",
                },
                "address": {
                    "zip_code": "01310-100",
                    "street_name": "Av. Paulista",
                    "street_number": "1000",
                    "neighborhood": "Bela Vista",
                    "city": "Sao Paulo",
                },
            },
            "shipment": {
                "mode": "custom",
                "local_pickup": False,
                "cost": "15.00",
                "free_shipping": False,
                "free_methods": [{"id": 73328}],
                "address": {
                    "zip_code": "01310-100",
                    "street_name": "Av. Paulista",
                    "street_number": "1000",
                    "floor": "3",
                    "apartment": "B",
                    "neighborhood": "Bela Vista",
                    "city": "Sao Paulo",
                },
            },
            "config": OrderCheckoutProDict(self.build_checkout_pro_config()),
            "items": [
                {
                    "external_code": "ITEM-001",
                    "title": "Flight SAO-RIO",
                    "description": "Round trip, economy class",
                    "category_id": "travels",
                    "picture_url": "https://example.com/img.jpg",
                    "quantity": 1,
                    "unit_price": "450.00",
                    "type": "travel",
                    "event_date": "2027-01-15T00:00:00.000-03:00",
                },
                {
                    "external_code": "ITEM-002",
                    "title": "Travel insurance",
                    "description": "Basic coverage during trip",
                    "category_id": "travels",
                    "picture_url": "https://example.com/insurance.jpg",
                    "quantity": 1,
                    "unit_price": "50.00",
                    "type": "travel",
                    "event_date": "2027-01-15T00:00:00.000-03:00",
                },
            ],
            "additional_info": {
                "payer.registration_date": "2020-01-15T00:00:00.000-03:00",
                "payer.authentication_type": "MOBILE",
                "payer.is_prime_user": True,
                "payer.is_first_purchase_online": True,
                "payer.last_purchase": "2025-12-01T00:00:00.000-03:00",
                "travel.passengers": [
                    {
                        "first_name": "John",
                        "last_name": "Smith",
                        "identification_type": "CPF",
                        "identification_number": "12345678909",
                        "item_references": ["ITEM-001"],
                    }
                ],
                "travel.routes": [
                    {
                        "departure": "SAO",
                        "destination": "RIO",
                        "departure_date_time": "2026-03-10T08:00:00.000-03:00",
                        "arrival_date_time": "2026-03-10T09:00:00.000-03:00",
                        "company": "TAM",
                        "item_references": ["ITEM-001"],
                    }
                ],
            },
        }

    def test_checkout_pro_order_payload_uses_expected_wire_keys(self):
        """
        Test Function: Create Checkout Pro Order Payload
        """
        http_client = FakeHttpClient()
        sdk = mercadopago.SDK("TEST_ACCESS_TOKEN", http_client=http_client)
        response = sdk.order().create(self.build_order_object())
        post_call = http_client.post_calls[0]
        request_body = json.loads(post_call["data"])

        self.assertEqual(response["status"], 201)
        self.assertEqual(post_call["url"], "https://api.mercadopago.com/v1/orders")
        self.assertEqual(request_body["type"], "online")
        self.assertEqual(request_body["processing_mode"], "manual")
        self.assertEqual(request_body["total_amount"], "500.00")
        self.assertEqual(request_body["marketplace_fee"], "5.00")
        self.assertEqual(request_body["shipment"]["cost"], "15.00")
        self.assertEqual(request_body["items"][0]["unit_price"], "450.00")
        self.assertEqual(request_body["items"][1]["unit_price"], "50.00")
        self.assertIs(request_body["shipment"]["local_pickup"], False)
        self.assertIs(request_body["shipment"]["free_shipping"], False)
        self.assertEqual(request_body["config"]["online"]["success_url"],
                         "https://example.com/success")
        self.assertEqual(request_body["config"]["online"]["failure_url"],
                         "https://example.com/failure")
        self.assertEqual(request_body["config"]["online"]["pending_url"],
                         "https://example.com/pending")
        self.assertEqual(request_body["config"]["online"]["auto_return"], "approved")
        self.assertEqual(
            request_body["config"]["online"]["tracks"][0]["values"]["conversion_id"],
            "21312312312123",
        )
        self.assertEqual(
            request_body["config"]["payment_method"]["installments"]["interest_free"]["type"],
            "range",
        )
        self.assertEqual(
            request_body["config"]["payment_method"]["installments"]["interest_free"]["values"],
            [2, 6],
        )
        self.assertIn("payer.authentication_type", request_body["additional_info"])
        self.assertIn("travel.passengers", request_body["additional_info"])

    def test_order_create_inherits_product_and_idempotency_headers(self):
        """
        Test Function: Create Order Headers
        """
        http_client = FakeHttpClient()
        sdk = mercadopago.SDK("TEST_ACCESS_TOKEN", http_client=http_client)
        request_options = RequestOptions(
            custom_headers={"x-idempotency-key": "fixed-idempotency-key"}
        )

        sdk.order().create(self.build_order_object(), request_options=request_options)
        headers = http_client.post_calls[0]["headers"]

        self.assertEqual(headers["Authorization"], "Bearer TEST_ACCESS_TOKEN")
        self.assertEqual(headers["x-product-id"], "bc32bpftrpp001u8nhlg")
        self.assertEqual(headers["x-idempotency-key"], "fixed-idempotency-key")
        self.assertEqual(headers["Content-type"], "application/json")

    def test_refund_alias_uses_order_refund_endpoint(self):
        """
        Test Function: Refund Order Alias
        """
        http_client = FakeHttpClient()
        sdk = mercadopago.SDK("TEST_ACCESS_TOKEN", http_client=http_client)

        sdk.order().refund("ORD123", {"transactions": [{"id": "PAY123", "amount": "25.00"}]})
        post_call = http_client.post_calls[0]
        request_body = json.loads(post_call["data"])

        self.assertEqual(post_call["url"], "https://api.mercadopago.com/v1/orders/ORD123/refund")
        self.assertEqual(request_body["transactions"][0]["amount"], "25.00")

    def test_order_checkout_pro_dict_omits_empty_values_but_keeps_false_and_zero(self):
        """
        Test Function: Compact Order Helper
        """
        payment_method = OrderCheckoutProPaymentMethod(
            max_installments=0,
            not_allowed_ids=[],
            not_allowed_types=[],
        )
        online_config = OrderCheckoutProOnlineConfig(
            allowed_user_type=None,
            success_url="https://example.com/success",
            tracks=[],
        )
        config = OrderCheckoutProDict(OrderCheckoutProConfig(
            online=online_config,
            payment_method=payment_method,
        ))

        self.assertNotIn("allowed_user_type", config["online"])
        self.assertNotIn("tracks", config["online"])
        self.assertEqual(config["online"]["success_url"], "https://example.com/success")
        self.assertNotIn("not_allowed_ids", config["payment_method"])
        self.assertNotIn("not_allowed_types", config["payment_method"])
        self.assertEqual(config["payment_method"]["max_installments"], 0)

    @unittest.skipIf("ACCESS_TOKEN" not in os.environ, "ACCESS_TOKEN is required")
    def test_create_checkout_pro_order_live(self):
        """
        Test Function: Create Checkout Pro Order Live
        """
        sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])
        random_email_id = random.randint(100000, 999999)
        order_created = sdk.order().create(
            self.build_order_object(f"test_payer_{random_email_id}@testuser.com")
        )

        self.assertEqual(order_created["status"], 201)
        self.assertEqual(order_created["response"]["status"], "created")
        self.assertEqual(order_created["response"]["type"], "online")
        self.assertEqual(order_created["response"]["processing_mode"], "manual")
        self.assertIn("id", order_created["response"])
        self.assertIn("checkout_url", order_created["response"])


if __name__ == "__main__":
    unittest.main()
