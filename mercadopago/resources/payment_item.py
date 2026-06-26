# mercadopago/resources/payment_item.py

```python
"""
PaymentItem resource model for MercadoPago SDK.

This module defines the PaymentItem model representing individual items
in a payment transaction.
"""

from typing import Optional
from dataclasses import dataclass


@dataclass
class PaymentItem:
    """
    PaymentItem model representing an individual item in a payment.
    
    Attributes:
        id: Unique identifier for the payment item
        title: Title or name of the item
        description: Detailed description of the item
        category_id: Category identifier for the item
        quantity: Number of units of this item (integer)
        unit_price: Price per unit of the item (float)
    """
    
    id: str
    title: str
    description: str
    category_id: str
    quantity: int
    unit_price: float
    
    def __post_init__(self):
        """Validate the payment item data after initialization."""
        if not isinstance(self.quantity, int):
            raise TypeError("quantity must be an integer")
        
        if self.quantity <= 0:
            raise ValueError("quantity must be greater than 0")
        
        if not isinstance(self.unit_price, (int, float)):
            raise TypeError("unit_price must be a number")
        
        if self.unit_price < 0:
            raise ValueError("unit_price must be non-negative")
    
    def get_total_amount(self) -> float:
        """
        Calculate the total amount for this item.
        
        Returns:
            float: Total amount (quantity * unit_price)
        """
        return self.quantity * self.unit_price
    
    def to_dict(self) -> dict:
        """
        Convert the PaymentItem to a dictionary representation.
        
        Returns:
            dict: Dictionary containing all payment item attributes
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category_id": self.category_id,
            "quantity": self.quantity,
            "unit_price": self.unit_price
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'PaymentItem':
        """
        Create a PaymentItem instance from a dictionary.
        
        Args:
            data: Dictionary containing payment item data
            
        Returns:
            PaymentItem: New PaymentItem instance
            
        Raises:
            KeyError: If required fields are missing
            TypeError: If field types are incorrect
        """
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            category_id=data["category_id"],
            quantity=int(data["quantity"]),
            unit_price=float(data["unit_price"])
        )
    
    def __str__(self) -> str:
        """String representation of the PaymentItem."""
        return (f"PaymentItem(id='{self.id}', title='{self.title}', "
                f"quantity={self.quantity}, unit_price={self.unit_price})")
    
    def __repr__(self) -> str:
        """Developer-friendly representation of the PaymentItem."""
        return (f"PaymentItem(id='{self.id}', title='{self.title}', "
                f"description='{self.description}', category_id='{self.category_id}', "
                f"quantity={self.quantity}, unit_price={self.unit_price})")
```