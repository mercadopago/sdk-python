"""Mercado Pago - Create Order for Checkout Pro.

Checkout Pro through Orders uses ``type="online"`` and
``processing_mode="manual"``. The API returns ``checkout_url`` in the created
order response; redirect the buyer to that URL to continue the payment flow.
"""
from mercadopago import SDK
from mercadopago.resources.order_checkout_pro import (
    OrderCheckoutProConfig,
    OrderCheckoutProInstallments,
    OrderCheckoutProInterestFree,
    OrderCheckoutProOnlineConfig,
    OrderCheckoutProPaymentMethod,
    OrderCheckoutProTrack,
    OrderCheckoutProDict,
)


def main():
    access_token = "<YOUR_ACCESS_TOKEN>"
    sdk = SDK(access_token)

    checkout_pro_config = OrderCheckoutProConfig(
        statement_descriptor="MYSTORE",
        default_payment_due_date="P1D",
        online=OrderCheckoutProOnlineConfig(
            available_from="2026-01-01T00:00:00Z",
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
            "email": "<PAYER_EMAIL>",
            "first_name": "<FIRST_NAME>",
            "last_name": "<LAST_NAME>",
            "phone": {
                "area_code": "11",
                "number": "999998888",
            },
            "identification": {
                "type": "CPF",
                "number": "<PAYER_DOC_NUMBER>",
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
        "config": OrderCheckoutProDict(checkout_pro_config),
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
        # Orders accepts vertical data with dotted keys under additional_info.
        "additional_info": {
            "payer.registration_date": "2020-01-15T00:00:00.000-03:00",
            "payer.authentication_type": "MOBILE",
            "payer.is_prime_user": True,
            "payer.is_first_purchase_online": True,
            "payer.last_purchase": "2025-12-01T00:00:00.000-03:00",
            "travel.passengers": [
                {
                    "first_name": "<PASSENGER_FIRST_NAME>",
                    "last_name": "<PASSENGER_LAST_NAME>",
                    "identification_type": "CPF",
                    "identification_number": "<PASSENGER_DOC_NUMBER>",
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

    try:
        response = sdk.order().create(order_object)
        order = response["response"]
        print("Order created successfully:")
        print("id:", order.get("id"))
        print("status:", order.get("status"))
        print("checkout_url:", order.get("checkout_url"))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
