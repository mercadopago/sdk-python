"""
Phone resource model for MercadoPago SDK.

This module defines the Phone schema with area code and number fields.
"""


class Phone:
    """
    Phone model representing a phone number with area code.
    
    Attributes:
        area_code (str): The area code of the phone number.
        number (str): The phone number without area code.
    """
    
    def __init__(self, area_code=None, number=None):
        """
        Initialize a Phone instance.
        
        Args:
            area_code (str, optional): The area code of the phone number.
            number (str, optional): The phone number without area code.
        """
        self.area_code = area_code
        self.number = number
    
    def to_dict(self):
        """
        Convert the Phone instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the phone object.
        """
        return {
            "area_code": self.area_code,
            "number": self.number
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Phone instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing phone data.
            
        Returns:
            Phone: A new Phone instance.
        """
        if data is None:
            return None
        
        return cls(
            area_code=data.get("area_code"),
            number=data.get("number")
        )
    
    def __repr__(self):
        """
        Return a string representation of the Phone instance.
        
        Returns:
            str: String representation of the phone object.
        """
        return f"Phone(area_code='{self.area_code}', number='{self.number}')"
    
    def __str__(self):
        """
        Return a human-readable string of the phone number.
        
        Returns:
            str: Formatted phone number string.
        """
        if self.area_code and self.number:
            return f"({self.area_code}) {self.number}"
        elif self.number:
            return self.number
        return ""