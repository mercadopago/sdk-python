"""Payment Payer resource for MercadoPago SDK."""

from typing import Optional
from mercadopago.resources.base import ResourceBase


class PaymentPayer(ResourceBase):
    """
    Payment Payer resource.
    
    Represents the payer information in a payment transaction.
    """
    
    _resource_name = "payment_payer"
    
    # Required fields
    email: str
    
    # Optional fields
    id: Optional[str] = None
    identification: Optional[dict] = None  # Contains 'type' and 'number'
    type: Optional[str] = None  # Enum: 'customer', 'registered', 'guest'
    
    def __init__(self, client=None):
        """
        Initialize PaymentPayer resource.
        
        Args:
            client: MercadoPago client instance
        """
        super().__init__(client)
    
    def create(self, request_data: dict) -> dict:
        """
        Create a payment payer.
        
        Args:
            request_data: Dictionary containing payer data with required 'email' field
            
        Returns:
            Dictionary with the created payer information
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        self._validate_payer_data(request_data)
        return super().create(request_data)
    
    def update(self, payer_id: str, request_data: dict) -> dict:
        """
        Update a payment payer.
        
        Args:
            payer_id: The payer ID
            request_data: Dictionary containing payer data to update
            
        Returns:
            Dictionary with the updated payer information
        """
        return super().update(payer_id, request_data)
    
    def get(self, payer_id: str) -> dict:
        """
        Get a payment payer by ID.
        
        Args:
            payer_id: The payer ID
            
        Returns:
            Dictionary with the payer information
        """
        return super().get(payer_id)
    
    def _validate_payer_data(self, data: dict) -> None:
        """
        Validate payer data.
        
        Args:
            data: Dictionary containing payer data
            
        Raises:
            ValueError: If validation fails
        """
        # Validate required field
        if not data.get('email'):
            raise ValueError("Field 'email' is required")
        
        if not isinstance(data['email'], str):
            raise ValueError("Field 'email' must be a string")
        
        # Validate optional type field if present
        if 'type' in data:
            valid_types = ['customer', 'registered', 'guest']
            if data['type'] not in valid_types:
                raise ValueError(f"Field 'type' must be one of: {', '.join(valid_types)}")
        
        # Validate optional identification field if present
        if 'identification' in data:
            if not isinstance(data['identification'], dict):
                raise ValueError("Field 'identification' must be an object")
            
            identification = data['identification']
            if 'type' in identification and not isinstance(identification['type'], str):
                raise ValueError("Field 'identification.type' must be a string")
            
            if 'number' in identification and not isinstance(identification['number'], str):
                raise ValueError("Field 'identification.number' must be a string")