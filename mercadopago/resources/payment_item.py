"""Payment Item resource for MercadoPago SDK."""

from mercadopago.resources.base import ResourceBase


class PaymentItem(ResourceBase):
    """
    PaymentItem resource class.
    
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
    
    def __init__(self, client=None):
        """
        Initialize PaymentItem resource.
        
        Args:
            client: MercadoPago client instance
        """
        super().__init__(client)
        self.id = None
        self.title = None
        self.description = None
        self.category_id = None
        self.quantity = None
        self.unit_price = None
    
    def validate(self):
        """
        Validate PaymentItem data.
        
        Returns:
            bool: True if valid
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        if not self.title:
            raise ValueError("title is required")
        
        if self.quantity is not None and self.quantity < 1:
            raise ValueError("quantity must be greater than 0")
        
        if self.unit_price is not None and self.unit_price < 0:
            raise ValueError("unit_price must be non-negative")
        
        return True
    
    def to_dict(self):
        """
        Convert PaymentItem to dictionary.
        
        Returns:
            dict: Dictionary representation of the payment item
        """
        data = {}
        
        if self.id is not None:
            data["id"] = self.id
        
        if self.title is not None:
            data["title"] = self.title
        
        if self.description is not None:
            data["description"] = self.description
        
        if self.category_id is not None:
            data["category_id"] = self.category_id
        
        if self.quantity is not None:
            data["quantity"] = self.quantity
        
        if self.unit_price is not None:
            data["unit_price"] = self.unit_price
        
        return data
    
    def from_dict(self, data):
        """
        Populate PaymentItem from dictionary.
        
        Args:
            data (dict): Dictionary with payment item data
            
        Returns:
            PaymentItem: Self instance
        """
        if not isinstance(data, dict):
            return self
        
        self.id = data.get("id")
        self.title = data.get("title")
        self.description = data.get("description")
        self.category_id = data.get("category_id")
        self.quantity = data.get("quantity")
        self.unit_price = data.get("unit_price")
        
        return self
    
    @property
    def total_amount(self):
        """
        Calculate total amount for this item.
        
        Returns:
            float: Total amount (quantity * unit_price) or None
        """
        if self.quantity is not None and self.unit_price is not None:
            return self.quantity * self.unit_price
        return None
    
    def __repr__(self):
        """String representation of PaymentItem."""
        return (
            f"PaymentItem(id={self.id!r}, title={self.title!r}, "
            f"quantity={self.quantity}, unit_price={self.unit_price})"
        )