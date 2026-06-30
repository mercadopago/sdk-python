# mercadopago/resources/payment_payer.py

from typing import Optional, Literal
from pydantic import BaseModel, Field


class PayerIdentification(BaseModel):
    """Payer identification information."""
    type: Optional[str] = Field(None, description="Type of identification")
    number: Optional[str] = Field(None, description="Identification number")


class PaymentPayer(BaseModel):
    """Payment payer information schema."""
    
    email: str = Field(..., description="Payer email address")
    id: Optional[str] = Field(None, description="Payer ID")
    identification: Optional[PayerIdentification] = Field(None, description="Payer identification")
    type: Optional[Literal["customer", "registered", "guest"]] = Field(
        None, 
        description="Type of payer"
    )