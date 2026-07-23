"""Dataclasses for payer contact data in order requests."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class OrderPayerPhone:
    """Payer phone number for an order request.

    Use this dataclass to build the ``payer.phone`` payload. Convert to dict with
    ``dataclasses.asdict()`` (``None`` fields are filtered out before sending).

    Attributes:
        area_code: Phone area code. Type: str.
        number: Phone number without the area code. Type: str.
    """

    area_code: Optional[str] = None
    number: Optional[str] = None


@dataclass
class OrderPayerAddress:
    """Payer address for an order request.

    Use this dataclass to build the ``payer.address`` payload. Convert to dict with
    ``dataclasses.asdict()`` (``None`` fields are filtered out before sending).

    Attributes:
        zip_code: Postal / ZIP code. Type: str.
        street_name: Name of the street. Type: str.
        street_number: Street number. Type: str.
        neighborhood: Neighborhood name. Type: str.
        city: City name. Type: str.
        state: State or province. Type: str.
        complement: Additional address details. Type: str.
        country: Country name or code. Type: str.
    """

    zip_code: Optional[str] = None
    street_name: Optional[str] = None
    street_number: Optional[str] = None
    neighborhood: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    complement: Optional[str] = None
    country: Optional[str] = None
