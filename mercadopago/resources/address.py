"""Address resource model for MercadoPago SDK."""

from typing import Optional
from mercadopago.resources.base import Resource


class Address(Resource):
    """Address model representing a physical address.
    
    Attributes:
        city: City name
        country: Country name or code
        state: State or province name
        street_name: Street name
        street_number: Street number
        zip_code: Postal or ZIP code
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
        """Initialize Address instance.
        
        Args:
            city: City name
            country: Country name or code
            state: State or province name
            street_name: Street name
            street_number: Street number
            zip_code: Postal or ZIP code
            **kwargs: Additional attributes
        """
        self.city = city
        self.country = country
        self.state = state
        self.street_name = street_name
        self.street_number = street_number
        self.zip_code = zip_code
        super().__init__(**kwargs)
    
    def to_dict(self) -> dict:
        """Convert Address instance to dictionary.
        
        Returns:
            Dictionary representation of the address
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
        """Create Address instance from dictionary.
        
        Args:
            data: Dictionary containing address data
            
        Returns:
            Address instance
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
        """String representation of Address.
        
        Returns:
            String representation
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