"""
MercadoPago Payment Additional Info Module.

This module provides the PaymentAdditionalInfo resource for handling
additional information related to payments, including items, payer details,
and shipment information used for fraud scoring.
"""

from typing import List, Optional, Dict, Any
from mercadopago.resources.base import Resource


class PaymentItem:
    """
    Represents an item in a payment transaction.
    
    Attributes:
        id: Item identifier
        title: Item title
        description: Item description
        picture_url: URL of the item picture
        category_id: Category identifier
        quantity: Quantity of items
        unit_price: Price per unit
    """
    
    def __init__(
        self,
        id: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        picture_url: Optional[str] = None,
        category_id: Optional[str] = None,
        quantity: Optional[int] = None,
        unit_price: Optional[float] = None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.picture_url = picture_url
        self.category_id = category_id
        self.quantity = quantity
        self.unit_price = unit_price
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert PaymentItem to dictionary."""
        data = {}
        if self.id is not None:
            data["id"] = self.id
        if self.title is not None:
            data["title"] = self.title
        if self.description is not None:
            data["description"] = self.description
        if self.picture_url is not None:
            data["picture_url"] = self.picture_url
        if self.category_id is not None:
            data["category_id"] = self.category_id
        if self.quantity is not None:
            data["quantity"] = self.quantity
        if self.unit_price is not None:
            data["unit_price"] = self.unit_price
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PaymentItem":
        """Create PaymentItem from dictionary."""
        return cls(
            id=data.get("id"),
            title=data.get("title"),
            description=data.get("description"),
            picture_url=data.get("picture_url"),
            category_id=data.get("category_id"),
            quantity=data.get("quantity"),
            unit_price=data.get("unit_price")
        )


class PaymentPayer:
    """
    Represents payer information for fraud scoring.
    
    Attributes:
        first_name: Payer's first name
        last_name: Payer's last name
        phone: Payer's phone information
        address: Payer's address information
    """
    
    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[Dict[str, Any]] = None,
        address: Optional[Dict[str, Any]] = None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone or {}
        self.address = address or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert PaymentPayer to dictionary."""
        data = {}
        if self.first_name is not None:
            data["first_name"] = self.first_name
        if self.last_name is not None:
            data["last_name"] = self.last_name
        if self.phone:
            data["phone"] = self.phone
        if self.address:
            data["address"] = self.address
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PaymentPayer":
        """Create PaymentPayer from dictionary."""
        return cls(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            phone=data.get("phone"),
            address=data.get("address")
        )


class PaymentShipments:
    """
    Represents shipment information for a payment.
    
    Attributes:
        receiver_address: Address where the shipment will be received
    """
    
    def __init__(self, receiver_address: Optional[Dict[str, Any]] = None):
        self.receiver_address = receiver_address or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert PaymentShipments to dictionary."""
        data = {}
        if self.receiver_address:
            data["receiver_address"] = self.receiver_address
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PaymentShipments":
        """Create PaymentShipments from dictionary."""
        return cls(receiver_address=data.get("receiver_address"))


class PaymentAdditionalInfo(Resource):
    """
    PaymentAdditionalInfo resource for MercadoPago API.
    
    This resource handles additional information for payments including
    items, payer details, and shipment information. This data is primarily
    used for fraud scoring and risk assessment.
    
    Attributes:
        items: List of PaymentItem objects
        payer: PaymentPayer object with payer information
        shipments: PaymentShipments object with shipment information
    """
    
    def __init__(self, client):
        """
        Initialize PaymentAdditionalInfo resource.
        
        Args:
            client: MercadoPago client instance
        """
        super().__init__(client)
        self._items: List[PaymentItem] = []
        self._payer: Optional[PaymentPayer] = None
        self._shipments: Optional[PaymentShipments] = None
    
    @property
    def items(self) -> List[PaymentItem]:
        """Get the list of payment items."""
        return self._items
    
    @items.setter
    def items(self, value: List[PaymentItem]):
        """Set the list of payment items."""
        self._items = value if value is not None else []
    
    @property
    def payer(self) -> Optional[PaymentPayer]:
        """Get the payer information."""
        return self._payer
    
    @payer.setter
    def payer(self, value: Optional[PaymentPayer]):
        """Set the payer information."""
        self._payer = value
    
    @property
    def shipments(self) -> Optional[PaymentShipments]:
        """Get the shipments information."""
        return self._shipments
    
    @shipments.setter
    def shipments(self, value: Optional[PaymentShipments]):
        """Set the shipments information."""
        self._shipments = value
    
    def add_item(
        self,
        id: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        picture_url: Optional[str] = None,
        category_id: Optional[str] = None,
        quantity: Optional[int] = None,
        unit_price: Optional[float] = None
    ) -> "PaymentAdditionalInfo":
        """
        Add an item to the payment.
        
        Args:
            id: Item identifier
            title: Item title
            description: Item description
            picture_url: URL of the item picture
            category_id: Category identifier
            quantity: Quantity of items
            unit_price: Price per unit
            
        Returns:
            Self for method chaining
        """
        item = PaymentItem(
            id=id,
            title=title,
            description=description,
            picture_url=picture_url,
            category_id=category_id,
            quantity=quantity,
            unit_price=unit_price
        )
        self._items.append(item)
        return self
    
    def set_payer(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[Dict[str, Any]] = None,
        address: Optional[Dict[str, Any]] = None
    ) -> "PaymentAdditionalInfo":
        """
        Set payer information.
        
        Args:
            first_name: Payer's first name
            last_name: Payer's last name
            phone: Payer's phone information
            address: Payer's address information
            
        Returns:
            Self for method chaining
        """
        self._payer = PaymentPayer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address
        )
        return self
    
    def set_shipments(
        self,
        receiver_address: Optional[Dict[str, Any]] = None
    ) -> "PaymentAdditionalInfo":
        """
        Set shipments information.
        
        Args:
            receiver_address: Address where the shipment will be received
            
        Returns:
            Self for method chaining
        """
        self._shipments = PaymentShipments(receiver_address=receiver_address)
        return self
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert PaymentAdditionalInfo to dictionary.
        
        Returns:
            Dictionary representation of the additional info
        """
        data = {}
        
        if self._items:
            data["items"] = [item.to_dict() for item in self._items]
        
        if self._payer is not None:
            data["payer"] = self._payer.to_dict()
        
        if self._shipments is not None:
            data["shipments"] = self._shipments.to_dict()
        
        return data
    
    @classmethod
    def from_dict(cls, client, data: Dict[str, Any]) -> "PaymentAdditionalInfo":
        """
        Create PaymentAdditionalInfo from dictionary.
        
        Args:
            client: MercadoPago client instance
            data: Dictionary with additional info data
            
        Returns:
            PaymentAdditionalInfo instance
        """
        instance = cls(client)
        
        if "items" in data:
            instance._items = [
                PaymentItem.from_dict(item) for item in data["items"]
            ]
        
        if "payer" in data:
            instance._payer = PaymentPayer.from_dict(data["payer"])
        
        if "shipments" in data:
            instance._shipments = PaymentShipments.from_dict(data["shipments"])
        
        return instance
    
    def validate(self) -> bool:
        """
        Validate the additional info data.
        
        Returns:
            True if data is valid, False otherwise
        """
        # Basic validation - can be extended based on requirements
        if self._items:
            for item in self._items:
                if item.quantity is not None and item.quantity < 0:
                    return False
                if item.unit_price is not None and item.unit_price < 0:
                    return False
        
        return True
    
    def clear(self) -> "PaymentAdditionalInfo":
        """
        Clear all additional info data.
        
        Returns:
            Self for method chaining
        """
        self._items = []
        self._payer = None
        self._shipments = None
        return self