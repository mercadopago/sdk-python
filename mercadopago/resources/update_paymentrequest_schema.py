"""
MercadoPago PaymentRequest Schema Update

This module defines the updated schema for PaymentRequest with new fields
and removed legacy fields for the MercadoPago payment processing API.

Change Type: modify
Target: PaymentRequest schema
Affected Endpoints: POST /v1/payments
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl, validator


class PaymentPayer(BaseModel):
    """
    Payer information for payment processing.
    """
    email: Optional[str] = Field(None, description="Payer's email address")
    first_name: Optional[str] = Field(None, description="Payer's first name")
    last_name: Optional[str] = Field(None, description="Payer's last name")
    identification: Optional[dict] = Field(None, description="Payer's identification document")
    phone: Optional[dict] = Field(None, description="Payer's phone information")
    address: Optional[dict] = Field(None, description="Payer's address information")
    entity_type: Optional[str] = Field(None, description="Entity type (individual or association)")


class PaymentAdditionalInfo(BaseModel):
    """
    Additional information for payment context.
    """
    ip_address: Optional[str] = Field(None, description="IP address of the payer")
    items: Optional[list] = Field(None, description="List of items being purchased")
    payer: Optional[dict] = Field(None, description="Additional payer information")
    shipments: Optional[dict] = Field(None, description="Shipment information")


class PaymentRequest(BaseModel):
    """
    Updated PaymentRequest schema for MercadoPago payment processing.
    
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
        description="Amount to be paid",
        gt=0,
        example=100.50
    )
    
    payer: PaymentPayer = Field(
        ...,
        description="Payer information (required)"
    )
    
    # Payment method fields
    token: Optional[str] = Field(
        None,
        description="Card token for payment processing"
    )
    
    payment_method_id: Optional[str] = Field(
        None,
        description="Payment method identifier (e.g., visa, master, pix)"
    )
    
    installments: Optional[int] = Field(
        None,
        description="Number of installments",
        ge=1,
        example=1
    )
    
    issuer_id: Optional[str] = Field(
        None,
        description="Payment issuer identifier"
    )
    
    # Payment behavior flags
    capture: bool = Field(
        True,
        description="Whether to capture payment immediately or authorize only"
    )
    
    binary_mode: bool = Field(
        False,
        description="Enable binary mode (only approved or rejected status)"
    )
    
    # Reference and descriptor fields
    external_reference: Optional[str] = Field(
        None,
        description="External reference for the payment (e.g., order ID)",
        example="ORDER-12345"
    )
    
    statement_descriptor: Optional[str] = Field(
        None,
        description="Text that appears on payer's statement",
        max_length=22
    )
    
    # Expiration
    date_of_expiration: Optional[datetime] = Field(
        None,
        description="Expiration date for the payment"
    )
    
    # Additional information
    additional_info: Optional[PaymentAdditionalInfo] = Field(
        None,
        description="Additional information for fraud prevention and context"
    )
    
    # Fee and discount fields
    application_fee: Optional[float] = Field(
        None,
        description="Application fee to be charged",
        ge=0
    )
    
    coupon_code: Optional[str] = Field(
        None,
        description="Coupon code for discount"
    )
    
    coupon_amount: Optional[float] = Field(
        None,
        description="Discount amount from coupon",
        ge=0
    )
    
    # Notification fields
    notification_url: Optional[HttpUrl] = Field(
        None,
        description="URL for IPN notifications (deprecated - use webhook configuration instead)",
        deprecated=True
    )
    
    callback_url: Optional[HttpUrl] = Field(
        None,
        description="URL to redirect after payment completion"
    )
    
    @validator('statement_descriptor')
    def validate_statement_descriptor(cls, v):
        """Validate statement descriptor length and characters."""
        if v and len(v) > 22:
            raise ValueError('statement_descriptor must not exceed 22 characters')
        return v
    
    @validator('installments')
    def validate_installments(cls, v):
        """Validate installments is a positive integer."""
        if v is not None and v < 1:
            raise ValueError('installments must be at least 1')
        return v
    
    @validator('coupon_amount')
    def validate_coupon_amount(cls, v, values):
        """Validate coupon amount does not exceed transaction amount."""
        if v is not None and 'transaction_amount' in values:
            if v > values['transaction_amount']:
                raise ValueError('coupon_amount cannot exceed transaction_amount')
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "transaction_amount": 100.50,
                "payment_method_id": "visa",
                "token": "card_token_123abc",
                "installments": 1,
                "payer": {
                    "email": "customer@example.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "identification": {
                        "type": "CPF",
                        "number": "12345678909"
                    }
                },
                "external_reference": "ORDER-2024-001",
                "statement_descriptor": "MY STORE",
                "capture": True,
                "binary_mode": False,
                "callback_url": "https://mystore.com/payment/callback"
            }
        }


class PaymentResponse(BaseModel):
    """
    Response schema for payment creation.
    """
    id: int = Field(..., description="Payment ID")
    status: str = Field(..., description="Payment status")
    status_detail: Optional[str] = Field(None, description="Detailed status information")
    transaction_amount: float = Field(..., description="Transaction amount")
    date_created: datetime = Field(..., description="Payment creation date")
    date_approved: Optional[datetime] = Field(None, description="Payment approval date")
    external_reference: Optional[str] = Field(None, description="External reference")
    
    class Config:
        schema_extra = {
            "example": {
                "id": 123456789,
                "status": "approved",
                "status_detail": "accredited",
                "transaction_amount": 100.50,
                "date_created": "2024-01-15T10:30:00Z",
                "date_approved": "2024-01-15T10:30:05Z",
                "external_reference": "ORDER-2024-001"
            }
        }