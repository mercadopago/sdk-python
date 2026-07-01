"""
MercadoPago Payment Request Schema Update

This module defines the updated PaymentRequest schema for the MercadoPago API.
The schema has been modified to align with MercadoPago's payment processing requirements.

Changes:
- REMOVED: amount, currency, customer_id, merchant_id, payment_method
- ADDED: transaction_amount, token, payment_method_id, installments, issuer_id,
         payer, capture, binary_mode, external_reference, statement_descriptor,
         date_of_expiration, additional_info, application_fee, notification_url,
         callback_url, coupon_code, coupon_amount
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl, validator


class PaymentPayer(BaseModel):
    """Payer information for the payment."""
    
    email: str = Field(..., description="Payer's email address")
    first_name: Optional[str] = Field(None, description="Payer's first name")
    last_name: Optional[str] = Field(None, description="Payer's last name")
    identification: Optional[dict] = Field(None, description="Payer's identification document")
    phone: Optional[dict] = Field(None, description="Payer's phone information")
    address: Optional[dict] = Field(None, description="Payer's address information")
    entity_type: Optional[str] = Field(None, description="Entity type (individual or association)")


class PaymentAdditionalInfo(BaseModel):
    """Additional information for the payment."""
    
    ip_address: Optional[str] = Field(None, description="IP address of the payer")
    items: Optional[list] = Field(None, description="List of items being purchased")
    payer: Optional[dict] = Field(None, description="Additional payer information")
    shipments: Optional[dict] = Field(None, description="Shipping information")


class PaymentRequest(BaseModel):
    """
    Updated Payment Request schema for MercadoPago API.
    
    Used by: POST /v1/payments
    """
    
    # Required fields
    transaction_amount: float = Field(
        ...,
        description="Amount to be paid",
        gt=0
    )
    
    payer: PaymentPayer = Field(
        ...,
        description="Information about the payer"
    )
    
    # Optional payment method fields
    token: Optional[str] = Field(
        None,
        description="Card token for the payment"
    )
    
    payment_method_id: Optional[str] = Field(
        None,
        description="Payment method identifier (e.g., visa, master, pix)"
    )
    
    installments: Optional[int] = Field(
        None,
        ge=1,
        description="Number of installments for the payment"
    )
    
    issuer_id: Optional[str] = Field(
        None,
        description="Issuer identifier for the payment method"
    )
    
    # Payment behavior settings
    capture: bool = Field(
        True,
        description="Whether to capture the payment automatically"
    )
    
    binary_mode: bool = Field(
        False,
        description="When true, payment can only result in approved or rejected"
    )
    
    # Reference and description fields
    external_reference: Optional[str] = Field(
        None,
        description="External reference for the payment"
    )
    
    statement_descriptor: Optional[str] = Field(
        None,
        max_length=22,
        description="Description that will appear on the payer's statement"
    )
    
    @validator('statement_descriptor')
    def validate_statement_descriptor(cls, v):
        if v and len(v) > 22:
            raise ValueError('statement_descriptor must not exceed 22 characters')
        return v
    
    # Expiration
    date_of_expiration: Optional[datetime] = Field(
        None,
        description="Expiration date for the payment"
    )
    
    # Additional information
    additional_info: Optional[PaymentAdditionalInfo] = Field(
        None,
        description="Additional information about the payment"
    )
    
    # Fee and commission
    application_fee: Optional[float] = Field(
        None,
        ge=0,
        description="Application fee amount"
    )
    
    # Notification URLs
    notification_url: Optional[HttpUrl] = Field(
        None,
        deprecated=True,
        description="URL for IPN notifications (deprecated, use callback_url instead)"
    )
    
    callback_url: Optional[HttpUrl] = Field(
        None,
        description="URL for payment notifications"
    )
    
    # Coupon fields
    coupon_code: Optional[str] = Field(
        None,
        description="Discount coupon code"
    )
    
    coupon_amount: Optional[float] = Field(
        None,
        ge=0,
        description="Discount amount from coupon"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "transaction_amount": 100.50,
                "token": "ae2b7b1b5e4c3b1b5e4c3b1b",
                "payment_method_id": "visa",
                "installments": 1,
                "issuer_id": "310",
                "payer": {
                    "email": "test_user@test.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "identification": {
                        "type": "CPF",
                        "number": "12345678909"
                    }
                },
                "capture": True,
                "binary_mode": False,
                "external_reference": "ORDER_123456",
                "statement_descriptor": "MY STORE",
                "additional_info": {
                    "items": [
                        {
                            "id": "item-1",
                            "title": "Product Name",
                            "quantity": 1,
                            "unit_price": 100.50
                        }
                    ]
                },
                "callback_url": "https://mystore.com/webhooks/mercadopago",
                "coupon_code": "DISCOUNT10",
                "coupon_amount": 10.0
            }
        }


class PaymentResponse(BaseModel):
    """Response schema for payment operations."""
    
    id: int = Field(..., description="Payment ID")
    status: str = Field(..., description="Payment status")
    status_detail: Optional[str] = Field(None, description="Payment status detail")
    transaction_amount: float = Field(..., description="Transaction amount")
    date_created: datetime = Field(..., description="Payment creation date")
    date_approved: Optional[datetime] = Field(None, description="Payment approval date")
    money_release_date: Optional[datetime] = Field(None, description="Money release date")
    
    class Config:
        schema_extra = {
            "example": {
                "id": 12345678,
                "status": "approved",
                "status_detail": "accredited",
                "transaction_amount": 100.50,
                "date_created": "2024-01-15T10:30:00Z",
                "date_approved": "2024-01-15T10:30:05Z"
            }
        }