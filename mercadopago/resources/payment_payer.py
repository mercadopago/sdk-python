# mercadopago/resources/payment_payer.py

"""
PaymentPayer resource schema for MercadoPago SDK.

This module defines the PaymentPayer model used to represent payer information
in payment transactions.
"""

from typing import Optional, Literal
from pydantic import BaseModel, Field, EmailStr


class PayerIdentification(BaseModel):
    """Payer identification information."""
    
    type: Optional[str] = Field(
        None,
        description="Type of identification (e.g., CPF, CNPJ, DNI, etc.)"
    )
    number: Optional[str] = Field(
        None,
        description="Identification number"
    )


class PaymentPayer(BaseModel):
    """
    PaymentPayer model for MercadoPago payments.
    
    Represents the payer information in a payment transaction.
    """
    
    email: EmailStr = Field(
        ...,
        description="Email address of the payer (required)"
    )
    id: Optional[str] = Field(
        None,
        description="Unique identifier of the payer"
    )
    identification: Optional[PayerIdentification] = Field(
        None,
        description="Identification information of the payer"
    )
    type: Optional[Literal["customer", "registered", "guest"]] = Field(
        None,
        description="Type of payer: customer, registered, or guest"
    )
    
    class Config:
        """Pydantic model configuration."""
        json_schema_extra = {
            "example": {
                "email": "payer@example.com",
                "id": "123456",
                "identification": {
                    "type": "CPF",
                    "number": "12345678900"
                },
                "type": "customer"
            }
        }