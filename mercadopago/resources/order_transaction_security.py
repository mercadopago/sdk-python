"""Dataclass for transaction security data in order requests."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class OrderTransactionSecurity:
    """Transaction security settings for an order request.

    Nested under ``config.online.transaction_security`` (not at the request root).
    Convert to dict with ``dataclasses.asdict()`` (``None`` fields are filtered
    out before sending, per the omit-empty behavior of the API).

    Attributes:
        validation: Validation strategy applied to the transaction (e.g.
            ``"complete"``). Type: str.
        liability_shift: Liability shift indicator for 3-D Secure flows. Type: str.
    """

    validation: Optional[str] = None
    liability_shift: Optional[str] = None
