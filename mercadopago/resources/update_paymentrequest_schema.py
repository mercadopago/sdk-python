"""
MercadoPago Payment Request Schema Update

This module defines the updated PaymentRequest schema with new fields
and removed legacy fields for the MercadoPago payment processing API.

Change Log:
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
    """
    Payment payer information.
    """
    email: str = Field(..., description="Payer email address")
    first_name: Optional[str] = Field(None, description="Payer first name")
    last_name: Optional[str] = Field(None, description="Payer last name")
    identification: Optional[dict] = Field(None, description="Identification information")
    phone: Optional[dict] = Field(None, description="Phone information")
    address: Optional[dict] = Field(None, description="Address information")
    entity_type: Optional[str] = Field(None, description="Entity type (individual/association)")


class PaymentAdditionalInfo(BaseModel):
    """
    Additional information for the payment.
    """
    ip_address: Optional[str] = Field(None, description="IP address of the payer")
    items: Optional[list] = Field(None, description="Items being paid for")
    payer: Optional[dict] = Field(None, description="Additional payer information")
    shipments: Optional[dict] = Field(None, description="Shipment information")


class PaymentRequest(BaseModel):
    """
    Updated Payment Request schema for MercadoPago API.
    
    Affected endpoints:
    - POST /v1/payments
    """
    
    # Required fields
    transaction_amount: float = Field(
        ...,
        description="Amount to be paid",
        gt=0,
        example=100.50
    )
    
    payer: PaymentPayer = Field(
        ...,
        description="Payer information"
    )
    
    # Optional payment details
    token: Optional[str] = Field(
        None,
        description="Card token for payment processing"
    )
    
    payment_method_id: Optional[str] = Field(
        None,
        description="Payment method identifier",
        example="visa"
    )
    
    installments: Optional[int] = Field(
        None,
        description="Number of installments",
        ge=1,
        example=1
    )
    
    issuer_id: Optional[str] = Field(
        None,
        description="Issuer identifier"
    )
    
    # Payment configuration
    capture: bool = Field(
        True,
        description="Whether to capture the payment immediately"
    )
    
    binary_mode: bool = Field(
        False,
        description="Binary mode for payment approval"
    )
    
    # Reference and description
    external_reference: Optional[str] = Field(
        None,
        description="External reference for the payment"
    )
    
    statement_descriptor: Optional[str] = Field(
        None,
        description="Statement descriptor",
        max_length=22
    )
    
    # Timing
    date_of_expiration: Optional[datetime] = Field(
        None,
        description="Expiration date for the payment"
    )
    
    # Additional information
    additional_info: Optional[PaymentAdditionalInfo] = Field(
        None,
        description="Additional payment information"
    )
    
    # Fees and amounts
    application_fee: Optional[float] = Field(
        None,
        description="Application fee amount",
        ge=0
    )
    
    # Notifications and callbacks
    notification_url: Optional[HttpUrl] = Field(
        None,
        description="URL for payment notifications",
        deprecated=True
    )
    
    callback_url: Optional[HttpUrl] = Field(
        None,
        description="Callback URL after payment processing"
    )
    
    # Coupons
    coupon_code: Optional[str] = Field(
        None,
        description="Coupon code to apply"
    )
    
    coupon_amount: Optional[float] = Field(
        None,
        description="Coupon discount amount",
        ge=0
    )
    
    @validator('statement_descriptor')
    def validate_statement_descriptor(cls, v):
        """Validate statement descriptor length."""
        if v is not None and len(v) > 22:
            raise ValueError('statement_descriptor must not exceed 22 characters')
        return v
    
    @validator('installments')
    def validate_installments(cls, v):
        """Validate installments is positive."""
        if v is not None and v < 1:
            raise ValueError('installments must be at least 1')
        return v
    
    @validator('transaction_amount', 'application_fee', 'coupon_amount')
    def validate_positive_amounts(cls, v, field):
        """Validate amounts are non-negative."""
        if v is not None and v < 0:
            raise ValueError(f'{field.name} must be non-negative')
        return v
    
    @validator('date_of_expiration')
    def validate_expiration_date(cls, v):
        """Validate expiration date is in the future."""
        if v is not None and v <= datetime.now():
            raise ValueError('date_of_expiration must be in the future')
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "transaction_amount": 100.50,
                "token": "card_token_example",
                "payment_method_id": "visa",
                "installments": 1,
                "payer": {
                    "email": "customer@example.com",
                    "first_name": "John",
                    "last_name": "Doe"
                },
                "capture": True,
                "binary_mode": False,
                "external_reference": "ORDER-12345",
                "statement_descriptor": "MY STORE",
                "callback_url": "https://mystore.com/callback",
                "coupon_code": "DISCOUNT10"
            }
        }


# Migration notes for developers
MIGRATION_NOTES = """
BREAKING CHANGES - PaymentRequest Schema Update:

REMOVED FIELDS (no longer supported):
- amount -> Use 'transaction_amount' instead
- currency -> Currency is now determined by the account configuration
- customer_id -> Customer information is now included in 'payer' object
- merchant_id -> Merchant is determined by authentication credentials
- payment_method -> Use 'payment_method_id' instead

NEW REQUIRED FIELDS:
- transaction_amount (float): The payment amount
- payer (PaymentPayer): Complete payer information object

NEW OPTIONAL FIELDS:
- token, payment_method_id, installments, issuer_id
- capture (default: true), binary_mode (default: false)
- external_reference, statement_descriptor (max 22 chars)
- date_of_expiration, additional_info, application_fee
- notification_url (deprecated), callback_url
- coupon_code, coupon_amount

AFFECTED ENDPOINTS:
- POST /v1/payments

MIGRATION EXAMPLE:
Old:
{
    "amount": 100.50,
    "currency": "USD",
    "customer_id": "123",
    "merchant_id": "456",
    "payment_method": "visa"
}

New:
{
    "transaction_amount": 100.50,
    "payment_method_id": "visa",
    "payer": {
        "email": "customer@example.com"
    }
}
"""