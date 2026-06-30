"""
PaymentAdditionalInfo resource for MercadoPago SDK.

This module provides the PaymentAdditionalInfo model for including additional
information in payment requests, primarily used for fraud scoring and risk assessment.
"""

from typing import List, Optional
from mercadopago.resources.base import ResourceBase


class PaymentItem:
    """
    Represents an item in a payment.
    
    Attributes:
        id (str): Item identifier.
        title (str): Item title/name.
        description (str): Item description.
        picture_url (str): URL of the item's picture.
        category_id (str): Category identifier.
        quantity (int): Quantity of items.
        unit_price (float): Price per unit.
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
        """
        Initialize a PaymentItem.
        
        Args:
            id: Item identifier.
            title: Item title/name.
            description: Item description.
            picture_url: URL of the item's picture.
            category_id: Category identifier.
            quantity: Quantity of items.
            unit_price: Price per unit.
        """
        self.id = id
        self.title = title
        self.description = description
        self.picture_url = picture_url
        self.category_id = category_id
        self.quantity = quantity
        self.unit_price = unit_price
    
    def to_dict(self) -> dict:
        """
        Convert the PaymentItem to a dictionary.
        
        Returns:
            dict: Dictionary representation of the item.
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


class PayerAddress:
    """
    Represents a payer's address.
    
    Attributes:
        zip_code (str): ZIP/postal code.
        street_name (str): Street name.
        street_number (int): Street number.
    """
    
    def __init__(
        self,
        zip_code: Optional[str] = None,
        street_name: Optional[str] = None,
        street_number: Optional[int] = None
    ):
        """
        Initialize a PayerAddress.
        
        Args:
            zip_code: ZIP/postal code.
            street_name: Street name.
            street_number: Street number.
        """
        self.zip_code = zip_code
        self.street_name = street_name
        self.street_number = street_number
    
    def to_dict(self) -> dict:
        """
        Convert the PayerAddress to a dictionary.
        
        Returns:
            dict: Dictionary representation of the address.
        """
        result = {}
        if self.zip_code is not None:
            result['zip_code'] = self.zip_code
        if self.street_name is not None:
            result['street_name'] = self.street_name
        if self.street_number is not None:
            result['street_number'] = self.street_number
        return result


class Payer:
    """
    Represents payer information.
    
    Attributes:
        first_name (str): Payer's first name.
        last_name (str): Payer's last name.
        phone (dict): Phone information with area_code and number.
        address (PayerAddress): Payer's address.
    """
    
    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[dict] = None,
        address: Optional[PayerAddress] = None
    ):
        """
        Initialize a Payer.
        
        Args:
            first_name: Payer's first name.
            last_name: Payer's last name.
            phone: Phone information dict with 'area_code' and 'number' keys.
            address: Payer's address as PayerAddress object or dict.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        
        if isinstance(address, dict):
            self.address = PayerAddress(**address)
        else:
            self.address = address
    
    def to_dict(self) -> dict:
        """
        Convert the Payer to a dictionary.
        
        Returns:
            dict: Dictionary representation of the payer.
        """
        result = {}
        if self.first_name is not None:
            result['first_name'] = self.first_name
        if self.last_name is not None:
            result['last_name'] = self.last_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.address is not None:
            result['address'] = self.address.to_dict() if hasattr(self.address, 'to_dict') else self.address
        return result


class ReceiverAddress:
    """
    Represents a receiver's address for shipments.
    
    Attributes:
        zip_code (str): ZIP/postal code.
        street_name (str): Street name.
        street_number (int): Street number.
        floor (str): Floor number.
        apartment (str): Apartment number.
    """
    
    def __init__(
        self,
        zip_code: Optional[str] = None,
        street_name: Optional[str] = None,
        street_number: Optional[int] = None,
        floor: Optional[str] = None,
        apartment: Optional[str] = None
    ):
        """
        Initialize a ReceiverAddress.
        
        Args:
            zip_code: ZIP/postal code.
            street_name: Street name.
            street_number: Street number.
            floor: Floor number.
            apartment: Apartment number.
        """
        self.zip_code = zip_code
        self.street_name = street_name
        self.street_number = street_number
        self.floor = floor
        self.apartment = apartment
    
    def to_dict(self) -> dict:
        """
        Convert the ReceiverAddress to a dictionary.
        
        Returns:
            dict: Dictionary representation of the address.
        """
        result = {}
        if self.zip_code is not None:
            result['zip_code'] = self.zip_code
        if self.street_name is not None:
            result['street_name'] = self.street_name
        if self.street_number is not None:
            result['street_number'] = self.street_number
        if self.floor is not None:
            result['floor'] = self.floor
        if self.apartment is not None:
            result['apartment'] = self.apartment
        return result


class Shipments:
    """
    Represents shipment information.
    
    Attributes:
        receiver_address (ReceiverAddress): Receiver's address.
    """
    
    def __init__(self, receiver_address: Optional[ReceiverAddress] = None):
        """
        Initialize Shipments.
        
        Args:
            receiver_address: Receiver's address as ReceiverAddress object or dict.
        """
        if isinstance(receiver_address, dict):
            self.receiver_address = ReceiverAddress(**receiver_address)
        else:
            self.receiver_address = receiver_address
    
    def to_dict(self) -> dict:
        """
        Convert the Shipments to a dictionary.
        
        Returns:
            dict: Dictionary representation of the shipments.
        """
        result = {}
        if self.receiver_address is not None:
            result['receiver_address'] = (
                self.receiver_address.to_dict() 
                if hasattr(self.receiver_address, 'to_dict') 
                else self.receiver_address
            )
        return result


class PaymentAdditionalInfo(ResourceBase):
    """
    PaymentAdditionalInfo resource for including additional information in payments.
    
    This information is primarily used for fraud scoring and risk assessment.
    
    Attributes:
        items (List[PaymentItem]): List of items being purchased.
        payer (Payer): Payer information including name, phone, and address.
        shipments (Shipments): Shipment information with receiver address.
    """
    
    def __init__(
        self,
        items: Optional[List[PaymentItem]] = None,
        payer: Optional[Payer] = None,
        shipments: Optional[Shipments] = None
    ):
        """
        Initialize PaymentAdditionalInfo.
        
        Args:
            items: List of PaymentItem objects or dicts.
            payer: Payer object or dict with payer information.
            shipments: Shipments object or dict with shipment information.
        """
        super().__init__()
        
        # Handle items
        if items is not None:
            self.items = []
            for item in items:
                if isinstance(item, dict):
                    self.items.append(PaymentItem(**item))
                else:
                    self.items.append(item)
        else:
            self.items = None
        
        # Handle payer
        if isinstance(payer, dict):
            self.payer = Payer(**payer)
        else:
            self.payer = payer
        
        # Handle shipments
        if isinstance(shipments, dict):
            self.shipments = Shipments(**shipments)
        else:
            self.shipments = shipments
    
    def to_dict(self) -> dict:
        """
        Convert the PaymentAdditionalInfo to a dictionary.
        
        Returns:
            dict: Dictionary representation of the additional info.
        """
        result = {}
        
        if self.items is not None:
            result['items'] = [
                item.to_dict() if hasattr(item, 'to_dict') else item 
                for item in self.items
            ]
        
        if self.payer is not None:
            result['payer'] = (
                self.payer.to_dict() 
                if hasattr(self.payer, 'to_dict') 
                else self.payer
            )
        
        if self.shipments is not None:
            result['shipments'] = (
                self.shipments.to_dict() 
                if hasattr(self.shipments, 'to_dict') 
                else self.shipments
            )
        
        return result
    
    @classmethod
    def from_dict(cls, data: dict) -> 'PaymentAdditionalInfo':
        """
        Create a PaymentAdditionalInfo instance from a dictionary.
        
        Args:
            data: Dictionary containing additional info data.
        
        Returns:
            PaymentAdditionalInfo: New instance with data from the dictionary.
        """
        return cls(
            items=data.get('items'),
            payer=data.get('payer'),
            shipments=data.get('shipments')
        )