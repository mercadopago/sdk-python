"""Phone resource model for MercadoPago SDK."""

from typing import Optional
from mercadopago.resources.base import Resource


class Phone(Resource):
    """
    Phone model representing a phone number.
    
    Attributes:
        area_code (Optional[str]): The area code of the phone number.
        number (Optional[str]): The phone number.
    """
    
    def __init__(
        self,
        area_code: Optional[str] = None,
        number: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize a Phone instance.
        
        Args:
            area_code (Optional[str]): The area code of the phone number.
            number (Optional[str]): The phone number.
            **kwargs: Additional keyword arguments.
        """
        self.area_code = area_code
        self.number = number
        super().__init__(**kwargs)
    
    def to_dict(self) -> dict:
        """
        Convert the Phone instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the phone.
        """
        data = {}
        if self.area_code is not None:
            data['area_code'] = self.area_code
        if self.number is not None:
            data['number'] = self.number
        return data
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Phone':
        """
        Create a Phone instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing phone data.
            
        Returns:
            Phone: A new Phone instance.
        """
        if data is None:
            return None
        
        return cls(
            area_code=data.get('area_code'),
            number=data.get('number')
        )