"""
MercadoPago Payment Additional Info Resource.

This module provides the PaymentAdditionalInfo resource for managing
additional payment information used for fraud scoring.
"""

from typing import Any, Dict, List, Optional

from mercadopago.resources.base import ResourceBase


class PaymentItem:
    """
    Represents an item in a payment.
    
    Attributes:
        id (str): Item identifier.
        title (str): Item title.
        description (str): Item description.
        picture_url (str): Item picture URL.
        category_id (str): Item category identifier.
        quantity (int): Item quantity.
        unit_price (float): Item unit price.
    """
    
    def __init__(
        self,
        id: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        picture_url: Optional[str] = None,
        category_id: Optional[str] = None,
        quantity: Optional[int] = None,
        unit_price: Optional[float] = None,
        **kwargs
    ):
        """
        Initialize a PaymentItem.
        
        Args:
            id: Item identifier.
            title: Item title.
            description: Item description.
            picture_url: Item picture URL.
            category_id: Item category identifier.
            quantity: Item quantity.
            unit_price: Item unit price.
            **kwargs: Additional item attributes.
        """
        self.id = id
        self.title = title
        self.description = description
        self.picture_url = picture_url
        self.category_id = category_id
        self.quantity = quantity
        self.unit_price = unit_price
        
        # Store any additional attributes
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the PaymentItem to a dictionary.
        
        Returns:
            Dictionary representation of the payment item.
        """
        result = {}
        
        if self.id is not None:
            result['id'] = self.id
        if self.title is not None:
            result['title'] = self.title
        if self.description is not None:
            result['description'] = self.description
        if self.picture_url is not None:
            result['picture_url'] = self.picture_url
        if self.category_id is not None:
            result['category_id'] = self.category_id
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.unit_price is not None:
            result['unit_price'] = self.unit_price
        
        return result
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PaymentItem':
        """
        Create a PaymentItem from a dictionary.
        
        Args:
            data: Dictionary containing payment item data.
        
        Returns:
            PaymentItem instance.
        """
        return cls(**data)


class Payer:
    """
    Represents a payer in a payment.
    
    Attributes:
        first_name (str): Payer's first name.
        last_name (str): Payer's last name.
        phone (dict): Payer's phone information.
        address (dict): Payer's address information.
    """
    
    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[Dict[str, Any]] = None,
        address: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        """
        Initialize a Payer.
        
        Args:
            first_name: Payer's first name.
            last_name: Payer's last name.
            phone: Payer's phone information (e.g., {"area_code": "11", "number": "12345678"}).
            address: Payer's address information.
            **kwargs: Additional payer attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone or {}
        self.address = address or {}
        
        # Store any additional attributes
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Payer to a dictionary.
        
        Returns:
            Dictionary representation of the payer.
        """
        result = {}
        
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        if self.phone:
            result['phone'] = self.phone
        if self.address:
            result['address'] = self.address
        
        return result
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Payer':
        """
        Create a Payer from a dictionary.
        
        Args:
            data: Dictionary containing payer data.
        
        Returns:
            Payer instance.
        """
        return cls(**data)


class Shipments:
    """
    Represents shipment information in a payment.
    
    Attributes:
        receiver_address (dict): Receiver's address information.
    """
    
    def __init__(
        self,
        receiver_address: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        """
        Initialize Shipments.
        
        Args:
            receiver_address: Receiver's address information.
            **kwargs: Additional shipment attributes.
        """
        self.receiver_address = receiver_address or {}
        
        # Store any additional attributes
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Shipments to a dictionary.
        
        Returns:
            Dictionary representation of the shipments.
        """
        result = {}
        
        if self.receiver_address:
            result['receiver_address'] = self.receiver_address
        
        return result
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Shipments':
        """
        Create Shipments from a dictionary.
        
        Args:
            data: Dictionary containing shipments data.
        
        Returns:
            Shipments instance.
        """
        return cls(**data)


class PaymentAdditionalInfo(ResourceBase):
    """
    MercadoPago Payment Additional Info Resource.
    
    This resource handles additional payment information used for fraud scoring,
    including items, payer information, and shipment details.
    
    Attributes:
        items (list): List of PaymentItem objects.
        payer (Payer): Payer information object.
        shipments (Shipments): Shipment information object.
    """
    
    _resource_name = "payment_additional_info"
    
    def __init__(self, client):
        """
        Initialize the PaymentAdditionalInfo resource.
        
        Args:
            client: MercadoPago client instance.
        """
        super().__init__(client)
        self.items: List[PaymentItem] = []
        self.payer: Optional[Payer] = None
        self.shipments: Optional[Shipments] = None
    
    def add_item(
        self,
        id: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        picture_url: Optional[str] = None,
        category_id: Optional[str] = None,
        quantity: Optional[int] = None,
        unit_price: Optional[float] = None,
        **kwargs
    ) -> 'PaymentAdditionalInfo':
        """
        Add an item to the payment additional info.
        
        Args:
            id: Item identifier.
            title: Item title.
            description: Item description.
            picture_url: Item picture URL.
            category_id: Item category identifier.
            quantity: Item quantity.
            unit_price: Item unit price.
            **kwargs: Additional item attributes.
        
        Returns:
            Self for method chaining.
        """
        item = PaymentItem(
            id=id,
            title=title,
            description=description,
            picture_url=picture_url,
            category_id=category_id,
            quantity=quantity,
            unit_price=unit_price,
            **kwargs
        )
        self.items.append(item)
        return self
    
    def set_payer(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[Dict[str, Any]] = None,
        address: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> 'PaymentAdditionalInfo':
        """
        Set payer information.
        
        Args:
            first_name: Payer's first name.
            last_name: Payer's last name.
            phone: Payer's phone information.
            address: Payer's address information.
            **kwargs: Additional payer attributes.
        
        Returns:
            Self for method chaining.
        """
        self.payer = Payer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            **kwargs
        )
        return self
    
    def set_shipments(
        self,
        receiver_address: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> 'PaymentAdditionalInfo':
        """
        Set shipment information.
        
        Args:
            receiver_address: Receiver's address information.
            **kwargs: Additional shipment attributes.
        
        Returns:
            Self for method chaining.
        """
        self.shipments = Shipments(
            receiver_address=receiver_address,
            **kwargs
        )
        return self
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the PaymentAdditionalInfo to a dictionary.
        
        Returns:
            Dictionary representation of the payment additional info.
        """
        result = {}
        
        if self.items:
            result['items'] = [item.to_dict() for item in self.items]
        
        if self.payer:
            result['payer'] = self.payer.to_dict()
        
        if self.shipments:
            result['shipments'] = self.shipments.to_dict()
        
        return result
    
    def from_dict(self, data: Dict[str, Any]) -> 'PaymentAdditionalInfo':
        """
        Populate the PaymentAdditionalInfo from a dictionary.
        
        Args:
            data: Dictionary containing payment additional info data.
        
        Returns:
            Self for method chaining.
        """
        if 'items' in data:
            self.items = [PaymentItem.from_dict(item) for item in data['items']]
        
        if 'payer' in data:
            self.payer = Payer.from_dict(data['payer'])
        
        if 'shipments' in data:
            self.shipments = Shipments.from_dict(data['shipments'])
        
        return self
    
    def clear(self) -> 'PaymentAdditionalInfo':
        """
        Clear all additional info data.
        
        Returns:
            Self for method chaining.
        """
        self.items = []
        self.payer = None
        self.shipments = None
        return self
    
    def validate(self) -> bool:
        """
        Validate the payment additional info data.
        
        Returns:
            True if valid, False otherwise.
        """
        # Basic validation - can be extended as needed
        if self.items:
            for item in self.items:
                if item.quantity is not None and item.quantity < 0:
                    return False
                if item.unit_price is not None and item.unit_price < 0:
                    return False
        
        return True