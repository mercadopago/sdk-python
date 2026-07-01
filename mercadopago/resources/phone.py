"""Phone resource for MercadoPago SDK."""

from typing import Optional
from mercadopago.resources.base import Resource


class Phone(Resource):
    """Phone model representing a phone number with area code.
    
    Attributes:
        area_code: Optional area code of the phone number
        number: Optional phone number
    """
    
    def __init__(
        self,
        area_code: Optional[str] = None,
        number: Optional[str] = None,
        **kwargs
    ):
        """Initialize Phone instance.
        
        Args:
            area_code: Area code of the phone number
            number: Phone number
            **kwargs: Additional attributes
        """
        self.area_code = area_code
        self.number = number
        super().__init__(**kwargs)
    
    def to_dict(self) -> dict:
        """Convert Phone instance to dictionary.
        
        Returns:
            Dictionary representation of the phone
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
            data: Dictionary containing phone data
            
        Returns:
            Phone instance
        """
        if not data:
            return None
        return cls(
            area_code=data.get('area_code'),
            number=data.get('number')
        )