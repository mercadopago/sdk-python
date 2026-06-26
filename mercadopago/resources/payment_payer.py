"""Payment payer resource for MercadoPago SDK."""

from typing import Optional
from mercadopago.resources.base import Resource


class PaymentPayer(Resource):
    """
    Payment payer model.
    
    Represents the payer information for a payment transaction.
    
    Attributes:
        email (str): Required. Email address of the payer.
        id (str): Optional. Unique identifier of the payer.
        identification (dict): Optional. Identification information with 'type' and 'number'.
        type (str): Optional. Type of payer. Enum: 'customer', 'registered', 'guest'.
    """
    
    PAYER_TYPES = ['customer', 'registered', 'guest']
    
    def __init__(self, email: str, id: Optional[str] = None, 
                 identification: Optional[dict] = None, 
                 type: Optional[str] = None):
        """
        Initialize a PaymentPayer instance.
        
        Args:
            email (str): Email address of the payer (required).
            id (str, optional): Unique identifier of the payer.
            identification (dict, optional): Identification information containing:
                - type (str): Type of identification document.
                - number (str): Identification document number.
            type (str, optional): Type of payer ('customer', 'registered', or 'guest').
        
        Raises:
            ValueError: If email is not provided or if type is not in allowed values.
        """
        if not email:
            raise ValueError("Email is required for PaymentPayer")
        
        if type and type not in self.PAYER_TYPES:
            raise ValueError(f"Type must be one of {self.PAYER_TYPES}")
        
        if identification:
            if not isinstance(identification, dict):
                raise ValueError("Identification must be a dictionary")
            if 'type' not in identification or 'number' not in identification:
                raise ValueError("Identification must contain 'type' and 'number' keys")
        
        self.email = email
        self.id = id
        self.identification = identification
        self.type = type
    
    def to_dict(self) -> dict:
        """
        Convert the PaymentPayer instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the payer, excluding None values.
        """
        data = {
            'email': self.email
        }
        
        if self.id is not None:
            data['id'] = self.id
        
        if self.identification is not None:
            data['identification'] = self.identification
        
        if self.type is not None:
            data['type'] = self.type
        
        return data
    
    @classmethod
    def from_dict(cls, data: dict) -> 'PaymentPayer':
        """
        Create a PaymentPayer instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing payer information.
        
        Returns:
            PaymentPayer: New PaymentPayer instance.
        
        Raises:
            ValueError: If required fields are missing.
        """
        if 'email' not in data:
            raise ValueError("Email is required in data dictionary")
        
        return cls(
            email=data['email'],
            id=data.get('id'),
            identification=data.get('identification'),
            type=data.get('type')
        )
    
    def __repr__(self) -> str:
        """String representation of PaymentPayer."""
        return (f"PaymentPayer(email='{self.email}', id='{self.id}', "
                f"type='{self.type}')")
    
    def __eq__(self, other) -> bool:
        """Check equality based on email and id."""
        if not isinstance(other, PaymentPayer):
            return False
        return self.email == other.email and self.id == other.id