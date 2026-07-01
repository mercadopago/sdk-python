"""Phone resource for MercadoPago SDK."""

from typing import Optional
from ..core.base import MPBase


class Phone(MPBase):
    """Phone model for MercadoPago SDK.
    
    Represents a phone number with optional area code and number.
    
    Attributes:
        area_code: Optional area code for the phone number
        number: Optional phone number
    """
    
    area_code: Optional[str] = None
    number: Optional[str] = None
    
    def __init__(
        self,
        area_code: Optional[str] = None,
        number: Optional[str] = None,
        **kwargs
    ):
        """Initialize Phone instance.
        
        Args:
            area_code: Optional area code for the phone number
            number: Optional phone number
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.area_code = area_code
        self.number = number