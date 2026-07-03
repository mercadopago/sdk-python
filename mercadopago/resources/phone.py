"""Phone resource for MercadoPago SDK."""

from typing import Optional
from ..config import RequestOptions
from ..http import HttpClient
from ..serialization import Serializer
from .base import ResourceBase


class Phone(ResourceBase):
    """Phone resource for managing phone information.
    
    This resource handles phone data including area code and number.
    """

    def __init__(
        self,
        http_client: HttpClient,
        serializer: Optional[Serializer] = None,
        request_options: Optional[RequestOptions] = None
    ):
        """Initialize Phone resource.
        
        Args:
            http_client: HTTP client for making requests
            serializer: Optional serializer for data transformation
            request_options: Optional default request options
        """
        super().__init__(
            http_client=http_client,
            serializer=serializer,
            request_options=request_options
        )

    @property
    def _base_path(self) -> str:
        """Get the base path for phone endpoints.
        
        Returns:
            Base path string
        """
        return "/v1/phones"


class PhoneSchema:
    """Schema for Phone data structure.
    
    Attributes:
        area_code: Optional area code string
        number: Optional phone number string
    """

    def __init__(
        self,
        area_code: Optional[str] = None,
        number: Optional[str] = None
    ):
        """Initialize PhoneSchema.
        
        Args:
            area_code: Optional area code
            number: Optional phone number
        """
        self.area_code = area_code
        self.number = number

    def to_dict(self) -> dict:
        """Convert schema to dictionary.
        
        Returns:
            Dictionary representation of phone data
        """
        data = {}
        if self.area_code is not None:
            data["area_code"] = self.area_code
        if self.number is not None:
            data["number"] = self.number
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "PhoneSchema":
        """Create PhoneSchema from dictionary.
        
        Args:
            data: Dictionary containing phone data
            
        Returns:
            PhoneSchema instance
        """
        return cls(
            area_code=data.get("area_code"),
            number=data.get("number")
        )

    def __repr__(self) -> str:
        """String representation of PhoneSchema.
        
        Returns:
            String representation
        """
        return f"PhoneSchema(area_code={self.area_code!r}, number={self.number!r})"

    def __eq__(self, other) -> bool:
        """Compare two PhoneSchema instances.
        
        Args:
            other: Another PhoneSchema instance
            
        Returns:
            True if equal, False otherwise
        """
        if not isinstance(other, PhoneSchema):
            return False
        return (
            self.area_code == other.area_code and
            self.number == other.number
        )