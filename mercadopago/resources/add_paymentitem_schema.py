# mercadopago/resources/add_paymentitem_schema.py

"""
PaymentItem resource schema for MercadoPago SDK.

This module defines the PaymentItem model used for handling payment item data.
"""

from typing import Optional
from pydantic import BaseModel, Field


class PaymentItem(BaseModel):
    """
    PaymentItem model representing an item in a payment transaction.
    
    Attributes:
        id: Unique identifier for the payment item
        title: Title or name of the item
        description: Detailed description of the item
        category_id: Category identifier for the item
        quantity: Number of units of the item
        unit_price: Price per unit of the item
    """
    
    id: Optional[str] = Field(None, description="Unique identifier for the payment item")
    title: Optional[str] = Field(None, description="Title or name of the item")
    description: Optional[str] = Field(None, description="Detailed description of the item")
    category_id: Optional[str] = Field(None, description="Category identifier for the item")
    quantity: Optional[int] = Field(None, description="Number of units of the item")
    unit_price: Optional[float] = Field(None, description="Price per unit of the item")

    class Config:
        """Pydantic model configuration."""
        json_schema_extra = {
            "example": {
                "id": "item_001",
                "title": "Premium Widget",
                "description": "High-quality widget with extended warranty",
                "category_id": "electronics",
                "quantity": 2,
                "unit_price": 99.99
            }
        }