"""Dataclass for line items in order requests."""
from dataclasses import dataclass
from typing import Optional


# pylint: disable=too-many-instance-attributes  # DTO: fields mirror the Orders API items contract
@dataclass
class OrderItemRequest:
    """A single line item within an order request.

    Use this dataclass to build an entry of the ``items`` array when creating
    an order. Convert to dict with ``dataclasses.asdict()`` (``None`` fields are
    filtered out before sending, per the omit-empty behavior of the API).

    Attributes:
        title: Display name of the item. Type: str.
        type: Item type/category classifier. Type: str.
        warranty: Whether the item includes a warranty. Type: bool.
        event_date: ISO 8601 date associated with the item (e.g. event tickets).
            Type: str.
        unit_price: Price per unit as a decimal string (e.g. ``"100.00"``).
            Type: str.
        external_code: Merchant-side external identifier for the item. Type: str.
        category_id: MercadoPago category identifier. Type: str.
        description: Free-text description of the item. Type: str.
        picture_url: URL of an image representing the item. Type: str.
        quantity: Number of units. Type: int.
    """

    title: Optional[str] = None
    type: Optional[str] = None
    warranty: Optional[bool] = None
    event_date: Optional[str] = None
    unit_price: Optional[str] = None
    external_code: Optional[str] = None
    category_id: Optional[str] = None
    description: Optional[str] = None
    picture_url: Optional[str] = None
    quantity: Optional[int] = None
