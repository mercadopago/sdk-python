# mercadopago/resources/add_paymentitem_schema.py

"""PaymentItem resource schema for MercadoPago SDK."""

from typing import Optional


class PaymentItem:
    """
    PaymentItem model representing an item in a payment transaction.
    
    Attributes:
        id (Optional[str]): Unique identifier for the payment item
        title (Optional[str]): Title or name of the item
        description (Optional[str]): Detailed description of the item
        category_id (Optional[str]): Category identifier for the item
        quantity (Optional[int]): Quantity of items
        unit_price (Optional[float]): Price per unit of the item
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
            id: Unique identifier for the payment item
            title: Title or name of the item
            description: Detailed description of the item
            category_id: Category identifier for the item
            quantity: Quantity of items
            unit_price: Price per unit of the item
        """
        self.id = id
        self.title = title
        self.description = description
        self.category_id = category_id
        self.quantity = quantity
        self.unit_price = unit_price
    
    def to_dict(self) -> dict:
        """
        Convert PaymentItem instance to dictionary representation.
        
        Returns:
            dict: Dictionary containing non-None payment item attributes
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
            data: Dictionary containing payment item data
            
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
    
    def __repr__(self) -> str:
        """
        String representation of PaymentItem.
        
        Returns:
            str: String representation showing all attributes
        """
        return (
            f"PaymentItem(id={self.id!r}, title={self.title!r}, "
            f"description={self.description!r}, category_id={self.category_id!r}, "
            f"quantity={self.quantity!r}, unit_price={self.unit_price!r})"
        )
    
    def __eq__(self, other) -> bool:
        """
        Check equality with another PaymentItem instance.
        
        Args:
            other: Another object to compare with
            
        Returns:
            bool: True if all attributes are equal, False otherwise
        """
        if not isinstance(other, PaymentItem):
            return False
        
        return (
            self.id == other.id and
            self.title == other.title and
            self.description == other.description and
            self.category_id == other.category_id and
            self.quantity == other.quantity and
            self.unit_price == other.unit_price
        )