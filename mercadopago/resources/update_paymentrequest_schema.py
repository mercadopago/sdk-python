"""
MercadoPago Payment Request Schema Update

This module defines the updated PaymentRequest schema with modified fields
for the MercadoPago payments API.

Change type: modify
Target: PaymentRequest schema
Affected endpoints: POST /v1/payments
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl


class PaymentPayer(BaseModel):
    """Payment payer information."""
    
    email: Optional[str] = Field(None, description="Payer email address")
    first_name: Optional[str] = Field(None, description="Payer first name")
    last_name: Optional[str] = Field(None, description="Payer last name")
    identification: Optional[dict] = Field(None, description="Payer identification")
    phone: Optional[dict] = Field(None, description="Payer phone information")
    address: Optional[dict] = Field(None, description="Payer address")
    entity_type: Optional[str] = Field(None, description="Entity type (individual or association)")


class PaymentAdditionalInfo(BaseModel):
    """Additional payment information."""
    
    ip_address: Optional[str] = Field(None, description="IP address of the buyer")
    items: Optional[list] = Field(None, description="List of items")
    payer: Optional[dict] = Field(None, description="Additional payer information")
    shipments: Optional[dict] = Field(None, description="Shipment information")


class PaymentRequest(BaseModel):
    """
    Updated Payment Request schema for MercadoPago API.
    
    Removed fields:
        - amount
        - currency
        - customer_id
        - merchant_id
        - payment_method
    
    Added fields:
        - transaction_amount (required)
        - token
        - payment_method_id
        - installments
        - issuer_id
        - payer (required)
        - capture
        - binary_mode
        - external_reference
        - statement_descriptor
        - date_of_expiration
        - additional_info
        - application_fee
        - notification_url (deprecated)
        - callback_url
        - coupon_code
        - coupon_amount
    """
    
    # Required fields
    transaction_amount: float = Field(
        ...,
        description="Transaction amount",
        gt=0
    )
    
    payer: PaymentPayer = Field(
        ...,
        description="Payer information"
    )
    
    # Optional payment fields
    token: Optional[str] = Field(
        None,
        description="Card token"
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
    
    # Control fields
    capture: bool = Field(
        True,
        description="Whether to capture payment immediately"
    )
    
    binary_mode: bool = Field(
        False,
        description="Binary mode for payment approval"
    )
    
    # Reference fields
    external_reference: Optional[str] = Field(
        None,
        description="External reference for the payment"
    )
    
    statement_descriptor: Optional[str] = Field(
        None,
        description="Statement descriptor shown on card statement",
        max_length=22
    )
    
    # Temporal fields
    date_of_expiration: Optional[datetime] = Field(
        None,
        description="Payment expiration date"
    )
    
    # Additional information
    additional_info: Optional[PaymentAdditionalInfo] = Field(
        None,
        description="Additional payment information"
    )
    
    # Fee and discount fields
    application_fee: Optional[float] = Field(
        None,
        description="Application fee amount",
        ge=0
    )
    
    coupon_code: Optional[str] = Field(
        None,
        description="Coupon code for discount"
    )
    
    coupon_amount: Optional[float] = Field(
        None,
        description="Coupon discount amount",
        ge=0
    )
    
    # Notification fields
    notification_url: Optional[HttpUrl] = Field(
        None,
        description="Webhook notification URL (deprecated - use callback_url instead)",
        deprecated=True
    )
    
    callback_url: Optional[HttpUrl] = Field(
        None,
        description="Callback URL for payment notifications"
    )
    
    class Config:
        """Pydantic model configuration."""
        
        json_schema_extra = {
            "example": {
                "transaction_amount": 100.50,
                "token": "card_token_example",
                "payment_method_id": "visa",
                "installments": 1,
                "issuer_id": "310",
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
                "callback_url": "https://example.com/callback",
                "coupon_code": "DISCOUNT10",
                "coupon_amount": 10.00
            }
        }


class PaymentResponse(BaseModel):
    """Payment response model."""
    
    id: int = Field(..., description="Payment ID")
    status: str = Field(..., description="Payment status")
    status_detail: str = Field(..., description="Payment status detail")
    transaction_amount: float = Field(..., description="Transaction amount")
    payment_method_id: Optional[str] = Field(None, description="Payment method ID")
    date_created: datetime = Field(..., description="Creation date")
    date_approved: Optional[datetime] = Field(None, description="Approval date")
    external_reference: Optional[str] = Field(None, description="External reference")


# Migration notes
MIGRATION_NOTES = """
Migration Guide for PaymentRequest Schema Update
=================================================

REMOVED FIELDS (action required):
---------------------------------
1. amount -> Use 'transaction_amount' instead
2. currency -> Currency is now inferred from merchant configuration
3. customer_id -> Use 'payer' object with detailed information
4. merchant_id -> Merchant is authenticated via API credentials
5. payment_method -> Use 'payment_method_id' instead

NEW REQUIRED FIELDS:
-------------------
1. transaction_amount: float - The payment amount
2. payer: PaymentPayer - Complete payer information object

NEW OPTIONAL FIELDS:
-------------------
- token: Card token for card payments
- payment_method_id: Payment method identifier
- installments: Number of payment installments
- issuer_id: Card issuer identifier
- capture: Auto-capture flag (default: true)
- binary_mode: Binary approval mode (default: false)
- external_reference: Your internal reference
- statement_descriptor: Card statement text (max 22 chars)
- date_of_expiration: Payment expiration datetime
- additional_info: Additional payment details
- application_fee: Marketplace application fee
- notification_url: Webhook URL (deprecated, use callback_url)
- callback_url: Payment notification callback URL
- coupon_code: Discount coupon code
- coupon_amount: Discount amount

EXAMPLE MIGRATION:
-----------------
OLD:
{
    "amount": 100.50,
    "currency": "BRL",
    "customer_id": "12345",
    "merchant_id": "67890",
    "payment_method": "credit_card"
}

NEW:
{
    "transaction_amount": 100.50,
    "payment_method_id": "visa",
    "token": "card_token_here",
    "payer": {
        "email": "customer@example.com",
        "first_name": "John",
        "last_name": "Doe"
    },
    "installments": 1
}
"""