"""Dataclasses for shipment data in API requests."""
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    List,
    Optional,
)


# pylint: disable=too-many-instance-attributes  # DTO: fields mirror the API shipment.address contract
@dataclass
class ShipmentAddress:
    """Delivery address for a shipment.

    Attributes:
        street_name: Name of the street. Type: str.
        street_number: Street number. Type: str.
        zip_code: Postal / ZIP code. Type: str.
        floor: Floor within the building. Type: str.
        apartment: Apartment / unit identifier. Type: str.
        neighborhood: Neighborhood name. Type: str.
        state: State or province. Type: str.
        city: City name. Type: str.
        complement: Additional address details. Type: str.
    """

    street_name: Optional[str] = None
    street_number: Optional[str] = None
    zip_code: Optional[str] = None
    floor: Optional[str] = None
    apartment: Optional[str] = None
    neighborhood: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    complement: Optional[str] = None


@dataclass
class ShipmentFreeMethod:
    """A free-shipping method.

    Attributes:
        id: Identifier of the free shipping method. Type: int.
    """

    id: Optional[int] = None


@dataclass
class ShipmentRequest:
    """Shipment configuration for an API request.

    Use this dataclass to build the ``shipment`` payload when creating an order.
    Convert to dict with ``dataclasses.asdict()`` (``None`` fields are filtered
    out before sending, per the omit-empty behavior of the API).

    Attributes:
        mode: Shipping mode (e.g. ``"me2"``, ``"custom"``). Type: str.
        local_pickup: Whether the buyer picks up the item locally. Type: bool.
        cost: Shipping cost as a decimal string. Type: str.
        free_shipping: Whether shipping is free. Type: bool.
        free_methods: Free shipping methods available.
        address: Delivery address for the shipment.
    """

    mode: Optional[str] = None
    local_pickup: Optional[bool] = None
    cost: Optional[str] = None
    free_shipping: Optional[bool] = None
    free_methods: Optional[List[ShipmentFreeMethod]] = field(default=None)
    address: Optional[ShipmentAddress] = None
