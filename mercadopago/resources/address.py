"""Address resource for MercadoPago SDK."""

from typing import Optional
from mercadopago.resources.base import Resource


class Address(Resource):
    """Address model for MercadoPago.
    
    Represents a physical address with city, country, state, street information,
    and zip code.
    """

    def __init__(
        self,
        city: Optional[str] = None,
        country: Optional[str] = None,
        state: Optional[str] = None,
        street_name: Optional[str] = None,
        street_number: Optional[str] = None,
        zip_code: Optional[str] = None,
    ):
        """Initialize an Address instance.
        
        Args:
            city: City name
            country: Country name or code
            state: State or province name
            street_name: Street name
            street_number: Street number
            zip_code: Postal/ZIP code
        """
        self.city = city
        self.country = country
        self.state = state
        self.street_name = street_name
        self.street_number = street_number
        self.zip_code = zip_code

    def to_dict(self) -> dict:
        """Convert Address instance to dictionary.
        
        Returns:
            Dictionary representation of the address, excluding None values
        """
        data = {}
        
        if self.city is not None:
            data["city"] = self.city
        if self.country is not None:
            data["country"] = self.country
        if self.state is not None:
            data["state"] = self.state
        if self.street_name is not None:
            data["street_name"] = self.street_name
        if self.street_number is not None:
            data["street_number"] = self.street_number
        if self.zip_code is not None:
            data["zip_code"] = self.zip_code
            
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Address":
        """Create an Address instance from a dictionary.
        
        Args:
            data: Dictionary containing address data
            
        Returns:
            Address instance
        """
        return cls(
            city=data.get("city"),
            country=data.get("country"),
            state=data.get("state"),
            street_name=data.get("street_name"),
            street_number=data.get("street_number"),
            zip_code=data.get("zip_code"),
        )

    def __repr__(self) -> str:
        """Return string representation of Address."""
        return (
            f"Address(city={self.city!r}, country={self.country!r}, "
            f"state={self.state!r}, street_name={self.street_name!r}, "
            f"street_number={self.street_number!r}, zip_code={self.zip_code!r})"
        )

    def __eq__(self, other) -> bool:
        """Check equality with another Address instance."""
        if not isinstance(other, Address):
            return False
        return (
            self.city == other.city
            and self.country == other.country
            and self.state == other.state
            and self.street_name == other.street_name
            and self.street_number == other.street_number
            and self.zip_code == other.zip_code
        )