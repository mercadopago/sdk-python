"""Root request dataclasses for the MercadoPago Orders API.

These dataclasses model the ``POST /v1/orders`` request body. They are an
optional, typed alternative to passing a plain ``dict`` to
:meth:`~mercadopago.resources.order.Order.create`. Build the request with the
dataclasses and convert it to a ``dict`` with ``dataclasses.asdict()``; ``None``
fields are filtered out before serialization so the resulting JSON matches the
dict path exactly.

The dict path continues to work unchanged; these dataclasses are purely additive.
"""
from dataclasses import (
    asdict,
    dataclass,
    field,
    is_dataclass,
)
from typing import (
    List,
    Optional,
    Union,
)

from mercadopago.resources.item import ItemRequest
from mercadopago.resources.order_integration_data import OrderIntegrationData
from mercadopago.resources.order_transaction import OrderTransactionRequest
from mercadopago.resources.payer import PayerRequest
from mercadopago.resources.shipment import ShipmentRequest


def _filter_none(value):
    """Recursively drop ``None`` values from dicts/lists (DD-3, omit-empty)."""
    if isinstance(value, dict):
        return {k: _filter_none(v) for k, v in value.items() if v is not None}
    if isinstance(value, list):
        return [_filter_none(v) for v in value]
    return value


def order_request_to_dict(request):
    """Convert a request dataclass into a ``dict`` with ``None`` fields omitted.

    This is the canonical way to turn any of the Orders API request dataclasses
    (``OrderCreateRequest`` and its nested objects) into the ``dict`` accepted by
    :meth:`~mercadopago.resources.order.Order.create`. It runs
    ``dataclasses.asdict()`` and then recursively strips keys whose value is
    ``None`` so the resulting JSON matches the plain-dict path exactly (DD-3).

    Args:
        request: A request dataclass instance (or any dataclass instance).

    Returns:
        dict: The request as a plain ``dict`` with ``None`` fields removed.

    Raises:
        TypeError: If *request* is not a dataclass instance.
    """
    if not is_dataclass(request) or isinstance(request, type):
        raise TypeError("request must be a dataclass instance")
    return _filter_none(asdict(request))


# pylint: disable=too-many-instance-attributes  # DTO: fields mirror the Orders API root request contract
@dataclass
class OrderCreateRequest:
    """Root request body for creating an order.

    Optional typed alternative to a plain ``dict``. Convert with
    ``dataclasses.asdict()``; ``None`` fields are filtered out before sending.

    Attributes:
        type: Order type (e.g. ``"online"``). Type: str.
        external_reference: Merchant-side reference for the order. Type: str.
        total_amount: Total order amount as a decimal string. Type: str.
        currency: Currency identifier (e.g. ``"BRL"``). Type: str.
        capture_mode: Capture mode (e.g. ``"automatic_async"``). Type: str.
        processing_mode: Processing mode (e.g. ``"automatic"``). Type: str.
        description: Free-text order description. Type: str.
        marketplace: Marketplace identifier. Type: str.
        marketplace_fee: Marketplace fee as a decimal string. Type: str.
        expiration_time: Order expiration time (ISO 8601 / duration). Type: str.
        checkout_available_at: When the checkout becomes available. Type: str.
        transactions: Typed transactions payload. Accepts an
            :class:`~mercadopago.resources.order_transaction.OrderTransactionRequest`
            for a fully typed AP chain, or a plain ``dict`` for backward
            compatibility.
        payer: Payer information.
        items: Line items in the order.
        config: Order configuration payload.
        shipment: Shipment configuration.
        integration_data: Integration metadata.
        additional_info: Free-form additional information (kept as-is).
    """

    type: Optional[str] = None
    external_reference: Optional[str] = None
    total_amount: Optional[str] = None
    currency: Optional[str] = None
    capture_mode: Optional[str] = None
    processing_mode: Optional[str] = None
    description: Optional[str] = None
    marketplace: Optional[str] = None
    marketplace_fee: Optional[str] = None
    expiration_time: Optional[str] = None
    checkout_available_at: Optional[str] = None
    transactions: Optional[Union[OrderTransactionRequest, dict]] = None
    payer: Optional[PayerRequest] = None
    items: Optional[List[ItemRequest]] = field(default=None)
    config: Optional[dict] = None
    shipment: Optional[ShipmentRequest] = None
    integration_data: Optional[OrderIntegrationData] = None
    additional_info: Optional[dict] = None
