# mercadopago/resources/add_phone_schema.py

from typing import Optional
from pydantic import BaseModel


class Phone(BaseModel):
    """
    Phone model representing a phone number with optional area code and number.
    
    Attributes:
        area_code: Optional area code for the phone number
        number: Optional phone number
    """
    area_code: Optional[str] = None
    number: Optional[str] = None