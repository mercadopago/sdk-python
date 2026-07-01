# mercadopago/resources/payment_item.py

from mercadopago.resources.base import ResourceBase


class PaymentItem(ResourceBase):
    """
    PaymentItem resource for MercadoPago SDK.
    
    Represents an item in a payment transaction with details about
    the product or service being purchased.
    """
    
    _schema = {
        "id": str,
        "title": str,
        "description": str,
        "category_id": str,
        "quantity": int,
        "unit_price": float
    }
    
    def __init__(self, **kwargs):
        """
        Initialize a PaymentItem instance.
        
        Args:
            id (str, optional): Item identifier
            title (str, optional): Item title/name
            description (str, optional): Item description
            category_id (str, optional): Category identifier
            quantity (int, optional): Quantity of items
            unit_price (float, optional): Price per unit
        """
        super().__init__(**kwargs)
        
        self.id = kwargs.get("id")
        self.title = kwargs.get("title")
        self.description = kwargs.get("description")
        self.category_id = kwargs.get("category_id")
        self.quantity = kwargs.get("quantity")
        self.unit_price = kwargs.get("unit_price")
    
    def to_dict(self):
        """
        Convert PaymentItem instance to dictionary.
        
        Returns:
            dict: Dictionary representation of the payment item
        """
        result = {}
        
        if self.id is not None:
            result["id"] = self.id
        if self.title is not None:
            result["title"] = self.title
        if self.description is not None:
            result["description"] = self.description
        if self.category_id is not None:
            result["category_id"] = self.category_id
        if self.quantity is not None:
            result["quantity"] = self.quantity
        if self.unit_price is not None:
            result["unit_price"] = self.unit_price
        
        return result
    
    @classmethod
    def from_dict(cls, data):
        """
        Create PaymentItem instance from dictionary.
        
        Args:
            data (dict): Dictionary containing payment item data
            
        Returns:
            PaymentItem: New PaymentItem instance
        """
        if not data:
            return None
        
        return cls(
            id=data.get("id"),
            title=data.get("title"),
            description=data.get("description"),
            category_id=data.get("category_id"),
            quantity=data.get("quantity"),
            unit_price=data.get("unit_price")
        )