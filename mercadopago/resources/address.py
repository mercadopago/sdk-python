"""Address resource for MercadoPago SDK."""

from typing import Optional
from ..core import MPBase


class Address(MPBase):
    """
    Address model representing a physical address.
    
    All fields are optional strings.
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
        """
        Initialize an Address instance.
        
        Args:
            city: The city name
            country: The country name or code
            state: The state or province name
            street_name: The street name
            street_number: The street number
            zip_code: The postal/ZIP code
            **kwargs: Additional optional parameters
        """
        self.city = city
        self.country = country
        self.state = state
        self.street_name = street_name
        self.street_number = street_number
        self.zip_code = zip_code
        super().__init__(**kwargs)
    
    def to_dict(self) -> dict:
        """
        Convert the Address instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the address
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
        """
        Create an Address instance from a dictionary.
        
        Args:
            data: Dictionary containing address data
            
        Returns:
            Address: New Address instance
        """
        return cls(
            city=data.get('city'),
            country=data.get('country'),
            state=data.get('state'),
            street_name=data.get('street_name'),
            street_number=data.get('street_number'),
            zip_code=data.get('zip_code')
        )