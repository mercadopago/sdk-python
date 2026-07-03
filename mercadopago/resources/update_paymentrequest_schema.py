"""
PaymentRequest schema for MercadoPago API v1.

This module defines the updated schema for payment requests,
removing legacy fields and adding new payment processing fields.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl


class PaymentPayer(BaseModel):
    """Payer information for payment requests."""
    
    email: Optional[str] = Field(None, description="Payer email address")
    first_name: Optional[str] = Field(None, description="Payer first name")
    last_name: Optional[str] = Field(None, description="Payer last name")
    identification: Optional[dict] = Field(None, description="Payer identification document")
    phone: Optional[dict] = Field(None, description="Payer phone information")
    address: Optional[dict] = Field(None, description="Payer address information")
    entity_type: Optional[str] = Field(None, description="Entity type: individual or association")


class PaymentAdditionalInfo(BaseModel):
    """Additional information for payment requests."""
    
    ip_address: Optional[str] = Field(None, description="IP address of the buyer")
    items: Optional[list] = Field(None, description="List of items being paid for")
    payer: Optional[dict] = Field(None, description="Additional payer information")
    shipments: Optional[dict] = Field(None, description="Shipping information")


class PaymentRequest(BaseModel):
    """
    Updated PaymentRequest schema for MercadoPago API v1.
    
    Used for POST /v1/payments endpoint.
    
    Changes:
    - REMOVED: amount, currency, customer_id, merchant_id, payment_method
    - ADDED: transaction_amount, token, payment_method_id, installments, issuer_id,
             payer, capture, binary_mode, external_reference, statement_descriptor,
             date_of_expiration, additional_info, application_fee, notification_url,
             callback_url, coupon_code, coupon_amount
    """
    
    # Required fields
    transaction_amount: float = Field(
        ...,
        description="Amount to be paid",
        gt=0
    )
    payer: PaymentPayer = Field(
        ...,
        description="Payer information (required)"
    )
    
    # Optional payment fields
    token: Optional[str] = Field(
        None,
        description="Card token ID for card payments"
    )
    payment_method_id: Optional[str] = Field(
        None,
        description="Payment method identifier"
    )
    installments: Optional[int] = Field(
        None,
        description="Number of installments",
        ge=1
    )
    issuer_id: Optional[str] = Field(
        None,
        description="Issuer identifier"
    )
    
    # Payment behavior
    capture: bool = Field(
        True,
        description="Whether to automatically capture the payment"
    )
    binary_mode: bool = Field(
        False,
        description="When set to true, payment can only be approved or rejected"
    )
    
    # Reference and description fields
    external_reference: Optional[str] = Field(
        None,
        description="External reference for the payment"
    )
    statement_descriptor: Optional[str] = Field(
        None,
        max_length=22,
        description="Description that will appear on the card statement"
    )
    description: Optional[str] = Field(
        None,
        description="Payment description"
    )
    
    # Date fields
    date_of_expiration: Optional[datetime] = Field(
        None,
        description="Expiration date for the payment"
    )
    
    # Additional information
    additional_info: Optional[PaymentAdditionalInfo] = Field(
        None,
        description="Additional payment information"
    )
    
    # Fee and discounts
    application_fee: Optional[float] = Field(
        None,
        description="Application fee amount",
        ge=0
    )
    coupon_code: Optional[str] = Field(
        None,
        description="Coupon code for discounts"
    )
    coupon_amount: Optional[float] = Field(
        None,
        description="Discount amount from coupon",
        ge=0
    )
    
    # Callback URLs
    notification_url: Optional[HttpUrl] = Field(
        None,
        deprecated=True,
        description="URL for payment notifications (deprecated, use callback_url instead)"
    )
    callback_url: Optional[HttpUrl] = Field(
        None,
        description="URL for payment callbacks"
    )
    
    class Config:
        """Pydantic model configuration."""
        
        json_schema_extra = {
            "example": {
                "transaction_amount": 100.50,
                "token": "card_token_123456",
                "payment_method_id": "visa",
                "installments": 1,
                "payer": {
                    "email": "customer@example.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "identification": {
                        "type": "CPF",
                        "number": "12345678900"
                    }
                },
                "capture": True,
                "binary_mode": False,
                "external_reference": "ORDER-123456",
                "statement_descriptor": "MY STORE",
                "description": "Purchase of products",
                "callback_url": "https://example.com/callback"
            }
        }


class PaymentResponse(BaseModel):
    """Response schema for payment requests."""
    
    id: int = Field(..., description="Payment ID")
    status: str = Field(..., description="Payment status")
    status_detail: Optional[str] = Field(None, description="Detailed status information")
    transaction_amount: float = Field(..., description="Transaction amount")
    date_created: datetime = Field(..., description="Payment creation date")
    date_approved: Optional[datetime] = Field(None, description="Payment approval date")
    payment_method_id: Optional[str] = Field(None, description="Payment method used")
    external_reference: Optional[str] = Field(None, description="External reference")
    
    class Config:
        """Pydantic model configuration."""
        
        json_schema_extra = {
            "example": {
                "id": 123456789,
                "status": "approved",
                "status_detail": "accredited",
                "transaction_amount": 100.50,
                "date_created": "2024-01-15T10:30:00Z",
                "date_approved": "2024-01-15T10:30:05Z",
                "payment_method_id": "visa",
                "external_reference": "ORDER-123456"
            }
        }