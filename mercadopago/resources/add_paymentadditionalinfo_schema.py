"""
MercadoPago PaymentAdditionalInfo Schema Module.

This module defines the PaymentAdditionalInfo model used for fraud scoring
with additional information about payment items, payer details, and shipments.
"""

from mercadopago.resources.base import MPBase


class PaymentItem(MPBase):
    """
    Payment Item model.
    
    Represents an individual item in a payment transaction.
    """
    
    def __init__(self, client=None):
        """
        Initialize PaymentItem.
        
        Args:
            client: MercadoPago client instance
        """
        super().__init__(client)
        self._schema = {
            "id": str,
            "title": str,
            "description": str,
            "picture_url": str,
            "category_id": str,
            "quantity": int,
            "unit_price": float,
        }


class Payer(MPBase):
    """
    Payer model.
    
    Represents payer information including personal details and address.
    """
    
    def __init__(self, client=None):
        """
        Initialize Payer.
        
        Args:
            client: MercadoPago client instance
        """
        super().__init__(client)
        self._schema = {
            "first_name": str,
            "last_name": str,
            "phone": dict,
            "address": dict,
            "registration_date": str,
        }


class Shipments(MPBase):
    """
    Shipments model.
    
    Represents shipment information including receiver address.
    """
    
    def __init__(self, client=None):
        """
        Initialize Shipments.
        
        Args:
            client: MercadoPago client instance
        """
        super().__init__(client)
        self._schema = {
            "receiver_address": dict,
        }


class PaymentAdditionalInfo(MPBase):
    """
    PaymentAdditionalInfo model.
    
    This model contains additional information used for fraud scoring,
    including items, payer details, and shipment information.
    """
    
    def __init__(self, client=None):
        """
        Initialize PaymentAdditionalInfo.
        
        Args:
            client: MercadoPago client instance
        """
        super().__init__(client)
        self._schema = {
            "items": list,
            "payer": dict,
            "shipments": dict,
            "ip_address": str,
        }
    
    def validate(self, data):
        """
        Validate PaymentAdditionalInfo data.
        
        Args:
            data (dict): Data to validate
            
        Returns:
            bool: True if valid, False otherwise
            
        Raises:
            ValueError: If validation fails
        """
        if not isinstance(data, dict):
            raise ValueError("PaymentAdditionalInfo data must be a dictionary")
        
        # Validate items if present
        if "items" in data:
            if not isinstance(data["items"], list):
                raise ValueError("items must be a list")
            for item in data["items"]:
                if not isinstance(item, dict):
                    raise ValueError("Each item must be a dictionary")
        
        # Validate payer if present
        if "payer" in data:
            if not isinstance(data["payer"], dict):
                raise ValueError("payer must be a dictionary")
            required_payer_fields = ["first_name", "last_name"]
            for field in required_payer_fields:
                if field in data["payer"] and not isinstance(data["payer"][field], str):
                    raise ValueError(f"payer.{field} must be a string")
        
        # Validate shipments if present
        if "shipments" in data:
            if not isinstance(data["shipments"], dict):
                raise ValueError("shipments must be a dictionary")
            if "receiver_address" in data["shipments"]:
                if not isinstance(data["shipments"]["receiver_address"], dict):
                    raise ValueError("shipments.receiver_address must be a dictionary")
        
        return True
    
    def create_item(self, **kwargs):
        """
        Create a payment item.
        
        Args:
            **kwargs: Item properties (id, title, description, etc.)
            
        Returns:
            dict: Created item data
        """
        item = PaymentItem(self._client)
        item_data = {}
        
        for key, value in kwargs.items():
            if key in item._schema:
                item_data[key] = value
        
        return item_data
    
    def create_payer(self, **kwargs):
        """
        Create payer information.
        
        Args:
            **kwargs: Payer properties (first_name, last_name, phone, address)
            
        Returns:
            dict: Created payer data
        """
        payer = Payer(self._client)
        payer_data = {}
        
        for key, value in kwargs.items():
            if key in payer._schema:
                payer_data[key] = value
        
        return payer_data
    
    def create_shipments(self, **kwargs):
        """
        Create shipment information.
        
        Args:
            **kwargs: Shipment properties (receiver_address)
            
        Returns:
            dict: Created shipment data
        """
        shipments = Shipments(self._client)
        shipments_data = {}
        
        for key, value in kwargs.items():
            if key in shipments._schema:
                shipments_data[key] = value
        
        return shipments_data