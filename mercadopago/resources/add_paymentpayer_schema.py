# mercadopago/resources/add_paymentpayer_schema.py

"""PaymentPayer resource schema for MercadoPago SDK."""

from typing import Optional, Literal
from pydantic import BaseModel, Field, EmailStr


class PaymentPayerIdentification(BaseModel):
    """Identification information for the payer."""
    
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
    PaymentPayer schema for MercadoPago payments.
    
    Represents the payer information in a payment transaction.
    """
    
    email: EmailStr = Field(
        ...,
        description="Email address of the payer (required)"
    )
    id: Optional[str] = Field(
        None,
        description="Unique identifier for the payer"
    )
    identification: Optional[PaymentPayerIdentification] = Field(
        None,
        description="Identification document information for the payer"
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