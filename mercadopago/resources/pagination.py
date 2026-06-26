```python
"""
Pagination resource for MercadoPago SDK.

This module defines the pagination structure used across API responses.
"""


class Pagination:
    """
    Represents pagination information for API responses.
    
    Attributes:
        total (int): Total number of items available.
        limit (int): Maximum number of items returned per page.
        offset (int): Number of items skipped from the beginning.
    """
    
    def __init__(self, total=None, limit=None, offset=None):
        """
        Initialize a Pagination instance.
        
        Args:
            total (int, optional): Total number of items available.
            limit (int, optional): Maximum number of items returned per page.
            offset (int, optional): Number of items skipped from the beginning.
        """
        self.total = total
        self.limit = limit
        self.offset = offset
    
    def to_dict(self):
        """
        Convert the Pagination instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the pagination.
        """
        return {
            'total': self.total,
            'limit': self.limit,
            'offset': self.offset
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Pagination instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing pagination data.
            
        Returns:
            Pagination: New Pagination instance.
        """
        if not data:
            return cls()
        
        return cls(
            total=data.get('total'),
            limit=data.get('limit'),
            offset=data.get('offset')
        )
    
    def __repr__(self):
        """String representation of the Pagination instance."""
        return f"Pagination(total={self.total}, limit={self.limit}, offset={self.offset})"

```