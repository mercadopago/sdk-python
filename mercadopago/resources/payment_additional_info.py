# mercadopago/resources/payment_additional_info.py

from typing import List, Optional
from mercadopago.resources.base import Resource


class PaymentAdditionalInfo(Resource):
    """
    PaymentAdditionalInfo resource for MercadoPago API.
    
    This resource represents additional information for payments,
    used primarily for fraud scoring and risk assessment.
    
    Attributes:
        items (list): List of items included in the payment
        payer (dict): Payer information including personal and contact details
        shipments (dict): Shipment information including receiver address
    """
    
    _resource_name = "payment_additional_info"
    
    class PaymentItem:
        """
        Represents an item in the payment.
        
        Attributes:
            id (str): Item identifier
            title (str): Item title/name
            description (str): Item description
            picture_url (str): URL to item picture
            category_id (str): Item category identifier
            quantity (int): Quantity of items
            unit_price (float): Price per unit
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
        
        def to_dict(self) -> dict:
            """Convert PaymentItem to dictionary."""
            return {
                k: v for k, v in {
                    'id': self.id,
                    'title': self.title,
                    'description': self.description,
                    'picture_url': self.picture_url,
                    'category_id': self.category_id,
                    'quantity': self.quantity,
                    'unit_price': self.unit_price
                }.items() if v is not None
            }
    
    class Payer:
        """
        Represents payer information.
        
        Attributes:
            first_name (str): Payer's first name
            last_name (str): Payer's last name
            phone (dict): Phone information with area_code and number
            address (dict): Address information
        """
        
        def __init__(
            self,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            phone: Optional[dict] = None,
            address: Optional[dict] = None
        ):
            self.first_name = first_name
            self.last_name = last_name
            self.phone = phone or {}
            self.address = address or {}
        
        def to_dict(self) -> dict:
            """Convert Payer to dictionary."""
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
    
    class Shipments:
        """
        Represents shipment information.
        
        Attributes:
            receiver_address (dict): Receiver address information
        """
        
        def __init__(self, receiver_address: Optional[dict] = None):
            self.receiver_address = receiver_address or {}
        
        def to_dict(self) -> dict:
            """Convert Shipments to dictionary."""
            return {'receiver_address': self.receiver_address} if self.receiver_address else {}
    
    def __init__(self, client=None):
        """
        Initialize PaymentAdditionalInfo resource.
        
        Args:
            client: MercadoPago client instance
        """
        super().__init__(client)
        self.items: List[PaymentAdditionalInfo.PaymentItem] = []
        self.payer: Optional[PaymentAdditionalInfo.Payer] = None
        self.shipments: Optional[PaymentAdditionalInfo.Shipments] = None
    
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
        Add an item to the payment additional info.
        
        Args:
            id: Item identifier
            title: Item title/name
            description: Item description
            picture_url: URL to item picture
            category_id: Item category identifier
            quantity: Quantity of items
            unit_price: Price per unit
        
        Returns:
            Self for method chaining
        """
        item = self.PaymentItem(
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
    
    def set_payer(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[dict] = None,
        address: Optional[dict] = None
    ) -> 'PaymentAdditionalInfo':
        """
        Set payer information.
        
        Args:
            first_name: Payer's first name
            last_name: Payer's last name
            phone: Phone information dict with area_code and number
            address: Address information dict
        
        Returns:
            Self for method chaining
        """
        self.payer = self.Payer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address
        )
        return self
    
    def set_shipments(self, receiver_address: Optional[dict] = None) -> 'PaymentAdditionalInfo':
        """
        Set shipment information.
        
        Args:
            receiver_address: Receiver address information dict
        
        Returns:
            Self for method chaining
        """
        self.shipments = self.Shipments(receiver_address=receiver_address)
        return self
    
    def to_dict(self) -> dict:
        """
        Convert PaymentAdditionalInfo to dictionary format.
        
        Returns:
            Dictionary representation of the additional info
        """
        result = {}
        
        if self.items:
            result['items'] = [item.to_dict() for item in self.items]
        
        if self.payer:
            payer_dict = self.payer.to_dict()
            if payer_dict:
                result['payer'] = payer_dict
        
        if self.shipments:
            shipments_dict = self.shipments.to_dict()
            if shipments_dict:
                result['shipments'] = shipments_dict
        
        return result
    
    def validate(self) -> bool:
        """
        Validate the additional info data.
        
        Returns:
            True if valid, False otherwise
        """
        # Items validation
        for item in self.items:
            if item.quantity is not None and item.quantity < 0:
                return False
            if item.unit_price is not None and item.unit_price < 0:
                return False
        
        return True
    
    @classmethod
    def from_dict(cls, data: dict, client=None) -> 'PaymentAdditionalInfo':
        """
        Create PaymentAdditionalInfo instance from dictionary.
        
        Args:
            data: Dictionary containing additional info data
            client: MercadoPago client instance
        
        Returns:
            PaymentAdditionalInfo instance
        """
        instance = cls(client=client)
        
        # Load items
        if 'items' in data:
            for item_data in data['items']:
                instance.add_item(**item_data)
        
        # Load payer
        if 'payer' in data:
            instance.set_payer(**data['payer'])
        
        # Load shipments
        if 'shipments' in data:
            instance.set_shipments(
                receiver_address=data['shipments'].get('receiver_address')
            )
        
        return instance