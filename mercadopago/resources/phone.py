"""Phone resource for MercadoPago SDK."""

from typing import Optional

from mercadopago.resources.base import ResourceBase


class Phone(ResourceBase):
    """Phone resource model.
    
    Represents a phone number with optional area code and number.
    
    Attributes:
        area_code (Optional[str]): The area code of the phone number.
        number (Optional[str]): The phone number.
    """

    def __init__(
        self,
        area_code: Optional[str] = None,
        number: Optional[str] = None,
    ):
        """Initialize Phone resource.
        
        Args:
            area_code (Optional[str]): The area code of the phone number.
            number (Optional[str]): The phone number.
        """
        self.area_code = area_code
        self.number = number

    def to_dict(self) -> dict:
        """Convert Phone to dictionary representation.
        
        Returns:
            dict: Dictionary representation of the Phone.
        """
        data = {}
        if self.area_code is not None:
            data['area_code'] = self.area_code
        if self.number is not None:
            data['number'] = self.number
        return data

    @classmethod
    def from_dict(cls, data: dict) -> 'Phone':
        """Create Phone instance from dictionary.
        
        Args:
            data (dict): Dictionary containing phone data.
            
        Returns:
            Phone: Phone instance created from the dictionary.
        """
        if not data:
            return cls()
        
        return cls(
            area_code=data.get('area_code'),
            number=data.get('number'),
        )

    def __repr__(self) -> str:
        """String representation of Phone.
        
        Returns:
            str: String representation.
        """
        return f"Phone(area_code={self.area_code!r}, number={self.number!r})"