# mercadopago/resources/payment_payer.py

from typing import Optional
from mercadopago.core.resource import Resource


class PaymentPayer(Resource):
    """
    PaymentPayer model for handling payer information in payments.
    
    Attributes:
        email (str): Payer's email address (required)
        id (str): Payer's ID (optional)
        identification (dict): Payer's identification document (optional)
            - type (str): Type of identification
            - number (str): Identification number
        type (str): Type of payer - customer, registered, or guest (optional)
    """
    
    def __init__(
        self,
        email: str,
        id: Optional[str] = None,
        identification: Optional[dict] = None,
        type: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize PaymentPayer instance.
        
        Args:
            email: Payer's email address (required)
            id: Payer's ID (optional)
            identification: Dictionary with 'type' and 'number' keys (optional)
            type: Type of payer - 'customer', 'registered', or 'guest' (optional)
            **kwargs: Additional attributes
        """
        super().__init__(**kwargs)
        self.email = email
        self.id = id
        self.identification = identification
        self.type = type
        
        # Validate type if provided
        if self.type and self.type not in ['customer', 'registered', 'guest']:
            raise ValueError(
                f"Invalid payer type: {self.type}. "
                "Must be one of: 'customer', 'registered', 'guest'"
            )
        
        # Validate identification structure if provided
        if self.identification:
            if not isinstance(self.identification, dict):
                raise ValueError("identification must be a dictionary")
            if 'type' not in self.identification or 'number' not in self.identification:
                raise ValueError(
                    "identification must contain 'type' and 'number' keys"
                )
    
    def to_dict(self) -> dict:
        """
        Convert PaymentPayer instance to dictionary.
        
        Returns:
            dict: Dictionary representation of the payer
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
        Create PaymentPayer instance from dictionary.
        
        Args:
            data: Dictionary containing payer data
            
        Returns:
            PaymentPayer: New instance created from dictionary
        """
        return cls(
            email=data.get('email'),
            id=data.get('id'),
            identification=data.get('identification'),
            type=data.get('type')
        )