"""Dataclass for stored credential (card-on-file) data in automatic payment flows."""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OrderStoredCredential:
    """Stored credential configuration for recurring payments (card-on-file).

    Use this dataclass to build the ``stored_credential`` payload when creating
    an order with Automatic Payments. Convert to dict with ``dataclasses.asdict()``.

    Attributes:
        payment_initiator: Who initiated the payment: ``"cardholder"`` or ``"merchant"``.
            Type: str.
        reason: Reason for using the stored credential.
            One of ``"recurring"``, ``"installment"``, ``"unscheduled"``. Type: str.
        store_payment_method: Whether to save the payment method for future charges.
            Type: bool.
        first_payment: ``True`` for the initial authorization; ``False`` for
            subsequent recurring charges. Type: bool.
        prev_transaction_ref: Identifier of the previous transaction in the recurring
            series. Required from the second charge onwards to link this payment to the
            original card-network authorization. Type: str.
    """

    payment_initiator: Optional[str] = None
    reason: Optional[str] = None
    store_payment_method: Optional[bool] = None
    first_payment: Optional[bool] = None
    prev_transaction_ref: Optional[str] = None
