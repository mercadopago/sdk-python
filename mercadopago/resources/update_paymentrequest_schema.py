"""
Update PaymentRequest schema for MercadoPago API.

This module defines the updated schema for payment requests with new fields
and structure aligned with MercadoPago's payment processing requirements.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl


class PaymentPayer(BaseModel):
    """Payer information for payment request."""
    
    email: Optional[str] = Field(None, description="Payer's email address")
    first_name: Optional[str] = Field(None, description="Payer's first name")
    last_name: Optional[str] = Field(None, description="Payer's last name")
    identification: Optional[dict] = Field(None, description="Payer's identification document")
    phone: Optional[dict] = Field(None, description="Payer's phone information")
    address: Optional[dict] = Field(None, description="Payer's address information")
    entity_type: Optional[str] = Field(None, description="Entity type (individual or association)")


class PaymentAdditionalInfo(BaseModel):
    """Additional information for payment request."""
    
    ip_address: Optional[str] = Field(None, description="IP address of the buyer")
    items: Optional[list] = Field(None, description="List of items being paid")
    payer: Optional[dict] = Field(None, description="Additional payer information")
    shipments: Optional[dict] = Field(None, description="Shipping information")


class PaymentRequest(BaseModel):
    """
    Updated PaymentRequest schema for POST /v1/payments endpoint.
    
    This schema reflects the changes to remove legacy fields and add new
    payment processing fields aligned with MercadoPago's current API.
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
    
    # Payment method fields
    token: Optional[str] = Field(
        None,
        description="Card token for payment"
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
        description="Payment issuer identifier"
    )
    
    # Payment behavior fields
    capture: bool = Field(
        True,
        description="Whether to capture the payment immediately"
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
    
    # Timing fields
    date_of_expiration: Optional[datetime] = Field(
        None,
        description="Expiration date for the payment"
    )
    
    # Additional information
    additional_info: Optional[PaymentAdditionalInfo] = Field(
        None,
        description="Additional information about the payment"
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
        description="Discount amount from coupon",
        ge=0
    )
    
    # Notification fields
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
                "token": "card_token_123",
                "payment_method_id": "visa",
                "installments": 3,
                "issuer_id": "310",
                "payer": {
                    "email": "customer@example.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "identification": {
                        "type": "DNI",
                        "number": "12345678"
                    }
                },
                "capture": True,
                "binary_mode": False,
                "external_reference": "ORDER-12345",
                "statement_descriptor": "MY STORE",
                "additional_info": {
                    "ip_address": "192.168.1.1",
                    "items": [
                        {
                            "id": "item-123",
                            "title": "Product Name",
                            "quantity": 1,
                            "unit_price": 100.50
                        }
                    ]
                },
                "callback_url": "https://mystore.com/payment/callback",
                "coupon_code": "DISCOUNT10"
            }
        }


# Legacy field mapping for migration reference
REMOVED_FIELDS = [
    "amount",  # Replaced by transaction_amount
    "currency",  # Now handled at account level
    "customer_id",  # Replaced by payer object
    "merchant_id",  # Now handled via authentication
    "payment_method"  # Replaced by payment_method_id
]

FIELD_MIGRATION_MAP = {
    "amount": "transaction_amount",
    "customer_id": "payer",
    "payment_method": "payment_method_id"
}