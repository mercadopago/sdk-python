"""
PaymentAdditionalInfo resource for MercadoPago SDK.

This module provides the PaymentAdditionalInfo model which contains additional
information about a payment used for fraud scoring and risk analysis.
"""

from typing import List, Optional
from mercadopago.resources.base import ResourceBase


class PaymentItem:
    """
    Represents an item in a payment.
    
    Attributes:
        id (str): Item identifier.
        title (str): Item title.
        description (str): Item description.
        picture_url (str): URL of the item picture.
        category_id (str): Item category identifier.
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
            title: Item title.
            description: Item description.
            picture_url: URL of the item picture.
            category_id: Item category identifier.
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
        data = {}
        if self.id is not None:
            data['id'] = self.id
        if self.title is not None:
            data['title'] = self.title
        if self.description is not None:
            data['description'] = self.description
        if self.picture_url is not None:
            data['picture_url'] = self.picture_url
        if self.category_id is not None:
            data['category_id'] = self.category_id
        if self.quantity is not None:
            data['quantity'] = self.quantity
        if self.unit_price is not None:
            data['unit_price'] = self.unit_price
        return data


class PayerAddress:
    """
    Represents a payer's address.
    
    Attributes:
        zip_code (str): ZIP code.
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
            zip_code: ZIP code.
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
        data = {}
        if self.zip_code is not None:
            data['zip_code'] = self.zip_code
        if self.street_name is not None:
            data['street_name'] = self.street_name
        if self.street_number is not None:
            data['street_number'] = self.street_number
        return data


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
            phone: Phone information dictionary with area_code and number.
            address: Payer's address.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
    
    def to_dict(self) -> dict:
        """
        Convert the Payer to a dictionary.
        
        Returns:
            dict: Dictionary representation of the payer.
        """
        data = {}
        if self.first_name is not None:
            data['first_name'] = self.first_name
        if self.last_name is not None:
            data['last_name'] = self.last_name
        if self.phone is not None:
            data['phone'] = self.phone
        if self.address is not None:
            data['address'] = self.address.to_dict() if isinstance(self.address, PayerAddress) else self.address
        return data


class ReceiverAddress:
    """
    Represents a receiver's address for shipments.
    
    Attributes:
        zip_code (str): ZIP code.
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
            zip_code: ZIP code.
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
        data = {}
        if self.zip_code is not None:
            data['zip_code'] = self.zip_code
        if self.street_name is not None:
            data['street_name'] = self.street_name
        if self.street_number is not None:
            data['street_number'] = self.street_number
        if self.floor is not None:
            data['floor'] = self.floor
        if self.apartment is not None:
            data['apartment'] = self.apartment
        return data


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
            receiver_address: Receiver's address.
        """
        self.receiver_address = receiver_address
    
    def to_dict(self) -> dict:
        """
        Convert the Shipments to a dictionary.
        
        Returns:
            dict: Dictionary representation of the shipments.
        """
        data = {}
        if self.receiver_address is not None:
            data['receiver_address'] = (
                self.receiver_address.to_dict() 
                if isinstance(self.receiver_address, ReceiverAddress) 
                else self.receiver_address
            )
        return data


class PaymentAdditionalInfo(ResourceBase):
    """
    PaymentAdditionalInfo resource for fraud scoring and risk analysis.
    
    This model contains additional information about a payment that is used
    by MercadoPago's fraud detection system to score and analyze transaction risk.
    
    Attributes:
        items (List[PaymentItem]): List of items in the payment.
        payer (Payer): Payer information including name, phone, and address.
        shipments (Shipments): Shipment information including receiver address.
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
            items: List of PaymentItem objects.
            payer: Payer object with personal information.
            shipments: Shipments object with delivery information.
        """
        super().__init__()
        self.items = items or []
        self.payer = payer
        self.shipments = shipments
    
    def to_dict(self) -> dict:
        """
        Convert the PaymentAdditionalInfo to a dictionary.
        
        Returns:
            dict: Dictionary representation of the additional info.
        """
        data = {}
        
        if self.items:
            data['items'] = [
                item.to_dict() if isinstance(item, PaymentItem) else item 
                for item in self.items
            ]
        
        if self.payer is not None:
            data['payer'] = self.payer.to_dict() if isinstance(self.payer, Payer) else self.payer
        
        if self.shipments is not None:
            data['shipments'] = (
                self.shipments.to_dict() 
                if isinstance(self.shipments, Shipments) 
                else self.shipments
            )
        
        return data
    
    @classmethod
    def from_dict(cls, data: dict) -> 'PaymentAdditionalInfo':
        """
        Create a PaymentAdditionalInfo instance from a dictionary.
        
        Args:
            data: Dictionary containing payment additional info data.
        
        Returns:
            PaymentAdditionalInfo: New instance populated with the provided data.
        """
        items = None
        if 'items' in data and data['items']:
            items = [
                PaymentItem(**item) if isinstance(item, dict) else item
                for item in data['items']
            ]
        
        payer = None
        if 'payer' in data and data['payer']:
            payer_data = data['payer']
            if isinstance(payer_data, dict):
                address = None
                if 'address' in payer_data and payer_data['address']:
                    address = PayerAddress(**payer_data['address'])
                payer = Payer(
                    first_name=payer_data.get('first_name'),
                    last_name=payer_data.get('last_name'),
                    phone=payer_data.get('phone'),
                    address=address
                )
            else:
                payer = payer_data
        
        shipments = None
        if 'shipments' in data and data['shipments']:
            shipments_data = data['shipments']
            if isinstance(shipments_data, dict):
                receiver_address = None
                if 'receiver_address' in shipments_data and shipments_data['receiver_address']:
                    receiver_address = ReceiverAddress(**shipments_data['receiver_address'])
                shipments = Shipments(receiver_address=receiver_address)
            else:
                shipments = shipments_data
        
        return cls(items=items, payer=payer, shipments=shipments)
    
    def add_item(
        self,
        id: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        picture_url: Optional[str] = None,
        category_id: Optional[str] = None,
        quantity: Optional[int] = None,
        unit_price: Optional[float] = None
    ) -> 'PaymentAdditionalInfo':
        """
        Add an item to the items list.
        
        Args:
            id: Item identifier.
            title: Item title.
            description: Item description.
            picture_url: URL of the item picture.
            category_id: Item category identifier.
            quantity: Quantity of items.
            unit_price: Price per unit.
        
        Returns:
            PaymentAdditionalInfo: Self for method chaining.
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
        self.items.append(item)
        return self