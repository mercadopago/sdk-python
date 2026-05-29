"""Dataclass for subscription billing data in automatic payment order requests."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class OrderSubscriptionSequence:
    """Position of a payment within a subscription series.

    Attributes:
        number: Current payment number in the subscription (1-based). Type: int.
        total: Total number of payments expected in the plan. Type: int.
    """

    number: Optional[int] = None
    total: Optional[int] = None


@dataclass
class OrderInvoicePeriod:
    """Billing period covered by a subscription invoice.

    Attributes:
        type: Period unit (e.g. ``"monthly"``, ``"daily"``, ``"yearly"``). Type: str.
        period: Number of period units covered by this invoice. Type: int.
    """

    type: Optional[str] = None
    period: Optional[int] = None


@dataclass
class OrderSubscriptionData:
    """Subscription billing information for a payment within an order.

    Use this dataclass to build the ``subscription_data`` payload when creating
    an order with Automatic Payments. Convert to dict with ``dataclasses.asdict()``.

    Attributes:
        invoice_id: Identifier of the invoice being settled by this payment.
            Type: str.
        billing_date: ISO 8601 date when the subscription billing was triggered.
            Type: str.
        subscription_sequence: Position of this payment in the subscription series.
        invoice_period: Billing period covered by this invoice.
    """

    invoice_id: Optional[str] = None
    billing_date: Optional[str] = None
    subscription_sequence: Optional[OrderSubscriptionSequence] = None
    invoice_period: Optional[OrderInvoicePeriod] = None
