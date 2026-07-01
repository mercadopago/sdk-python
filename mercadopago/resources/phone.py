"""Phone resource for MercadoPago SDK."""

from typing import Optional
from mercadopago.resources.base import ResourceBase


class Phone(ResourceBase):
    """Phone resource model.
    
    Represents a phone number with area code and number components.
    """
    
    area_code: Optional[str] = None
    number: Optional[str] = None
    
    def __init__(self, area_code: Optional[str] = None, number: Optional[str] = None):
        """Initialize Phone resource.
        
        Args:
            area_code: Optional area code for the phone number
            number: Optional phone number
        """
        self.area_code = area_code
        self.number = number