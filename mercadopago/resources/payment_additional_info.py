```python
"""
MercadoPago Payment Additional Info Resource.

This module contains the PaymentAdditionalInfo resource model used for fraud scoring.
"""

from typing import List, Optional
from mercadopago.resources.base import Resource


class PaymentItem(Resource):
    """
    Payment Item model.
    
    Represents an item in a payment transaction.
    """
    
    def __init__(self, **kwargs):
        """
        Initialize a PaymentItem.
        
        Args:
            **kwargs: Arbitrary keyword arguments for item attributes.
        """
        super().__init__(**kwargs)
        self.id: Optional[str] = kwargs.get('id')
        self.title: Optional[str] = kwargs.get('title')
        self.description: Optional[str] = kwargs.get('description')
        self.picture_url: Optional[str] = kwargs.get('picture_url')
        self.category_id: Optional[str] = kwargs.get('category_id')
        self.quantity: Optional[int] = kwargs.get('quantity')
        self.unit_price: Optional[float] = kwargs.get('unit_price')


class PayerAddress(Resource):
    """
    Payer Address model.
    
    Represents the address information of a payer.
    """
    
    def __init__(self, **kwargs):
        """
        Initialize a PayerAddress.
        
        Args:
            **kwargs: Arbitrary keyword arguments for address attributes.
        """
        super().__init__(**kwargs)
        self.zip_code: Optional[str] = kwargs.get('zip_code')
        self.street_name: Optional[str] = kwargs.get('street_name')
        self.street_number: Optional[str] = kwargs.get('street_number')


class Payer(Resource):
    """
    Payer model.
    
    Represents the payer information in a payment transaction.
    """
    
    def __init__(self, **kwargs):
        """
        Initialize a Payer.
        
        Args:
            **kwargs: Arbitrary keyword arguments for payer attributes.
        """
        super().__init__(**kwargs)
        self.first_name: Optional[str] = kwargs.get('first_name')
        self.last_name: Optional[str] = kwargs.get('last_name')
        self.phone: Optional[dict] = kwargs.get('phone')
        
        # Handle address as nested object
        address_data = kwargs.get('address')
        if address_data and isinstance(address_data, dict):
            self.address: Optional[PayerAddress] = PayerAddress(**address_data)
        else:
            self.address: Optional[PayerAddress] = address_data


class ReceiverAddress(Resource):
    """
    Receiver Address model.
    
    Represents the receiver address for shipment.
    """
    
    def __init__(self, **kwargs):
        """
        Initialize a ReceiverAddress.
        
        Args:
            **kwargs: Arbitrary keyword arguments for address attributes.
        """
        super().__init__(**kwargs)
        self.zip_code: Optional[str] = kwargs.get('zip_code')
        self.street_name: Optional[str] = kwargs.get('street_name')
        self.street_number: Optional[str] = kwargs.get('street_number')
        self.floor: Optional[str] = kwargs.get('floor')
        self.apartment: Optional[str] = kwargs.get('apartment')


class Shipment(Resource):
    """
    Shipment model.
    
    Represents shipment information in a payment transaction.
    """
    
    def __init__(self, **kwargs):
        """
        Initialize a Shipment.
        
        Args:
            **kwargs: Arbitrary keyword arguments for shipment attributes.
        """
        super().__init__(**kwargs)
        
        # Handle receiver_address as nested object
        receiver_address_data = kwargs.get('receiver_address')
        if receiver_address_data and isinstance(receiver_address_data, dict):
            self.receiver_address: Optional[ReceiverAddress] = ReceiverAddress(**receiver_address_data)
        else:
            self.receiver_address: Optional[ReceiverAddress] = receiver_address_data


class PaymentAdditionalInfo(Resource):
    """
    Payment Additional Info model.
    
    This model contains additional information about a payment transaction
    used for fraud scoring and risk assessment.
    """
    
    def __init__(self, **kwargs):
        """
        Initialize PaymentAdditionalInfo.
        
        Args:
            **kwargs: Arbitrary keyword arguments for additional info attributes.
        """
        super().__init__(**kwargs)
        
        # Handle items as list of PaymentItem objects
        items_data = kwargs.get('items', [])
        self.items: List[PaymentItem] = []
        if items_data:
            for item in items_data:
                if isinstance(item, dict):
                    self.items.append(PaymentItem(**item))
                elif isinstance(item, PaymentItem):
                    self.items.append(item)
        
        # Handle payer as nested object
        payer_data = kwargs.get('payer')
        if payer_data and isinstance(payer_data, dict):
            self.payer: Optional[Payer] = Payer(**payer_data)
        else:
            self.payer: Optional[Payer] = payer_data
        
        # Handle shipments as nested object
        shipments_data = kwargs.get('shipments')
        if shipments_data and isinstance(shipments_data, dict):
            self.shipments: Optional[Shipment] = Shipment(**shipments_data)
        else:
            self.shipments: Optional[Shipment] = shipments_data
    
    def to_dict(self) -> dict:
        """
        Convert the PaymentAdditionalInfo object to a dictionary.
        
        Returns:
            dict: Dictionary representation of the object.
        """
        result = {}
        
        if self.items:
            result['items'] = [
                item.to_dict() if hasattr(item, 'to_dict') else item
                for item in self.items
            ]
        
        if self.payer:
            result['payer'] = self.payer.to_dict() if hasattr(self.payer, 'to_dict') else self.payer
        
        if self.shipments:
            result['shipments'] = self.shipments.to_dict() if hasattr(self.shipments, 'to_dict') else self.shipments
        
        return result

```