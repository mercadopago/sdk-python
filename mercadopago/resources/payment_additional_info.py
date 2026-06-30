"""
MercadoPago Payment Additional Info Module.

This module provides functionality for managing additional information
related to payments, which is used for fraud scoring and risk assessment.
"""

from typing import List, Dict, Any, Optional
from mercadopago.resources.base import Resource


class PaymentItem:
    """
    Represents an item in a payment transaction.
    
    Attributes:
        id (str): Item identifier.
        title (str): Item title/name.
        description (str): Item description.
        picture_url (str): URL of the item picture.
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
            picture_url: URL of the item picture.
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
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert PaymentItem to dictionary.
        
        Returns:
            Dictionary representation of the payment item.
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


class PayerInfo:
    """
    Represents payer information for fraud scoring.
    
    Attributes:
        first_name (str): Payer's first name.
        last_name (str): Payer's last name.
        phone (dict): Phone information with area_code and number.
        address (dict): Address information including street_name, street_number, zip_code.
    """
    
    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[Dict[str, str]] = None,
        address: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize PayerInfo.
        
        Args:
            first_name: Payer's first name.
            last_name: Payer's last name.
            phone: Phone information dictionary.
            address: Address information dictionary.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone or {}
        self.address = address or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert PayerInfo to dictionary.
        
        Returns:
            Dictionary representation of the payer information.
        """
        data = {}
        if self.first_name is not None:
            data['first_name'] = self.first_name
        if self.last_name is not None:
            data['last_name'] = self.last_name
        if self.phone:
            data['phone'] = self.phone
        if self.address:
            data['address'] = self.address
        return data


class ShipmentInfo:
    """
    Represents shipment information for a payment.
    
    Attributes:
        receiver_address (dict): Receiver address information including street_name,
                                street_number, zip_code, city_name, state_name, etc.
    """
    
    def __init__(self, receiver_address: Optional[Dict[str, Any]] = None):
        """
        Initialize ShipmentInfo.
        
        Args:
            receiver_address: Receiver address information dictionary.
        """
        self.receiver_address = receiver_address or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert ShipmentInfo to dictionary.
        
        Returns:
            Dictionary representation of the shipment information.
        """
        data = {}
        if self.receiver_address:
            data['receiver_address'] = self.receiver_address
        return data


class PaymentAdditionalInfo(Resource):
    """
    Payment Additional Information resource for MercadoPago API.
    
    This resource manages additional information related to payments,
    which is particularly useful for fraud scoring and risk assessment.
    It includes details about items, payer information, and shipment details.
    """
    
    def __init__(self, client):
        """
        Initialize PaymentAdditionalInfo resource.
        
        Args:
            client: MercadoPago client instance.
        """
        super().__init__(client)
        self._endpoint = "/v1/payments"
    
    def create_additional_info(
        self,
        items: Optional[List[PaymentItem]] = None,
        payer: Optional[PayerInfo] = None,
        shipments: Optional[ShipmentInfo] = None
    ) -> Dict[str, Any]:
        """
        Create additional info structure for a payment.
        
        Args:
            items: List of PaymentItem objects.
            payer: PayerInfo object with payer details.
            shipments: ShipmentInfo object with shipment details.
        
        Returns:
            Dictionary containing the additional info structure.
        """
        additional_info = {}
        
        if items:
            additional_info['items'] = [item.to_dict() for item in items]
        
        if payer:
            additional_info['payer'] = payer.to_dict()
        
        if shipments:
            additional_info['shipments'] = shipments.to_dict()
        
        return additional_info
    
    def validate_additional_info(self, additional_info: Dict[str, Any]) -> bool:
        """
        Validate the structure of additional info.
        
        Args:
            additional_info: Dictionary containing additional info to validate.
        
        Returns:
            True if the structure is valid, False otherwise.
        """
        if not isinstance(additional_info, dict):
            return False
        
        # Validate items structure
        if 'items' in additional_info:
            if not isinstance(additional_info['items'], list):
                return False
            for item in additional_info['items']:
                if not isinstance(item, dict):
                    return False
        
        # Validate payer structure
        if 'payer' in additional_info:
            if not isinstance(additional_info['payer'], dict):
                return False
        
        # Validate shipments structure
        if 'shipments' in additional_info:
            if not isinstance(additional_info['shipments'], dict):
                return False
        
        return True
    
    def add_to_payment_data(
        self,
        payment_data: Dict[str, Any],
        items: Optional[List[PaymentItem]] = None,
        payer: Optional[PayerInfo] = None,
        shipments: Optional[ShipmentInfo] = None
    ) -> Dict[str, Any]:
        """
        Add additional info to existing payment data.
        
        Args:
            payment_data: Existing payment data dictionary.
            items: List of PaymentItem objects.
            payer: PayerInfo object with payer details.
            shipments: ShipmentInfo object with shipment details.
        
        Returns:
            Updated payment data with additional info included.
        """
        additional_info = self.create_additional_info(items, payer, shipments)
        
        if additional_info:
            payment_data['additional_info'] = additional_info
        
        return payment_data