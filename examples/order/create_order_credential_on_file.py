"""Example: CREDENTIAL_ON_FILE automatic payment flows with the MercadoPago Orders API.

Demonstrates three scenarios that use the ``transaction_data`` block with
``type: "CREDENTIAL_ON_FILE"``:

1. **CIT – Customer-Initiated Transaction (enrolment)**
   The cardholder authorises the first charge and the credential is stored for
   future use.  ``first_transaction: True``, ``storage: "store"``,
   ``transaction_initiator: "customer"``.

2. **MIT – Merchant-Initiated Transaction (scheduled recurring charge)**
   The merchant triggers a charge without cardholder interaction, referencing the
   original CIT. ``first_transaction: False``, ``storage: "stored"``,
   ``transaction_initiator: "merchant"``, ``reference.id`` pointing to the CIT
   payment id.

3. **UCOF-CIT – Unscheduled Card-On-File, Customer-Initiated**
   The cardholder initiates a one-off purchase using a previously stored card.
   ``sub_type: "unscheduled"``, ``storage: "stored"``,
   ``transaction_initiator: "customer"``, ``first_transaction: False``.
"""
import mercadopago

sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")


# ── 1. CIT – Enrolment / first payment ────────────────────────────────────────
# The cardholder completes checkout and their card is stored for future charges.

cit_order = {
    "type": "online",
    "total_amount": "100.00",
    "external_reference": "cof-subscription-001-cit",
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
                "transaction_data": {
                    # CREDENTIAL_ON_FILE identifies this as a stored-credential flow.
                    "type": "CREDENTIAL_ON_FILE",
                    # "recurring" indicates a subscription-style agreement.
                    "sub_type": "recurring",
                    # "store" signals that the credential should be saved now.
                    "storage": "store",
                    # The cardholder is present and initiates this first charge.
                    "transaction_initiator": "customer",
                    # Mark as first transaction so the network creates the mandate.
                    "first_transaction": True,
                },
            }
        ]
    },
}

result = sdk.order().create(cit_order)
cit_response = result["response"]
print("CIT order:", cit_response.get("id"), "→", cit_response.get("status"))

# Capture the payment id to reference it in the subsequent MIT charges.
cit_payment_id = (
    cit_response.get("transactions", {})
    .get("payments", [{}])[0]
    .get("id", "")
)


# ── 2. MIT – Scheduled recurring charge ───────────────────────────────────────
# The merchant triggers the monthly charge without cardholder interaction.
# The ``reference.id`` links this payment to the original CIT authorisation.

mit_order = {
    "type": "online",
    "total_amount": "100.00",
    "external_reference": "cof-subscription-001-mit-month-2",
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
                    # No card token needed — the credential is already stored.
                    "installments": 1,
                },
                "transaction_data": {
                    "type": "CREDENTIAL_ON_FILE",
                    "sub_type": "recurring",
                    # "stored" confirms the credential was previously persisted.
                    "storage": "stored",
                    # The merchant initiates this charge on the cardholder's behalf.
                    "transaction_initiator": "merchant",
                    "first_transaction": False,
                    # Reference the CIT payment so the network can trace the series.
                    "reference": {
                        "id": cit_payment_id,
                    },
                },
            }
        ]
    },
}

result = sdk.order().create(mit_order)
mit_response = result["response"]
print("MIT order:", mit_response.get("id"), "→", mit_response.get("status"))


# ── 3. UCOF-CIT – Unscheduled Card-On-File, Customer-Initiated ────────────────
# The cardholder returns to the site and pays with their stored card in a
# one-off, unplanned transaction (e.g. top-up, on-demand purchase).

ucof_cit_order = {
    "type": "online",
    "total_amount": "49.90",
    "external_reference": "cof-ucof-cit-purchase-001",
    "payer": {
        "email": "customer@example.com",
        "customer_id": "CUSTOMER_ID",
    },
    "transactions": {
        "payments": [
            {
                "amount": "49.90",
                "payment_method": {
                    "id": "master",
                    "type": "credit_card",
                    "installments": 1,
                },
                "transaction_data": {
                    "type": "CREDENTIAL_ON_FILE",
                    # "unscheduled" distinguishes this from a planned recurring charge.
                    "sub_type": "unscheduled",
                    # The credential was already stored from the original CIT.
                    "storage": "stored",
                    # The cardholder is present and actively initiates this purchase.
                    "transaction_initiator": "customer",
                    "first_transaction": False,
                },
            }
        ]
    },
}

result = sdk.order().create(ucof_cit_order)
ucof_response = result["response"]
print("UCOF-CIT order:", ucof_response.get("id"), "→", ucof_response.get("status"))
