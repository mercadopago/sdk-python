# resources/address.py

```python
"""
Address resource for MercadoPago SDK.

This module defines the Address schema used across different MercadoPago entities
like customers, payment methods, and shipping information.
"""

from mercadopago.core import MPBase


class Address(MPBase):
    """
    Address model representing physical address information.
    
    Attributes:
        city (str): City name
        country (str): Country name or code
        state (str): State or province name
        street_name (str): Street name
        street_number (str): Street number
        zip_code (str): ZIP or postal code
    """
    
    def __init__(self, client):
        """
        Initialize Address resource.
        
        Args:
            client: MercadoPago client instance
        """
        super().__init__(client)
        self._schema = {
            "city": str,
            "country": str,
            "state": str,
            "street_name": str,
            "street_number": str,
            "zip_code": str
        }
    
    @property
    def city(self):
        """Get city."""
        return self._data.get("city")
    
    @city.setter
    def city(self, value):
        """Set city."""
        self._data["city"] = value
    
    @property
    def country(self):
        """Get country."""
        return self._data.get("country")
    
    @country.setter
    def country(self, value):
        """Set country."""
        self._data["country"] = value
    
    @property
    def state(self):
        """Get state."""
        return self._data.get("state")
    
    @state.setter
    def state(self, value):
        """Set state."""
        self._data["state"] = value
    
    @property
    def street_name(self):
        """Get street name."""
        return self._data.get("street_name")
    
    @street_name.setter
    def street_name(self, value):
        """Set street name."""
        self._data["street_name"] = value
    
    @property
    def street_number(self):
        """Get street number."""
        return self._data.get("street_number")
    
    @street_number.setter
    def street_number(self, value):
        """Set street number."""
        self._data["street_number"] = value
    
    @property
    def zip_code(self):
        """Get ZIP code."""
        return self._data.get("zip_code")
    
    @zip_code.setter
    def zip_code(self, value):
        """Set ZIP code."""
        self._data["zip_code"] = value
    
    def to_dict(self):
        """
        Convert Address to dictionary representation.
        
        Returns:
            dict: Dictionary with address data
        """
        return {
            "city": self.city,
            "country": self.country,
            "state": self.state,
            "street_name": self.street_name,
            "street_number": self.street_number,
            "zip_code": self.zip_code
        }
    
    @classmethod
    def from_dict(cls, client, data):
        """
        Create Address instance from dictionary.
        
        Args:
            client: MercadoPago client instance
            data (dict): Dictionary with address data
            
        Returns:
            Address: New Address instance
        """
        address = cls(client)
        if data:
            address.city = data.get("city")
            address.country = data.get("country")
            address.state = data.get("state")
            address.street_name = data.get("street_name")
            address.street_number = data.get("street_number")
            address.zip_code = data.get("zip_code")
        return address
    
    def __repr__(self):
        """String representation of Address."""
        return f"<Address {self.street_name} {self.street_number}, {self.city}, {self.state} {self.zip_code}, {self.country}>"

```