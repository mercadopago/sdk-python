"""Address dataclass for the MercadoPago Python SDK.

Defines a reusable Address model used in payer, shipment, and other API
request and response structures.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Address:
    """Represents a physical address.

    Used in payer information, shipment details, and customer records.

    Attributes:
        zip_code: Postal or ZIP code (e.g. ``"01310-100"``). Type: str.
        street_name: Street or avenue name (e.g. ``"Av. Paulista"``). Type: str.
        street_number: Street number (e.g. ``"1000"``). Type: str.
        neighborhood: Neighborhood or district name. Type: str.
        city: City name. Type: str.
        federal_unit: State or province code (e.g. ``"SP"``, ``"RJ"``). Type: str.
        floor: Floor number in a building. Type: str.
        apartment: Apartment or unit number. Type: str.
    """

    zip_code: Optional[str] = None
    street_name: Optional[str] = None
    street_number: Optional[str] = None
    neighborhood: Optional[str] = None
    city: Optional[str] = None
    federal_unit: Optional[str] = None
    floor: Optional[str] = None
    apartment: Optional[str] = None