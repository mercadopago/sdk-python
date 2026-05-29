"""Dataclass for automatic/recurring payment scheduling in order requests."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class OrderAutomaticPayments:
    """Configuration for automatic (recurring) payment scheduling within an order.

    Use this dataclass to build the ``automatic_payments`` payload when creating
    an order with Automatic Payments. Convert to dict with ``dataclasses.asdict()``.

    Attributes:
        payment_profile_id: Identifier of the stored payment profile used for
            automatic charges. Type: str.
        retries: Maximum number of retry attempts if the automatic charge fails.
            Type: int.
        schedule_date: ISO 8601 date when the automatic payment is scheduled to
            be charged (e.g. ``"2026-06-01T00:00:00.000-04:00"``). Type: str.
        due_date: ISO 8601 date by which the payment must be completed before it
            is considered overdue. Type: str.
    """

    payment_profile_id: Optional[str] = None
    retries: Optional[int] = None
    schedule_date: Optional[str] = None
    due_date: Optional[str] = None
