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
)

from mercadopago.resources.order_item import OrderItemRequest
from mercadopago.resources.order_integration_data import OrderIntegrationData
from mercadopago.resources.order_payer import (
    OrderPayerAddress,
    OrderPayerPhone,
)
from mercadopago.resources.order_shipment import OrderShipmentRequest


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


@dataclass
class OrderIdentification:
    """Payer identification document for an order request.

    Attributes:
        type: Identification document type (e.g. ``"CPF"``). Type: str.
        number: Identification document number. Type: str.
    """

    type: Optional[str] = None
    number: Optional[str] = None


# pylint: disable=too-many-instance-attributes  # DTO: fields mirror the Orders API payer contract
@dataclass
class OrderPayerRequest:
    """Payer information for an order request.

    Attributes:
        email: Payer email address. Type: str.
        first_name: Payer first name. Type: str.
        last_name: Payer last name. Type: str.
        customer_id: Stored customer identifier. Type: str.
        entity_type: Payer entity type (``"individual"`` | ``"association"``).
            Type: str.
        identification: Payer identification document.
        phone: Payer phone number.
        address: Payer address.
    """

    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    customer_id: Optional[str] = None
    entity_type: Optional[str] = None
    identification: Optional[OrderIdentification] = None
    phone: Optional[OrderPayerPhone] = None
    address: Optional[OrderPayerAddress] = None


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
        transactions: Transactions payload (payments).
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
    transactions: Optional[dict] = None
    payer: Optional[OrderPayerRequest] = None
    items: Optional[List[OrderItemRequest]] = field(default=None)
    config: Optional[dict] = None
    shipment: Optional[OrderShipmentRequest] = None
    integration_data: Optional[OrderIntegrationData] = None
    additional_info: Optional[dict] = None
