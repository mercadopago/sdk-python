"""
Update Pagination - remove has_more field

This module updates pagination response models by removing the has_more field.
Keeping only: total (integer), limit (integer), offset (integer).

Affected endpoints: GET /v1/payments/search
"""

from mercadopago.core import MPBase


class PaginationResponse(MPBase):
    """
    Pagination response model without has_more field.
    
    Attributes:
        total (int): Total number of items available
        limit (int): Maximum number of items returned per request
        offset (int): Number of items skipped from the beginning
    """
    
    def __init__(self, data=None):
        """
        Initialize pagination response.
        
        Args:
            data (dict, optional): Dictionary containing pagination data
        """
        super().__init__()
        if data is None:
            data = {}
        
        self.total = data.get('total', 0)
        self.limit = data.get('limit', 0)
        self.offset = data.get('offset', 0)
    
    def to_dict(self):
        """
        Convert pagination response to dictionary.
        
        Returns:
            dict: Dictionary representation of pagination response
        """
        return {
            'total': self.total,
            'limit': self.limit,
            'offset': self.offset
        }
    
    def __repr__(self):
        """String representation of pagination response."""
        return f"PaginationResponse(total={self.total}, limit={self.limit}, offset={self.offset})"


class PaymentSearchResponse(MPBase):
    """
    Payment search response with updated pagination model.
    
    Attributes:
        paging (PaginationResponse): Pagination information
        results (list): List of payment results
    """
    
    def __init__(self, data=None):
        """
        Initialize payment search response.
        
        Args:
            data (dict, optional): Dictionary containing search response data
        """
        super().__init__()
        if data is None:
            data = {}
        
        paging_data = data.get('paging', {})
        self.paging = PaginationResponse(paging_data)
        self.results = data.get('results', [])
    
    def to_dict(self):
        """
        Convert payment search response to dictionary.
        
        Returns:
            dict: Dictionary representation of search response
        """
        return {
            'paging': self.paging.to_dict(),
            'results': self.results
        }
    
    def has_next_page(self):
        """
        Check if there are more results available.
        
        Returns:
            bool: True if more results are available, False otherwise
        """
        return (self.paging.offset + self.paging.limit) < self.paging.total
    
    def has_previous_page(self):
        """
        Check if there is a previous page.
        
        Returns:
            bool: True if previous page exists, False otherwise
        """
        return self.paging.offset > 0
    
    def get_next_offset(self):
        """
        Get the offset for the next page.
        
        Returns:
            int or None: Next offset value or None if no next page
        """
        if self.has_next_page():
            return self.paging.offset + self.paging.limit
        return None
    
    def get_previous_offset(self):
        """
        Get the offset for the previous page.
        
        Returns:
            int: Previous offset value (minimum 0)
        """
        previous_offset = self.paging.offset - self.paging.limit
        return max(0, previous_offset)
    
    def __repr__(self):
        """String representation of payment search response."""
        return (f"PaymentSearchResponse(paging={self.paging}, "
                f"results_count={len(self.results)})")


def parse_pagination_response(response_data):
    """
    Parse API response and extract pagination information.
    
    Args:
        response_data (dict): Raw API response data
    
    Returns:
        PaginationResponse: Parsed pagination response
    """
    if not isinstance(response_data, dict):
        return PaginationResponse()
    
    paging_data = response_data.get('paging', {})
    return PaginationResponse(paging_data)


def parse_payment_search_response(response_data):
    """
    Parse payment search API response.
    
    Args:
        response_data (dict): Raw API response data
    
    Returns:
        PaymentSearchResponse: Parsed payment search response
    """
    if not isinstance(response_data, dict):
        return PaymentSearchResponse()
    
    return PaymentSearchResponse(response_data)