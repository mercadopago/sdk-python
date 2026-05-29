"""Example: Automatic Payments flow with the MercadoPago Orders API.

Demonstrates both the first payment (storing the card credential) and a
subsequent recurring charge (referencing the previous transaction).
"""
import dataclasses
import mercadopago
from mercadopago.resources.order_automatic_payments import OrderAutomaticPayments
from mercadopago.resources.order_stored_credential import OrderStoredCredential
from mercadopago.resources.order_subscription_data import (
    OrderInvoicePeriod,
    OrderSubscriptionData,
    OrderSubscriptionSequence,
)

sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")


# ── First payment ──────────────────────────────────────────────────────────
# Use first_payment=True and no prev_transaction_ref.
# The API stores the credential for future charges.

first_payment_order = {
    "type": "online",
    "total_amount": "100.00",
    "external_reference": "subscription-001-payment-1",
    "payer": {
        "email": "customer@example.com",
        "customer_id": "CUSTOMER_ID",
    },
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
                        payment_profile_id="PAYMENT_PROFILE_ID",
                        schedule_date="2026-07-01T00:00:00.000-04:00",
                        due_date="2026-07-05T00:00:00.000-04:00",
                        retries=3,
                    )
                ),
                "stored_credential": dataclasses.asdict(
                    OrderStoredCredential(
                        payment_initiator="merchant",
                        reason="recurring",
                        store_payment_method=True,
                        first_payment=True,
                        # prev_transaction_ref not required on first payment
                    )
                ),
                "subscription_data": dataclasses.asdict(
                    OrderSubscriptionData(
                        invoice_id="INVOICE_001",
                        billing_date="2026-06-01",
                        subscription_sequence=OrderSubscriptionSequence(number=1, total=12),
                        invoice_period=OrderInvoicePeriod(type="monthly", period=1),
                    )
                ),
            }
        ]
    },
}

result = sdk.order().create(first_payment_order)
first_order = result["response"]
print("First payment order:", first_order.get("id"), "→", first_order.get("status"))

# Save the transaction ID for use in the next charge.
first_transaction_id = (
    first_order.get("transactions", {})
    .get("payments", [{}])[0]
    .get("id", "")
)


# ── Subsequent recurring charge ────────────────────────────────────────────
# Use first_payment=False and include prev_transaction_ref pointing to the
# previous charge. The API links this payment to the original authorization.

recurring_order = {
    "type": "online",
    "total_amount": "100.00",
    "external_reference": "subscription-001-payment-2",
    "payer": {
        "email": "customer@example.com",
        "customer_id": "CUSTOMER_ID",
    },
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
                        payment_profile_id="PAYMENT_PROFILE_ID",
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
                        prev_transaction_ref=first_transaction_id,  # required
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
}

result = sdk.order().create(recurring_order)
recurring = result["response"]
print("Recurring charge order:", recurring.get("id"), "→", recurring.get("status"))
