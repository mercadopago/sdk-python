"""Address resource model."""

from typing import Optional
from mercadopago.resources.base import Resource


class Address(Resource):
    """Address model with location details.
    
    Attributes:
        city: City name
        country: Country name
        state: State or province name
        street_name: Street name
        street_number: Street number
        zip_code: Postal/ZIP code
    """
    
    city: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    street_name: Optional[str] = None
    street_number: Optional[str] = None
    zip_code: Optional[str] = None