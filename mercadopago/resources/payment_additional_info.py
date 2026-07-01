"""
MercadoPago Payment Additional Info Resource.

This module provides the PaymentAdditionalInfo resource for handling additional
information related to payments, particularly useful for fraud scoring.
"""

from mercadopago.core import MPBase


class PaymentItem(MPBase):
    """
    Represents an item in a payment.
    
    Attributes:
        id (str): Item identifier.
        title (str): Item title.
        description (str): Item description.
        picture_url (str): URL of the item picture.
        category_id (str): Item category identifier.
        quantity (int): Item quantity.
        unit_price (float): Unit price of the item.
    """
    
    @classmethod
    def _get_schema(cls):
        """Get the schema for payment item validation."""
        return {
            "id": str,
            "title": str,
            "description": str,
            "picture_url": str,
            "category_id": str,
            "quantity": int,
            "unit_price": (int, float)
        }


class Payer(MPBase):
    """
    Represents payer information.
    
    Attributes:
        first_name (str): Payer's first name.
        last_name (str): Payer's last name.
        phone (object): Phone information with area_code and number.
        address (object): Address information with zip_code, street_name, and street_number.
    """
    
    @classmethod
    def _get_schema(cls):
        """Get the schema for payer validation."""
        return {
            "first_name": str,
            "last_name": str,
            "phone": {
                "area_code": str,
                "number": str
            },
            "address": {
                "zip_code": str,
                "street_name": str,
                "street_number": (int, str)
            }
        }


class Shipments(MPBase):
    """
    Represents shipment information.
    
    Attributes:
        receiver_address (object): Receiver address information with zip_code, 
                                   street_name, street_number, floor, and apartment.
    """
    
    @classmethod
    def _get_schema(cls):
        """Get the schema for shipments validation."""
        return {
            "receiver_address": {
                "zip_code": str,
                "street_name": str,
                "street_number": (int, str),
                "floor": str,
                "apartment": str
            }
        }


class PaymentAdditionalInfo(MPBase):
    """
    Payment Additional Info Resource.
    
    This class handles additional information for payments that can be used
    for fraud scoring and risk analysis in MercadoPago.
    
    Attributes:
        items (list): List of PaymentItem objects representing the items in the payment.
        payer (Payer): Payer object containing payer information.
        shipments (Shipments): Shipments object containing shipping information.
    
    Example:
        >>> from mercadopago import SDK
        >>> sdk = SDK("YOUR_ACCESS_TOKEN")
        >>> 
        >>> additional_info = {
        ...     "items": [
        ...         {
        ...             "id": "item-123",
        ...             "title": "Product Name",
        ...             "description": "Product description",
        ...             "picture_url": "https://example.com/image.jpg",
        ...             "category_id": "electronics",
        ...             "quantity": 1,
        ...             "unit_price": 100.00
        ...         }
        ...     ],
        ...     "payer": {
        ...         "first_name": "John",
        ...         "last_name": "Doe",
        ...         "phone": {
        ...             "area_code": "11",
        ...             "number": "987654321"
        ...         },
        ...         "address": {
        ...             "zip_code": "12345",
        ...             "street_name": "Main Street",
        ...             "street_number": "123"
        ...         }
        ...     },
        ...     "shipments": {
        ...         "receiver_address": {
        ...             "zip_code": "12345",
        ...             "street_name": "Main Street",
        ...             "street_number": "123",
        ...             "floor": "4",
        ...             "apartment": "A"
        ...         }
        ...     }
        ... }
    """
    
    @classmethod
    def _get_schema(cls):
        """Get the schema for payment additional info validation."""
        return {
            "items": [PaymentItem],
            "payer": Payer,
            "shipments": Shipments
        }
    
    def __init__(self, request_options=None):
        """
        Initialize PaymentAdditionalInfo resource.
        
        Args:
            request_options (RequestOptions, optional): Request options for API calls.
        """
        super().__init__(request_options)
        self.items = []
        self.payer = None
        self.shipments = None
    
    def add_item(self, item_data):
        """
        Add an item to the payment additional info.
        
        Args:
            item_data (dict): Dictionary containing item information.
        
        Returns:
            PaymentItem: The created payment item.
        """
        item = PaymentItem()
        for key, value in item_data.items():
            setattr(item, key, value)
        self.items.append(item)
        return item
    
    def set_payer(self, payer_data):
        """
        Set payer information.
        
        Args:
            payer_data (dict): Dictionary containing payer information.
        
        Returns:
            Payer: The created payer object.
        """
        self.payer = Payer()
        for key, value in payer_data.items():
            setattr(self.payer, key, value)
        return self.payer
    
    def set_shipments(self, shipments_data):
        """
        Set shipment information.
        
        Args:
            shipments_data (dict): Dictionary containing shipment information.
        
        Returns:
            Shipments: The created shipments object.
        """
        self.shipments = Shipments()
        for key, value in shipments_data.items():
            setattr(self.shipments, key, value)
        return self.shipments
    
    def to_dict(self):
        """
        Convert the PaymentAdditionalInfo object to a dictionary.
        
        Returns:
            dict: Dictionary representation of the additional info.
        """
        result = {}
        
        if self.items:
            result["items"] = [
                {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
                for item in self.items
            ]
        
        if self.payer:
            result["payer"] = {
                k: v for k, v in self.payer.__dict__.items() 
                if not k.startswith('_')
            }
        
        if self.shipments:
            result["shipments"] = {
                k: v for k, v in self.shipments.__dict__.items() 
                if not k.startswith('_')
            }
        
        return result
    
    @classmethod
    def from_dict(cls, data, request_options=None):
        """
        Create a PaymentAdditionalInfo object from a dictionary.
        
        Args:
            data (dict): Dictionary containing additional info data.
            request_options (RequestOptions, optional): Request options for API calls.
        
        Returns:
            PaymentAdditionalInfo: The created PaymentAdditionalInfo object.
        """
        instance = cls(request_options)
        
        if "items" in data:
            for item_data in data["items"]:
                instance.add_item(item_data)
        
        if "payer" in data:
            instance.set_payer(data["payer"])
        
        if "shipments" in data:
            instance.set_shipments(data["shipments"])
        
        return instance