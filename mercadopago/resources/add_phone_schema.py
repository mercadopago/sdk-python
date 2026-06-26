# mercadopago/resources/add_phone_schema.py

from typing import Optional
from pydantic import BaseModel, Field


class Phone(BaseModel):
    """
    Phone model for MercadoPago API.
    
    Attributes:
        area_code: Optional area code for the phone number
        number: Optional phone number
    """
    area_code: Optional[str] = Field(None, description="Area code for the phone number")
    number: Optional[str] = Field(None, description="Phone number")

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
        str_strip_whitespace = True