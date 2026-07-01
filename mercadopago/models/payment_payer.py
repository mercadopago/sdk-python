# mercadopago/models/payment_payer.py

from typing import Optional
from pydantic import BaseModel, Field


class PayerIdentification(BaseModel):
    """Payer identification information."""
    
    type: Optional[str] = Field(None, description="Type of identification")
    number: Optional[str] = Field(None, description="Identification number")


class PaymentPayer(BaseModel):
    """Payment payer information.
    
    Represents the person or entity making a payment.
    """
    
    email: str = Field(..., description="Payer email address")
    id: Optional[str] = Field(None, description="Payer ID")
    identification: Optional[PayerIdentification] = Field(None, description="Payer identification details")
    type: Optional[str] = Field(None, description="Payer type: customer, registered, or guest")