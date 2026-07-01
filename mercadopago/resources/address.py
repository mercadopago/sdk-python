"""Address resource for MercadoPago SDK."""

from typing import Optional
from mercadopago.resources.base import Resource


class Address(Resource):
    """Address model with location information.
    
    This model represents a physical address with various location components.
    All fields are optional to allow for flexible address representations.
    """
    
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
        """Initialize an Address instance.
        
        Args:
            city: The city name
            country: The country name or code
            state: The state or province name
            street_name: The name of the street
            street_number: The street number or building identifier
            zip_code: The postal or ZIP code
            **kwargs: Additional optional parameters
        """
        super().__init__(**kwargs)
        self.city = city
        self.country = country
        self.state = state
        self.street_name = street_name
        self.street_number = street_number
        self.zip_code = zip_code
    
    def to_dict(self) -> dict:
        """Convert the Address instance to a dictionary.
        
        Returns:
            A dictionary representation of the address with non-None values
        """
        data = {}
        
        if self.city is not None:
            data['city'] = self.city
        if self.country is not None:
            data['country'] = self.country
        if self.state is not None:
            data['state'] = self.state
        if self.street_name is not None:
            data['street_name'] = self.street_name
        if self.street_number is not None:
            data['street_number'] = self.street_number
        if self.zip_code is not None:
            data['zip_code'] = self.zip_code
            
        return data
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Address':
        """Create an Address instance from a dictionary.
        
        Args:
            data: Dictionary containing address data
            
        Returns:
            An Address instance populated with the provided data
        """
        return cls(
            city=data.get('city'),
            country=data.get('country'),
            state=data.get('state'),
            street_name=data.get('street_name'),
            street_number=data.get('street_number'),
            zip_code=data.get('zip_code')
        )
    
    def __repr__(self) -> str:
        """Return a string representation of the Address.
        
        Returns:
            A string representation showing all address components
        """
        parts = []
        if self.street_name:
            parts.append(self.street_name)
        if self.street_number:
            parts.append(self.street_number)
        if self.city:
            parts.append(self.city)
        if self.state:
            parts.append(self.state)
        if self.zip_code:
            parts.append(self.zip_code)
        if self.country:
            parts.append(self.country)
        
        address_str = ', '.join(parts) if parts else 'Empty Address'
        return f"<Address({address_str})>"