"""
MercadoPago Payment Additional Info resource module.

This module provides the PaymentAdditionalInfo resource for handling
additional information related to payments, used for fraud scoring.
"""

from typing import Optional, List, Dict, Any
from mercadopago.resources.base import ResourceBase


class PaymentAdditionalInfo(ResourceBase):
    """
    PaymentAdditionalInfo resource for handling additional payment information.
    
    This resource manages additional information that can be attached to payments
    for fraud prevention and scoring purposes.
    
    Attributes:
        items: List of payment items included in the transaction
        payer: Information about the payer (first_name, last_name, phone, address)
        shipments: Shipping information including receiver_address
    """
    
    _resource_name = "payment_additional_info"
    
    def __init__(self, client):
        """
        Initialize PaymentAdditionalInfo resource.
        
        Args:
            client: MercadoPago client instance
        """
        super().__init__(client)
    
    def create(
        self,
        payment_id: int,
        items: Optional[List[Dict[str, Any]]] = None,
        payer: Optional[Dict[str, Any]] = None,
        shipments: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Add additional information to a payment.
        
        Args:
            payment_id: The ID of the payment to add information to
            items: List of payment items with details like:
                - id: Item identifier
                - title: Item title
                - description: Item description
                - picture_url: Item image URL
                - category_id: Item category
                - quantity: Quantity purchased
                - unit_price: Unit price
            payer: Payer information object with:
                - first_name: Payer's first name
                - last_name: Payer's last name
                - phone: Phone contact information (area_code, number)
                - address: Address information (zip_code, street_name, street_number)
            shipments: Shipping information object with:
                - receiver_address: Delivery address details
            **kwargs: Additional optional parameters
        
        Returns:
            Dict containing the API response with additional info status
        
        Raises:
            MPException: If the API request fails
        """
        data = {}
        
        if items is not None:
            data["items"] = items
        
        if payer is not None:
            data["payer"] = payer
        
        if shipments is not None:
            data["shipments"] = shipments
        
        data.update(kwargs)
        
        return self._client.put(
            f"/v1/payments/{payment_id}",
            data=data
        )
    
    def update(
        self,
        payment_id: int,
        items: Optional[List[Dict[str, Any]]] = None,
        payer: Optional[Dict[str, Any]] = None,
        shipments: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update additional information for a payment.
        
        Args:
            payment_id: The ID of the payment to update
            items: Updated list of payment items
            payer: Updated payer information
            shipments: Updated shipping information
            **kwargs: Additional optional parameters
        
        Returns:
            Dict containing the API response with updated additional info
        
        Raises:
            MPException: If the API request fails
        """
        return self.create(
            payment_id=payment_id,
            items=items,
            payer=payer,
            shipments=shipments,
            **kwargs
        )
    
    def validate_items(self, items: List[Dict[str, Any]]) -> bool:
        """
        Validate the structure of payment items.
        
        Args:
            items: List of payment items to validate
        
        Returns:
            True if items are valid, False otherwise
        """
        if not isinstance(items, list):
            return False
        
        required_fields = ["id", "title", "quantity", "unit_price"]
        
        for item in items:
            if not isinstance(item, dict):
                return False
            
            for field in required_fields:
                if field not in item:
                    return False
        
        return True
    
    def validate_payer(self, payer: Dict[str, Any]) -> bool:
        """
        Validate the structure of payer information.
        
        Args:
            payer: Payer information to validate
        
        Returns:
            True if payer info is valid, False otherwise
        """
        if not isinstance(payer, dict):
            return False
        
        # At least one of these should be present
        basic_fields = ["first_name", "last_name", "phone", "address"]
        
        return any(field in payer for field in basic_fields)
    
    def validate_shipments(self, shipments: Dict[str, Any]) -> bool:
        """
        Validate the structure of shipment information.
        
        Args:
            shipments: Shipment information to validate
        
        Returns:
            True if shipment info is valid, False otherwise
        """
        if not isinstance(shipments, dict):
            return False
        
        return "receiver_address" in shipments