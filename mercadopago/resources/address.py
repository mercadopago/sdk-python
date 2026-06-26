"""
Address resource for MercadoPago SDK.

This module contains the Address model with properties for representing
physical addresses.
"""

from mercadopago.resources.base import ResourceBase


class Address(ResourceBase):
    """
    Address resource model.
    
    Represents a physical address with properties for city, country, state,
    street name, street number, and zip code.
    """
    
    _schema = {
        "city": str,
        "country": str,
        "state": str,
        "street_name": str,
        "street_number": str,
        "zip_code": str,
    }
    
    def __init__(self, data=None):
        """
        Initialize an Address instance.
        
        Args:
            data (dict, optional): Dictionary containing address data.
        """
        super(Address, self).__init__(data)
        
        self.city = None
        self.country = None
        self.state = None
        self.street_name = None
        self.street_number = None
        self.zip_code = None
        
        if data:
            self._load_from_dict(data)
    
    def _load_from_dict(self, data):
        """
        Load address properties from a dictionary.
        
        Args:
            data (dict): Dictionary containing address data.
        """
        if not isinstance(data, dict):
            return
        
        self.city = data.get("city")
        self.country = data.get("country")
        self.state = data.get("state")
        self.street_name = data.get("street_name")
        self.street_number = data.get("street_number")
        self.zip_code = data.get("zip_code")
    
    def to_dict(self):
        """
        Convert the Address instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the address.
        """
        result = {}
        
        if self.city is not None:
            result["city"] = self.city
        if self.country is not None:
            result["country"] = self.country
        if self.state is not None:
            result["state"] = self.state
        if self.street_name is not None:
            result["street_name"] = self.street_name
        if self.street_number is not None:
            result["street_number"] = self.street_number
        if self.zip_code is not None:
            result["zip_code"] = self.zip_code
        
        return result
    
    def __repr__(self):
        """
        Return a string representation of the Address instance.
        
        Returns:
            str: String representation of the address.
        """
        return (
            f"Address(city={self.city!r}, country={self.country!r}, "
            f"state={self.state!r}, street_name={self.street_name!r}, "
            f"street_number={self.street_number!r}, zip_code={self.zip_code!r})"
        )