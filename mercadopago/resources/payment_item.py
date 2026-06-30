# mercadopago/resources/payment_item.py

from typing import Optional
from mercadopago.resources.base import ResourceBase


class PaymentItem(ResourceBase):
    """
    PaymentItem model representing an item in a payment.
    
    Attributes:
        id (str, optional): Item identifier
        title (str, optional): Item title
        description (str, optional): Item description
        category_id (str, optional): Category identifier
        quantity (int, optional): Item quantity
        unit_price (float, optional): Price per unit
    """
    
    def __init__(
        self,
        id: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        category_id: Optional[str] = None,
        quantity: Optional[int] = None,
        unit_price: Optional[float] = None,
        **kwargs
    ):
        """
        Initialize a PaymentItem instance.
        
        Args:
            id (str, optional): Item identifier
            title (str, optional): Item title
            description (str, optional): Item description
            category_id (str, optional): Category identifier
            quantity (int, optional): Item quantity
            unit_price (float, optional): Price per unit
            **kwargs: Additional keyword arguments
        """
        self.id = id
        self.title = title
        self.description = description
        self.category_id = category_id
        self.quantity = quantity
        self.unit_price = unit_price
        super().__init__(**kwargs)
    
    def to_dict(self) -> dict:
        """
        Convert the PaymentItem instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the payment item
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
            data (dict): Dictionary containing payment item data
            
        Returns:
            PaymentItem: New PaymentItem instance
        """
        return cls(
            id=data.get('id'),
            title=data.get('title'),
            description=data.get('description'),
            category_id=data.get('category_id'),
            quantity=data.get('quantity'),
            unit_price=data.get('unit_price')
        )