# mercadopago/resources/payment_item.py

from typing import Optional
from mercadopago.resources.base import Resource


class PaymentItem(Resource):
    """
    PaymentItem model representing an item in a payment.
    
    Attributes:
        id (Optional[str]): The item identifier
        title (Optional[str]): The item title
        description (Optional[str]): The item description
        category_id (Optional[str]): The category identifier
        quantity (Optional[int]): The quantity of items
        unit_price (Optional[float]): The price per unit
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
            id (Optional[str]): The item identifier
            title (Optional[str]): The item title
            description (Optional[str]): The item description
            category_id (Optional[str]): The category identifier
            quantity (Optional[int]): The quantity of items
            unit_price (Optional[float]): The price per unit
            **kwargs: Additional fields
        """
        self.id = id
        self.title = title
        self.description = description
        self.category_id = category_id
        self.quantity = quantity
        self.unit_price = unit_price
        
        # Store any additional fields
        for key, value in kwargs.items():
            setattr(self, key, value)
    
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
        
        # Include any additional attributes
        for key, value in self.__dict__.items():
            if key not in ['id', 'title', 'description', 'category_id', 'quantity', 'unit_price'] and value is not None:
                data[key] = value
        
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
        return cls(**data)
    
    def __repr__(self) -> str:
        """String representation of the PaymentItem."""
        return f"PaymentItem(id={self.id!r}, title={self.title!r}, quantity={self.quantity}, unit_price={self.unit_price})"