# mercadopago/resources/payment_item.py

from mercadopago.http import HttpClient
from mercadopago.config import Config
from mercadopago.resources.base import ResourceBase


class PaymentItem(ResourceBase):
    """
    PaymentItem resource for Mercado Pago API.
    
    Represents an item in a payment transaction with details about
    the product or service being paid for.
    """
    
    def __init__(self, client: HttpClient, config: Config):
        """
        Initialize PaymentItem resource.
        
        Args:
            client: HTTP client for making API requests
            config: Configuration object with API credentials
        """
        super().__init__(client, config)
        self._base_path = "/v1/payment_items"
    
    @property
    def base_path(self) -> str:
        """Get the base API path for payment items."""
        return self._base_path


class PaymentItemSchema:
    """
    Schema definition for PaymentItem model.
    
    All fields are optional to allow flexible item creation.
    """
    
    def __init__(
        self,
        id: str = None,
        title: str = None,
        description: str = None,
        category_id: str = None,
        quantity: int = None,
        unit_price: float = None
    ):
        """
        Initialize a PaymentItem schema.
        
        Args:
            id: Unique identifier for the payment item
            title: Title or name of the item
            description: Detailed description of the item
            category_id: Category identifier for item classification
            quantity: Number of units of this item
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
        Convert the schema to a dictionary.
        
        Returns:
            Dictionary representation with non-None values
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
    def from_dict(cls, data: dict) -> 'PaymentItemSchema':
        """
        Create a PaymentItemSchema from a dictionary.
        
        Args:
            data: Dictionary containing payment item data
            
        Returns:
            PaymentItemSchema instance
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
        """String representation of the PaymentItemSchema."""
        return (
            f"PaymentItemSchema(id={self.id!r}, title={self.title!r}, "
            f"description={self.description!r}, category_id={self.category_id!r}, "
            f"quantity={self.quantity!r}, unit_price={self.unit_price!r})"
        )