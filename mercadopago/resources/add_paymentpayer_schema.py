# mercadopago/resources/add_paymentpayer_schema.py

"""
PaymentPayer schema definition for MercadoPago SDK.

This module defines the PaymentPayer model used in payment processing.
"""

from typing import Optional, Literal
from pydantic import BaseModel, Field, EmailStr


class Identification(BaseModel):
    """
    Identification information for a payer.
    
    Attributes:
        type: Type of identification document (e.g., 'DNI', 'CPF', 'CUIT')
        number: Identification document number
    """
    type: Optional[str] = Field(None, description="Type of identification document")
    number: Optional[str] = Field(None, description="Identification document number")


class PaymentPayer(BaseModel):
    """
    Payment payer information.
    
    This model represents the payer details in a payment transaction.
    
    Attributes:
        email: Payer's email address (required)
        id: Unique identifier for the payer
        identification: Payer's identification details
        type: Type of payer (customer, registered, or guest)
    """
    email: EmailStr = Field(..., description="Payer's email address")
    id: Optional[str] = Field(None, description="Unique identifier for the payer")
    identification: Optional[Identification] = Field(
        None, 
        description="Payer's identification details"
    )
    type: Optional[Literal["customer", "registered", "guest"]] = Field(
        None, 
        description="Type of payer"
    )

    class Config:
        """Pydantic model configuration."""
        json_schema_extra = {
            "example": {
                "email": "payer@example.com",
                "id": "123456",
                "identification": {
                    "type": "DNI",
                    "number": "12345678"
                },
                "type": "customer"
            }
        }


__all__ = ["PaymentPayer", "Identification"]