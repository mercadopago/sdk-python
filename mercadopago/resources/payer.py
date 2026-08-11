"""Dataclasses for payer data in API requests."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class PayerPhone:
    """Payer phone number.

    Attributes:
        area_code: Phone area code. Type: str.
        number: Phone number without the area code. Type: str.
    """

    area_code: Optional[str] = None
    number: Optional[str] = None


# pylint: disable=too-many-instance-attributes  # DTO: fields mirror the API payer.address contract
@dataclass
class PayerAddress:
    """Payer address.

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


@dataclass
class PayerIdentification:
    """Payer identification document.

    Attributes:
        type: Identification document type (e.g. ``"CPF"``). Type: str.
        number: Identification document number. Type: str.
    """

    type: Optional[str] = None
    number: Optional[str] = None


# pylint: disable=too-many-instance-attributes  # DTO: fields mirror the API payer contract
@dataclass
class PayerRequest:
    """Payer information for an API request.

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
    identification: Optional[PayerIdentification] = None
    phone: Optional[PayerPhone] = None
    address: Optional[PayerAddress] = None
