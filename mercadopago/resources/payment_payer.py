# mercadopago/resources/payment_payer.py

```python
"""
PaymentPayer schema for MercadoPago SDK.

This module defines the PaymentPayer model used in payment operations.
"""

from typing import Optional
from mercadopago.resources.base import BaseModel


class PaymentPayerIdentification(BaseModel):
    """Payment payer identification information."""
    
    type: Optional[str] = None
    number: Optional[str] = None


class PaymentPayer(BaseModel):
    """
    PaymentPayer model for MercadoPago payments.
    
    Attributes:
        email (str): Payer's email address (required).
        id (str, optional): Payer's unique identifier.
        identification (PaymentPayerIdentification, optional): Payer's identification document.
        type (str, optional): Type of payer. Valid values: 'customer', 'registered', 'guest'.
    """
    
    # Required fields
    email: str
    
    # Optional fields
    id: Optional[str] = None
    identification: Optional[PaymentPayerIdentification] = None
    type: Optional[str] = None
    
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
            email (str): Payer's email address (required).
            id (str, optional): Payer's unique identifier.
            identification (dict, optional): Payer's identification with 'type' and 'number' keys.
            type (str, optional): Type of payer ('customer', 'registered', or 'guest').
            **kwargs: Additional fields.
        
        Raises:
            ValueError: If type is not one of the valid values.
        """
        if type is not None and type not in ['customer', 'registered', 'guest']:
            raise ValueError(
                f"Invalid payer type: {type}. Must be one of: 'customer', 'registered', 'guest'"
            )
        
        super().__init__(
            email=email,
            id=id,
            identification=PaymentPayerIdentification(**identification) if identification else None,
            type=type,
            **kwargs
        )
    
    def to_dict(self) -> dict:
        """
        Convert PaymentPayer instance to dictionary.
        
        Returns:
            dict: Dictionary representation of the payer.
        """
        result = {
            'email': self.email
        }
        
        if self.id is not None:
            result['id'] = self.id
        
        if self.identification is not None:
            result['identification'] = self.identification.to_dict()
        
        if self.type is not None:
            result['type'] = self.type
        
        return result

```