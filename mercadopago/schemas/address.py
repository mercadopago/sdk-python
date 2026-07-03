"""Address schema for MercadoPago API requests.

Defines the Address model with required fields for street, city, country,
state, and postal_code.
"""
from dataclasses import dataclass


@dataclass
class Address:
    """Address model with required location fields.

    Use this dataclass to build address payloads for MercadoPago API requests.
    Convert to dict with ``dataclasses.asdict()``.

    Attributes:
        street: Street name and number. Type: str, required.
        city: City name. Type: str, required.
        country: Country name or code. Type: str, required.
        state: State or province name. Type: str, required.
        postal_code: Postal or ZIP code. Type: str, required.
    """

    street: str
    city: str
    country: str
    state: str
    postal_code: str