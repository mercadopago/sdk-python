"""
    Module: test_order_checkout_pro
"""
import dataclasses
import os
import random
import unittest

import mercadopago
from mercadopago.resources.order_checkout_pro import (
    OrderCheckoutProConfig,
    OrderCheckoutProInstallments,
    OrderCheckoutProInterestFree,
    OrderCheckoutProOnlineConfig,
    OrderCheckoutProPaymentMethod,
    OrderCheckoutProTrack,
)


class TestOrderCheckoutPro(unittest.TestCase):
    """
    Test Module: Order Checkout Pro
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

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

    def test_create_checkout_pro_order(self):
        """
        Test Function: Create Checkout Pro Order
        """
        random_email_id = random.randint(100000, 999999)
        order_object = {
            "type": "online",
            "total_amount": "500.00",
            "external_reference": "ext_ref_checkout_pro",
            "processing_mode": "manual",
            "capture_mode": "automatic",
            "marketplace_fee": "5.00",
            "description": "Travel package SAO-RIO with insurance",
            "expiration_time": "P1D",
            "payer": {
                "email": f"test_payer_{random_email_id}@testuser.com",
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
            "config": dataclasses.asdict(self.build_checkout_pro_config()),
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

        order_created = self.sdk.order().create(order_object)
        self.assertEqual(order_created["status"], 201)
        self.assertEqual(order_created["response"]["status"], "created")
        self.assertEqual(order_created["response"]["type"], "online")
        self.assertEqual(order_created["response"]["processing_mode"], "manual")
        self.assertIn("id", order_created["response"])
        self.assertIn("checkout_url", order_created["response"])


if __name__ == "__main__":
    unittest.main()
