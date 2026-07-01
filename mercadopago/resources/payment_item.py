"""
PaymentItem resource for MercadoPago SDK.

This module contains the PaymentItem model representing an item
in a payment transaction.
"""

from typing import Optional
from mercadopago.resources.base import ResourceBase


class PaymentItem(ResourceBase):
    """
    PaymentItem model representing an item in a payment.
    
    Attributes:
        id: Item identifier
        title: Item title/name
        description: Item description
        category_id: Category identifier for the item
        quantity: Quantity of items
        unit_price: Price per unit
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
            id: Item identifier
            title: Item title/name
            description: Item description
            category_id: Category identifier for the item
            quantity: Quantity of items
            unit_price: Price per unit
        """
        self.id = id
        self.title = title
        self.description = description
        self.category_id = category_id
        self.quantity = quantity
        self.unit_price = unit_price
    
    def to_dict(self) -> dict:
        """
        Convert PaymentItem instance to dictionary.
        
        Returns:
            Dictionary representation of the PaymentItem
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
        Create PaymentItem instance from dictionary.
        
        Args:
            data: Dictionary containing PaymentItem data
            
        Returns:
            PaymentItem instance
        """
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            description=data.get('description'),
            category_id=data.get('category_id'),
            quantity=data.get('quantity'),
            unit_price=data.get('unit_price')
        )