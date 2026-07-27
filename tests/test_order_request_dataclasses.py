"""Offline unit + integration tests for the typed Order request dataclasses.

These tests do not hit the live API. They verify:
  * new dataclasses produce the correct snake_case keys,
  * None filtering (DD-3) removes unset fields,
  * the existing dict path still works (backward compatibility),
  * the typed Automatic Payments flow serializes correctly.
"""
import dataclasses
import json
import unittest

import mercadopago
from mercadopago.http import HttpClient
from mercadopago.resources.order_automatic_payments import OrderAutomaticPayments
from mercadopago.resources.order_create import (
    OrderCreateRequest,
    OrderIdentification,
    OrderPayerRequest,
    order_request_to_dict,
)
from mercadopago.resources.order_integration_data import (
    OrderIntegrationData,
    OrderSponsor,
)
from mercadopago.resources.order_item import OrderItemRequest
from mercadopago.resources.order_payer import (
    OrderPayerAddress,
    OrderPayerPhone,
)
from mercadopago.resources.order_shipment import (
    OrderShipmentAddress,
    OrderShipmentFreeMethod,
    OrderShipmentRequest,
)
from mercadopago.resources.order_stored_credential import OrderStoredCredential
from mercadopago.resources.order_subscription_data import (
    OrderInvoicePeriod,
    OrderSubscriptionData,
    OrderSubscriptionSequence,
)
from mercadopago.resources.order_transaction_security import OrderTransactionSecurity


class _CapturingHttpClient(HttpClient):
    """HttpClient stub that captures the request body instead of sending it."""

    def __init__(self):
        self.last_url = None
        self.last_data = None

    def post(self, url, headers,  # noqa: D401
             data=None, params=None, timeout=None, maxretries=None):
        self.last_url = url
        self.last_data = data
        return {"status": 201, "response": {"id": "ORDER_ID", "status": "processed"}}


def _make_sdk():
    http = _CapturingHttpClient()
    sdk = mercadopago.SDK("TEST_TOKEN", http_client=http)
    return sdk, http


class TestOrderItemRequest(unittest.TestCase):
    def test_snake_case_keys(self):
        item = OrderItemRequest(
            title="A book",
            type="physical",
            warranty=True,
            event_date="2026-07-01",
            unit_price="100.00",
            external_code="EXT-1",
            category_id="books",
            description="A nice book",
            picture_url="https://example.com/p.png",
            quantity=2,
        )
        as_dict = order_request_to_dict(item)
        self.assertEqual(
            set(as_dict.keys()),
            {
                "title", "type", "warranty", "event_date", "unit_price",
                "external_code", "category_id", "description", "picture_url",
                "quantity",
            },
        )
        self.assertEqual(as_dict["unit_price"], "100.00")
        self.assertEqual(as_dict["quantity"], 2)

    def test_none_fields_filtered(self):
        item = OrderItemRequest(title="Only title", quantity=1)
        as_dict = order_request_to_dict(item)
        self.assertEqual(as_dict, {"title": "Only title", "quantity": 1})


class TestOrderShipmentRequest(unittest.TestCase):
    def test_full_shipment_snake_case(self):
        shipment = OrderShipmentRequest(
            mode="me2",
            local_pickup=False,
            cost="10.00",
            free_shipping=True,
            free_methods=[OrderShipmentFreeMethod(id=1), OrderShipmentFreeMethod(id=2)],
            address=OrderShipmentAddress(
                street_name="Main",
                street_number="123",
                zip_code="0000",
                floor="2",
                apartment="B",
                neighborhood="Centro",
                state="SP",
                city="Sao Paulo",
                complement="near park",
            ),
        )
        as_dict = order_request_to_dict(shipment)
        self.assertEqual(as_dict["free_methods"], [{"id": 1}, {"id": 2}])
        self.assertEqual(as_dict["address"]["street_name"], "Main")
        self.assertIn("free_shipping", as_dict)
        self.assertIn("local_pickup", as_dict)

    def test_partial_shipment_filters_none(self):
        shipment = OrderShipmentRequest(mode="custom", cost="5.00")
        as_dict = order_request_to_dict(shipment)
        self.assertEqual(as_dict, {"mode": "custom", "cost": "5.00"})


class TestOrderPayer(unittest.TestCase):
    def test_payer_phone_and_address(self):
        payer = OrderPayerRequest(
            email="buyer@example.com",
            first_name="Jane",
            last_name="Doe",
            customer_id="CUST-1",
            entity_type="individual",
            identification=OrderIdentification(type="CPF", number="12345678909"),
            phone=OrderPayerPhone(area_code="11", number="999999999"),
            address=OrderPayerAddress(
                zip_code="0000",
                street_name="Main",
                street_number="123",
                neighborhood="Centro",
                city="Sao Paulo",
                state="SP",
                complement="apt 1",
                country="BR",
            ),
        )
        as_dict = order_request_to_dict(payer)
        self.assertEqual(as_dict["phone"], {"area_code": "11", "number": "999999999"})
        self.assertEqual(as_dict["address"]["zip_code"], "0000")
        self.assertEqual(as_dict["identification"], {"type": "CPF", "number": "12345678909"})

    def test_payer_email_only_filters_none(self):
        payer = OrderPayerRequest(email="buyer@example.com")
        self.assertEqual(order_request_to_dict(payer), {"email": "buyer@example.com"})


class TestOrderTransactionSecurity(unittest.TestCase):
    def test_snake_case_keys(self):
        sec = OrderTransactionSecurity(validation="complete", liability_shift="yes")
        self.assertEqual(
            order_request_to_dict(sec),
            {"validation": "complete", "liability_shift": "yes"},
        )


class TestOrderCreateRequestRootFields(unittest.TestCase):
    def test_all_root_fields_present(self):
        req = OrderCreateRequest(
            type="online",
            external_reference="ext_ref_1234",
            total_amount="200.00",
            currency="BRL",
            capture_mode="automatic_async",
            processing_mode="automatic",
            description="An order",
            marketplace="NONE",
            marketplace_fee="1.00",
            expiration_time="P3D",
            checkout_available_at="2026-07-22T00:00:00.000-03:00",
        )
        as_dict = order_request_to_dict(req)
        for key in (
            "description", "marketplace", "marketplace_fee",
            "expiration_time", "checkout_available_at", "currency",
        ):
            self.assertIn(key, as_dict)
        self.assertEqual(as_dict["marketplace_fee"], "1.00")

    def test_none_root_fields_filtered(self):
        req = OrderCreateRequest(type="online", total_amount="10.00")
        as_dict = order_request_to_dict(req)
        self.assertEqual(as_dict, {"type": "online", "total_amount": "10.00"})
        self.assertNotIn("marketplace", as_dict)

    def test_config_online_transaction_security_nesting(self):
        # transaction_security lives under config.online (not root).
        req = OrderCreateRequest(
            type="online",
            config={
                "online": {
                    "transaction_security": order_request_to_dict(
                        OrderTransactionSecurity(validation="complete")
                    )
                }
            },
        )
        as_dict = order_request_to_dict(req)
        self.assertEqual(
            as_dict["config"]["online"]["transaction_security"],
            {"validation": "complete"},
        )
        self.assertNotIn("transaction_security", as_dict)

    def test_helper_rejects_non_dataclass(self):
        with self.assertRaises(TypeError):
            order_request_to_dict({"type": "online"})


class TestOrderCreateDualPath(unittest.TestCase):
    def test_dict_path_backward_compat(self):
        sdk, http = _make_sdk()
        order_object = {
            "type": "online",
            "total_amount": "200.00",
            "external_reference": "ext_ref_1234",
            "payer": {"email": "buyer@example.com"},
        }
        result = sdk.order().create(order_object)
        self.assertEqual(result["status"], 201)
        sent = json.loads(http.last_data)
        self.assertEqual(sent, order_object)

    def test_dataclass_path_matches_dict_path(self):
        sdk, http = _make_sdk()
        typed = OrderCreateRequest(
            type="online",
            total_amount="200.00",
            external_reference="ext_ref_1234",
            payer=OrderPayerRequest(email="buyer@example.com"),
            items=[OrderItemRequest(title="A book", unit_price="200.00", quantity=1)],
        )
        sdk.order().create(typed)
        sent_typed = json.loads(http.last_data)

        equivalent_dict = {
            "type": "online",
            "total_amount": "200.00",
            "external_reference": "ext_ref_1234",
            "payer": {"email": "buyer@example.com"},
            "items": [{"title": "A book", "unit_price": "200.00", "quantity": 1}],
        }
        sdk2, http2 = _make_sdk()
        sdk2.order().create(equivalent_dict)
        sent_dict = json.loads(http2.last_data)

        self.assertEqual(sent_typed, sent_dict)

    def test_invalid_type_raises(self):
        sdk, _ = _make_sdk()
        with self.assertRaises(ValueError):
            sdk.order().create("not-a-dict")


class TestAutomaticPaymentsTypedFlow(unittest.TestCase):
    def test_ap_flow_snake_case(self):
        sdk, http = _make_sdk()
        order_object = {
            "type": "online",
            "total_amount": "100.00",
            "external_reference": "subscription-001-payment-2",
            "payer": {"email": "customer@example.com", "customer_id": "CUSTOMER_ID"},
            "transactions": {
                "payments": [
                    {
                        "amount": "100.00",
                        "payment_method": {
                            "id": "master",
                            "type": "credit_card",
                            "token": "CARD_TOKEN",
                            "installments": 1,
                        },
                        "automatic_payments": dataclasses.asdict(
                            OrderAutomaticPayments(
                                payment_profile_id="PROFILE",
                                schedule_date="2026-08-01T00:00:00.000-04:00",
                                due_date="2026-08-05T00:00:00.000-04:00",
                                retries=3,
                            )
                        ),
                        "stored_credential": dataclasses.asdict(
                            OrderStoredCredential(
                                payment_initiator="merchant",
                                reason="recurring",
                                store_payment_method=False,
                                first_payment=False,
                                prev_transaction_ref="PREV_TX",
                            )
                        ),
                        "subscription_data": dataclasses.asdict(
                            OrderSubscriptionData(
                                invoice_id="INVOICE_002",
                                billing_date="2026-07-01",
                                subscription_sequence=OrderSubscriptionSequence(number=2, total=12),
                                invoice_period=OrderInvoicePeriod(type="monthly", period=1),
                            )
                        ),
                    }
                ]
            },
            "integration_data": dataclasses.asdict(
                OrderIntegrationData(
                    integrator_id="INT-1",
                    platform_id="PLAT-1",
                    corporation_id="CORP-1",
                    sponsor=OrderSponsor(id="SPONSOR-1"),
                )
            ),
        }
        result = sdk.order().create(order_object)
        self.assertEqual(result["status"], 201)
        sent = json.loads(http.last_data)
        payment = sent["transactions"]["payments"][0]
        self.assertEqual(payment["stored_credential"]["prev_transaction_ref"], "PREV_TX")
        self.assertEqual(payment["automatic_payments"]["payment_profile_id"], "PROFILE")
        self.assertEqual(
            payment["subscription_data"]["subscription_sequence"],
            {"number": 2, "total": 12},
        )
        self.assertEqual(sent["integration_data"]["sponsor"], {"id": "SPONSOR-1"})

    def test_ap_typed_via_dataclass_root(self):
        # AP nested dicts inside a typed OrderCreateRequest (transactions kept as dict).
        sdk, http = _make_sdk()
        typed = OrderCreateRequest(
            type="online",
            total_amount="100.00",
            payer=OrderPayerRequest(email="customer@example.com", customer_id="CUSTOMER_ID"),
            transactions={
                "payments": [
                    {
                        "amount": "100.00",
                        "stored_credential": dataclasses.asdict(
                            OrderStoredCredential(
                                payment_initiator="merchant",
                                first_payment=True,
                            )
                        ),
                    }
                ]
            },
        )
        sdk.order().create(typed)
        sent = json.loads(http.last_data)
        sc = sent["transactions"]["payments"][0]["stored_credential"]
        # first_payment stays; None fields (reason, prev_transaction_ref) are dropped.
        self.assertEqual(sc, {"payment_initiator": "merchant", "first_payment": True})


if __name__ == "__main__":
    unittest.main()
