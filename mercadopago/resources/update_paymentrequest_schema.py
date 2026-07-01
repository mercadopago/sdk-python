"""
MercadoPago Payment Request Schema Update

This module defines the updated PaymentRequest schema for MercadoPago API v1.
Removed legacy fields and added new payment processing fields.

Change Summary:
- REMOVED: amount, currency, customer_id, merchant_id, payment_method
- ADDED: transaction_amount, token, payment_method_id, installments, issuer_id,
         payer, capture, binary_mode, external_reference, statement_descriptor,
         date_of_expiration, additional_info, application_fee, notification_url,
         callback_url, coupon_code, coupon_amount

Affected Endpoints:
- POST /v1/payments
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl, field_validator, ConfigDict


class PaymentPayer(BaseModel):
    """Payment payer information."""
    
    model_config = ConfigDict(extra='forbid')
    
    email: str = Field(..., description="Payer email address")
    first_name: Optional[str] = Field(None, description="Payer first name")
    last_name: Optional[str] = Field(None, description="Payer last name")
    identification: Optional[dict] = Field(None, description="Payer identification document")
    phone: Optional[dict] = Field(None, description="Payer phone information")
    address: Optional[dict] = Field(None, description="Payer address information")
    entity_type: Optional[str] = Field(None, description="Entity type (individual or association)")


class PaymentAdditionalInfo(BaseModel):
    """Additional payment information."""
    
    model_config = ConfigDict(extra='forbid')
    
    ip_address: Optional[str] = Field(None, description="IP address of the buyer")
    items: Optional[list] = Field(None, description="List of items being paid")
    payer: Optional[dict] = Field(None, description="Additional payer information")
    shipments: Optional[dict] = Field(None, description="Shipment information")


class PaymentRequest(BaseModel):
    """
    Updated PaymentRequest schema for MercadoPago API v1.
    
    This schema represents the structure for creating payment requests
    with the new field set introduced in the latest API version.
    """
    
    model_config = ConfigDict(extra='forbid', validate_assignment=True)
    
    # Required fields
    transaction_amount: float = Field(
        ...,
        description="Transaction amount to be paid",
        gt=0,
        example=100.50
    )
    
    payer: PaymentPayer = Field(
        ...,
        description="Payment payer information (required)"
    )
    
    # Payment method fields
    token: Optional[str] = Field(
        None,
        description="Card token identifier for the payment method"
    )
    
    payment_method_id: Optional[str] = Field(
        None,
        description="Payment method identifier (e.g., visa, master, pix)",
        example="visa"
    )
    
    installments: Optional[int] = Field(
        None,
        description="Number of installments for the payment",
        ge=1,
        example=1
    )
    
    issuer_id: Optional[str] = Field(
        None,
        description="Payment issuer identifier"
    )
    
    # Processing options
    capture: bool = Field(
        default=True,
        description="Whether to capture the payment immediately or just authorize"
    )
    
    binary_mode: bool = Field(
        default=False,
        description="When true, payment can only result in approved or rejected"
    )
    
    # Reference and descriptor fields
    external_reference: Optional[str] = Field(
        None,
        description="External reference for the payment (merchant's internal ID)",
        example="ORDER-12345"
    )
    
    statement_descriptor: Optional[str] = Field(
        None,
        description="Description that will appear on the payer's statement",
        max_length=22,
        example="MYSTORE*PURCHASE"
    )
    
    # Expiration
    date_of_expiration: Optional[datetime] = Field(
        None,
        description="Date and time when the payment expires"
    )
    
    # Additional information
    additional_info: Optional[PaymentAdditionalInfo] = Field(
        None,
        description="Additional information about the payment and items"
    )
    
    # Fee and discount fields
    application_fee: Optional[float] = Field(
        None,
        description="Application fee amount for marketplace scenarios",
        ge=0
    )
    
    coupon_code: Optional[str] = Field(
        None,
        description="Discount coupon code"
    )
    
    coupon_amount: Optional[float] = Field(
        None,
        description="Discount coupon amount",
        ge=0
    )
    
    # Notification URLs
    notification_url: Optional[HttpUrl] = Field(
        None,
        description="URL to receive payment notifications (deprecated, use callback_url)",
        deprecated=True
    )
    
    callback_url: Optional[HttpUrl] = Field(
        None,
        description="URL to receive payment callbacks"
    )
    
    @field_validator('statement_descriptor')
    @classmethod
    def validate_statement_descriptor(cls, v: Optional[str]) -> Optional[str]:
        """Validate statement descriptor length and characters."""
        if v is not None:
            if len(v) > 22:
                raise ValueError('statement_descriptor must not exceed 22 characters')
            # Optional: Add additional character validation if needed
            # e.g., alphanumeric and specific special characters only
        return v
    
    @field_validator('transaction_amount', 'application_fee', 'coupon_amount')
    @classmethod
    def validate_positive_amounts(cls, v: Optional[float]) -> Optional[float]:
        """Ensure amount fields are positive when provided."""
        if v is not None and v < 0:
            raise ValueError('Amount must be positive')
        return v
    
    @field_validator('coupon_amount')
    @classmethod
    def validate_coupon_amount(cls, v: Optional[float], info) -> Optional[float]:
        """Ensure coupon amount doesn't exceed transaction amount."""
        if v is not None and 'transaction_amount' in info.data:
            transaction_amount = info.data['transaction_amount']
            if v > transaction_amount:
                raise ValueError('coupon_amount cannot exceed transaction_amount')
        return v
    
    def model_dump(self, **kwargs) -> dict:
        """
        Override model_dump to exclude None values by default.
        
        This ensures that optional fields are not sent to the API when not provided.
        """
        kwargs.setdefault('exclude_none', True)
        return super().model_dump(**kwargs)


# Migration helper for legacy PaymentRequest objects
class LegacyPaymentRequest(BaseModel):
    """Legacy PaymentRequest schema (deprecated)."""
    
    amount: float
    currency: str
    customer_id: str
    merchant_id: str
    payment_method: str


def migrate_legacy_to_new(legacy: LegacyPaymentRequest, payer_email: str) -> PaymentRequest:
    """
    Migrate a legacy PaymentRequest to the new schema format.
    
    Args:
        legacy: Legacy payment request object
        payer_email: Required payer email for the new schema
        
    Returns:
        PaymentRequest: New format payment request
        
    Example:
        >>> legacy = LegacyPaymentRequest(
        ...     amount=100.0,
        ...     currency="USD",
        ...     customer_id="cust_123",
        ...     merchant_id="merch_456",
        ...     payment_method="credit_card"
        ... )
        >>> new_request = migrate_legacy_to_new(legacy, "buyer@example.com")
    """
    return PaymentRequest(
        transaction_amount=legacy.amount,
        payment_method_id=legacy.payment_method,
        external_reference=legacy.customer_id,
        payer=PaymentPayer(email=payer_email)
    )


# Example usage
if __name__ == "__main__":
    # Example: Creating a new payment request
    payment = PaymentRequest(
        transaction_amount=150.00,
        payment_method_id="visa",
        token="card_token_abc123",
        installments=3,
        payer=PaymentPayer(
            email="buyer@example.com",
            first_name="John",
            last_name="Doe"
        ),
        external_reference="ORDER-2024-001",
        statement_descriptor="STORE*PURCHASE",
        capture=True,
        binary_mode=False,
        callback_url="https://example.com/payment/callback"
    )
    
    print("Payment Request JSON:")
    print(payment.model_dump_json(indent=2, exclude_none=True))
    
    # Example: Payment with coupon
    payment_with_coupon = PaymentRequest(
        transaction_amount=200.00,
        payment_method_id="master",
        payer=PaymentPayer(email="customer@example.com"),
        coupon_code="DISCOUNT20",
        coupon_amount=40.00
    )
    
    print("\nPayment with Coupon:")
    print(payment_with_coupon.model_dump_json(indent=2, exclude_none=True))