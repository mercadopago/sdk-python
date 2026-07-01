"""
PaymentItem resource for MercadoPago SDK.

This module provides the PaymentItem model for handling payment item data.
"""

from typing import Optional
from mercadopago.resources.base import ResourceBase


class PaymentItem(ResourceBase):
    """
    PaymentItem model for representing individual items in a payment.
    
    Attributes:
        id (Optional[str]): Unique identifier for the payment item.
        title (Optional[str]): Title or name of the item.
        description (Optional[str]): Detailed description of the item.
        category_id (Optional[str]): Category identifier for the item.
        quantity (Optional[int]): Number of units of the item.
        unit_price (Optional[float]): Price per unit of the item.
    """
    
    def __init__(
        self,
        id: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        category_id: Optional[str] = None,
        quantity: Optional[int] = None,
        unit_price: Optional[float] = None
    ):
        """
        Initialize a PaymentItem instance.
        
        Args:
            id (Optional[str]): Unique identifier for the payment item.
            title (Optional[str]): Title or name of the item.
            description (Optional[str]): Detailed description of the item.
            category_id (Optional[str]): Category identifier for the item.
            quantity (Optional[int]): Number of units of the item.
            unit_price (Optional[float]): Price per unit of the item.
        """
        self.id = id
        self.title = title
        self.description = description
        self.category_id = category_id
        self.quantity = quantity
        self.unit_price = unit_price
    
    def to_dict(self) -> dict:
        """
        Convert the PaymentItem instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the payment item with non-None values.
        """
        data = {}
        
        if self.id is not None:
            data['id'] = self.id
        if self.title is not None:
            data['title'] = self.title
        if self.description is not None:
            data['description'] = self.description
        if self.category_id is not None:
            data['category_id'] = self.category_id
        if self.quantity is not None:
            data['quantity'] = self.quantity
        if self.unit_price is not None:
            data['unit_price'] = self.unit_price
        
        return data
    
    @classmethod
    def from_dict(cls, data: dict) -> 'PaymentItem':
        """
        Create a PaymentItem instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing payment item data.
        
        Returns:
            PaymentItem: A new PaymentItem instance populated with the provided data.
        """
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            description=data.get('description'),
            category_id=data.get('category_id'),
            quantity=data.get('quantity'),
            unit_price=data.get('unit_price')
        )
    
    def __repr__(self) -> str:
        """
        Return a string representation of the PaymentItem.
        
        Returns:
            str: String representation including key attributes.
        """
        return (
            f"PaymentItem(id={self.id!r}, title={self.title!r}, "
            f"quantity={self.quantity}, unit_price={self.unit_price})"
        )
    
    def __eq__(self, other) -> bool:
        """
        Compare two PaymentItem instances for equality.
        
        Args:
            other: Another object to compare with.
        
        Returns:
            bool: True if both instances have the same attribute values.
        """
        if not isinstance(other, PaymentItem):
            return False
        
        return (
            self.id == other.id
            and self.title == other.title
            and self.description == other.description
            and self.category_id == other.category_id
            and self.quantity == other.quantity
            and self.unit_price == other.unit_price
        )