# mercadopago/resources/update_pagination___remove_has_more_field.py

"""
Update Pagination - Remove has_more field

This module updates the pagination structure to remove the has_more property.
Pagination now only includes: total (integer), limit (integer), offset (integer).

Affected endpoints:
- GET /v1/payments/search
"""


class PaginationSchema:
    """
    Updated pagination schema without has_more field.
    
    Properties:
        total (int): Total number of results available
        limit (int): Maximum number of results returned per request
        offset (int): Number of results to skip from the beginning
    """
    
    def __init__(self, total=None, limit=None, offset=None):
        """
        Initialize pagination object.
        
        Args:
            total (int, optional): Total number of results
            limit (int, optional): Maximum results per page
            offset (int, optional): Results offset
        """
        self.total = total
        self.limit = limit
        self.offset = offset
    
    def to_dict(self):
        """
        Convert pagination object to dictionary.
        
        Returns:
            dict: Dictionary with pagination fields (excluding has_more)
        """
        result = {}
        
        if self.total is not None:
            result['total'] = int(self.total)
        
        if self.limit is not None:
            result['limit'] = int(self.limit)
        
        if self.offset is not None:
            result['offset'] = int(self.offset)
        
        return result
    
    @classmethod
    def from_dict(cls, data):
        """
        Create pagination object from dictionary.
        
        Args:
            data (dict): Dictionary containing pagination data
            
        Returns:
            PaginationSchema: Pagination object instance
        """
        if not data:
            return cls()
        
        return cls(
            total=data.get('total'),
            limit=data.get('limit'),
            offset=data.get('offset')
        )
    
    def has_next_page(self):
        """
        Check if there are more results available.
        
        Returns:
            bool: True if there are more results, False otherwise
        """
        if self.total is None or self.offset is None or self.limit is None:
            return False
        
        return (self.offset + self.limit) < self.total
    
    def has_previous_page(self):
        """
        Check if there are previous results available.
        
        Returns:
            bool: True if there are previous results, False otherwise
        """
        if self.offset is None:
            return False
        
        return self.offset > 0
    
    def get_next_offset(self):
        """
        Calculate the offset for the next page.
        
        Returns:
            int: Next offset value, or None if no next page
        """
        if not self.has_next_page():
            return None
        
        return self.offset + self.limit
    
    def get_previous_offset(self):
        """
        Calculate the offset for the previous page.
        
        Returns:
            int: Previous offset value, or None if no previous page
        """
        if not self.has_previous_page():
            return None
        
        return max(0, self.offset - self.limit)
    
    def __repr__(self):
        """String representation of pagination object."""
        return f"PaginationSchema(total={self.total}, limit={self.limit}, offset={self.offset})"
    
    def __eq__(self, other):
        """Check equality between pagination objects."""
        if not isinstance(other, PaginationSchema):
            return False
        
        return (self.total == other.total and 
                self.limit == other.limit and 
                self.offset == other.offset)


def parse_pagination_from_response(response_data):
    """
    Parse pagination data from API response.
    
    Args:
        response_data (dict): API response data
        
    Returns:
        PaginationSchema: Parsed pagination object
    """
    if not response_data or 'paging' not in response_data:
        return PaginationSchema()
    
    paging_data = response_data.get('paging', {})
    
    # Extract only the allowed fields (total, limit, offset)
    # Ignore has_more if present in the response
    return PaginationSchema(
        total=paging_data.get('total'),
        limit=paging_data.get('limit'),
        offset=paging_data.get('offset')
    )


def build_pagination_params(limit=None, offset=None):
    """
    Build pagination parameters for API requests.
    
    Args:
        limit (int, optional): Maximum number of results per page
        offset (int, optional): Number of results to skip
        
    Returns:
        dict: Dictionary with pagination query parameters
    """
    params = {}
    
    if limit is not None:
        params['limit'] = int(limit)
    
    if offset is not None:
        params['offset'] = int(offset)
    
    return params


# Migration helper function
def migrate_pagination_response(legacy_response):
    """
    Migrate legacy pagination responses that may contain has_more field.
    
    Args:
        legacy_response (dict): Legacy API response with pagination
        
    Returns:
        dict: Updated response without has_more field
    """
    if not legacy_response or 'paging' not in legacy_response:
        return legacy_response
    
    paging = legacy_response['paging'].copy()
    
    # Remove has_more if present
    if 'has_more' in paging:
        del paging['has_more']
    
    # Ensure only allowed fields are present
    allowed_fields = {'total', 'limit', 'offset'}
    paging = {k: v for k, v in paging.items() if k in allowed_fields}
    
    legacy_response['paging'] = paging
    return legacy_response