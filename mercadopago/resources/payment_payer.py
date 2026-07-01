"""Payment payer resource implementation."""

from mercadopago.resources.base import ResourceBase


class PaymentPayer(ResourceBase):
    """PaymentPayer resource model.
    
    Represents the payer information for a payment transaction.
    
    Attributes:
        email (str): Required. Payer's email address.
        id (str): Optional. Payer's ID.
        identification (dict): Optional. Identification details with 'type' and 'number' keys.
        type (str): Optional. Payer type. Valid values: 'customer', 'registered', 'guest'.
    """
    
    _schema = {
        "email": {
            "type": str,
            "required": True
        },
        "id": {
            "type": str,
            "required": False
        },
        "identification": {
            "type": dict,
            "required": False
        },
        "type": {
            "type": str,
            "required": False,
            "enum": ["customer", "registered", "guest"]
        }
    }
    
    def __init__(self, email, id=None, identification=None, type=None):
        """Initialize PaymentPayer instance.
        
        Args:
            email (str): Payer's email address (required).
            id (str, optional): Payer's ID.
            identification (dict, optional): Identification object with 'type' and 'number'.
            type (str, optional): Payer type ('customer', 'registered', or 'guest').
        
        Raises:
            ValueError: If email is not provided or type is not valid.
        """
        if not email:
            raise ValueError("email is required")
        
        if type is not None and type not in ["customer", "registered", "guest"]:
            raise ValueError(f"type must be one of: customer, registered, guest. Got: {type}")
        
        if identification is not None and not isinstance(identification, dict):
            raise ValueError("identification must be a dictionary")
        
        self.email = email
        self.id = id
        self.identification = identification
        self.type = type
        
        super().__init__()
    
    def to_dict(self):
        """Convert PaymentPayer instance to dictionary.
        
        Returns:
            dict: Dictionary representation of the payment payer.
        """
        data = {"email": self.email}
        
        if self.id is not None:
            data["id"] = self.id
        
        if self.identification is not None:
            data["identification"] = self.identification
        
        if self.type is not None:
            data["type"] = self.type
        
        return data
    
    @classmethod
    def from_dict(cls, data):
        """Create PaymentPayer instance from dictionary.
        
        Args:
            data (dict): Dictionary containing payment payer data.
        
        Returns:
            PaymentPayer: New instance created from dictionary data.
        
        Raises:
            ValueError: If required fields are missing.
        """
        if not data:
            raise ValueError("data dictionary is required")
        
        if "email" not in data:
            raise ValueError("email is required in data")
        
        return cls(
            email=data.get("email"),
            id=data.get("id"),
            identification=data.get("identification"),
            type=data.get("type")
        )
    
    def validate(self):
        """Validate the PaymentPayer instance.
        
        Returns:
            bool: True if valid.
        
        Raises:
            ValueError: If validation fails.
        """
        if not self.email:
            raise ValueError("email is required")
        
        if not isinstance(self.email, str):
            raise ValueError("email must be a string")
        
        if self.id is not None and not isinstance(self.id, str):
            raise ValueError("id must be a string")
        
        if self.identification is not None:
            if not isinstance(self.identification, dict):
                raise ValueError("identification must be a dictionary")
            
            if "type" in self.identification and not isinstance(self.identification["type"], str):
                raise ValueError("identification.type must be a string")
            
            if "number" in self.identification and not isinstance(self.identification["number"], str):
                raise ValueError("identification.number must be a string")
        
        if self.type is not None:
            if not isinstance(self.type, str):
                raise ValueError("type must be a string")
            
            if self.type not in ["customer", "registered", "guest"]:
                raise ValueError(f"type must be one of: customer, registered, guest. Got: {self.type}")
        
        return True
    
    def __repr__(self):
        """Return string representation of PaymentPayer.
        
        Returns:
            str: String representation.
        """
        return f"PaymentPayer(email='{self.email}', id='{self.id}', type='{self.type}')"
    
    def __eq__(self, other):
        """Check equality with another PaymentPayer instance.
        
        Args:
            other: Another object to compare with.
        
        Returns:
            bool: True if equal, False otherwise.
        """
        if not isinstance(other, PaymentPayer):
            return False
        
        return (
            self.email == other.email and
            self.id == other.id and
            self.identification == other.identification and
            self.type == other.type
        )