"""Address resource model."""

from typing import Optional
from mercadopago.resources.base import ResourceModel


class Address(ResourceModel):
    """Address model representing a physical address.
    
    Attributes:
        city: City name
        country: Country name or code
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
    
    def __init__(
        self,
        city: Optional[str] = None,
        country: Optional[str] = None,
        state: Optional[str] = None,
        street_name: Optional[str] = None,
        street_number: Optional[str] = None,
        zip_code: Optional[str] = None,
        **kwargs
    ):
        """Initialize Address instance.
        
        Args:
            city: City name
            country: Country name or code
            state: State or province name
            street_name: Street name
            street_number: Street number
            zip_code: Postal/ZIP code
            **kwargs: Additional keyword arguments
        """
        self.city = city
        self.country = country
        self.state = state
        self.street_name = street_name
        self.street_number = street_number
        self.zip_code = zip_code
        super().__init__(**kwargs)