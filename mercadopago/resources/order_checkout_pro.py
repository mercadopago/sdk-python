"""Dataclasses for Checkout Pro fields in order requests."""
from dataclasses import asdict, dataclass, field, is_dataclass
from typing import Any, Dict, List, Optional


def as_order_dict(value):
    """Converts dataclasses to an order payload dict without empty values.

    ``dataclasses.asdict()`` preserves ``None`` values, which can produce
    invalid API payloads for optional nested fields. This helper recursively
    removes ``None`` values and empty containers while preserving explicit
    ``False`` and ``0`` values.
    """
    if is_dataclass(value):
        value = asdict(value)

    if isinstance(value, dict):
        compact = {}
        for key, item in value.items():
            item = as_order_dict(item)
            if item is not None and item != [] and item != {}:
                compact[key] = item
        return compact

    if isinstance(value, list):
        return [
            item for item in (as_order_dict(item) for item in value)
            if item is not None and item != [] and item != {}
        ]

    return value


@dataclass
class OrderCheckoutProTrack:
    """Tracking pixel configuration for Checkout Pro orders.

    Attributes:
        type: Tracking pixel type, for example ``"google_ad"`` or
            ``"facebook_ad"``. Type: str.
        values: Pixel-specific values, such as ``conversion_id``,
            ``conversion_label``, or ``pixel_id``. Type: dict.
    """

    type: Optional[str] = None
    values: Optional[Dict[str, Any]] = None


@dataclass
class OrderCheckoutProOnlineConfig:
    """Checkout Pro redirect and availability configuration.

    Use this dataclass to build the ``config.online`` payload when creating an
    order for Checkout Pro. Convert to dict with ``as_order_dict()`` to omit
    empty values.

    Attributes:
        available_from: ISO 8601 date from which the order can be paid.
            Type: str.
        allowed_user_type: Restricts who can pay, for example
            ``"account_only"``. Type: str.
        success_url: Redirect URL after an approved payment. Type: str.
        failure_url: Redirect URL after a rejected or cancelled payment.
            Type: str.
        pending_url: Redirect URL when payment remains pending. Type: str.
        auto_return: Automatic redirect behavior, for example ``"approved"``
            or ``"all"``. Type: str.
        tracks: Tracking pixel configuration list.
    """

    available_from: Optional[str] = None
    allowed_user_type: Optional[str] = None
    success_url: Optional[str] = None
    failure_url: Optional[str] = None
    pending_url: Optional[str] = None
    auto_return: Optional[str] = None
    tracks: List[OrderCheckoutProTrack] = field(default_factory=list)


@dataclass
class OrderCheckoutProInterestFree:
    """Interest-free installment configuration for Checkout Pro orders.

    Attributes:
        type: Configuration type, for example ``"range"``, ``"list"``, or
            ``"none"``. Type: str.
        values: Installment range or list. Type: list[int].
    """

    type: Optional[str] = None
    values: List[int] = field(default_factory=list)


@dataclass
class OrderCheckoutProInstallments:
    """Installment rules for Checkout Pro payment methods.

    Attributes:
        interest_free: Interest-free installment configuration.
    """

    interest_free: Optional[OrderCheckoutProInterestFree] = None


@dataclass
class OrderCheckoutProPaymentMethod:
    """Payment method constraints for Checkout Pro orders.

    Use this dataclass to build the ``config.payment_method`` payload when
    creating an order for Checkout Pro. Convert to dict with
    ``as_order_dict()`` to omit empty values.

    Attributes:
        max_installments: Maximum installments accepted. Type: int.
        not_allowed_ids: Payment method IDs to block, such as card brands.
            Type: list[str].
        not_allowed_types: Payment method types to block. Type: list[str].
        installments: Installment rules.
    """

    max_installments: Optional[int] = None
    not_allowed_ids: List[str] = field(default_factory=list)
    not_allowed_types: List[str] = field(default_factory=list)
    installments: Optional[OrderCheckoutProInstallments] = None


@dataclass
class OrderCheckoutProConfig:
    """Checkout Pro order configuration.

    Use this dataclass to build the root ``config`` payload when creating an
    order for Checkout Pro. Convert to dict with ``as_order_dict()`` to omit
    empty values.

    Attributes:
        statement_descriptor: Text shown on the buyer's card statement.
            Type: str.
        default_payment_due_date: Offline payment expiration duration in ISO
            8601 format. Type: str.
        online: Checkout Pro redirect and availability configuration.
        payment_method: Checkout Pro payment method constraints.
    """

    statement_descriptor: Optional[str] = None
    default_payment_due_date: Optional[str] = None
    online: Optional[OrderCheckoutProOnlineConfig] = None
    payment_method: Optional[OrderCheckoutProPaymentMethod] = None
