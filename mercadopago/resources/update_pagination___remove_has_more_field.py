# mercadopago/resources/update_pagination___remove_has_more_field.py

"""
Update Pagination - remove has_more field

Change type: modify
Title: Update Pagination - remove has_more field
Detail: Remove the has_more property. Keep only: total (integer), limit (integer), offset (integer).
Affected endpoints: GET /v1/payments/search
"""

from typing import Optional, Dict, Any, List
from mercadopago.http import HttpClient
from mercadopago.config import Config


class PaginationResponse:
    """
    Pagination response object without has_more field.
    Contains only: total, limit, and offset.
    """
    
    def __init__(self, data: Dict[str, Any]):
        """
        Initialize pagination response.
        
        Args:
            data: Dictionary containing pagination data
        """
        self.total: int = data.get('total', 0)
        self.limit: int = data.get('limit', 0)
        self.offset: int = data.get('offset', 0)
    
    def to_dict(self) -> Dict[str, int]:
        """
        Convert pagination object to dictionary.
        
        Returns:
            Dictionary with total, limit, and offset
        """
        return {
            'total': self.total,
            'limit': self.limit,
            'offset': self.offset
        }


class PaymentSearchResponse:
    """
    Payment search response with updated pagination structure.
    """
    
    def __init__(self, data: Dict[str, Any]):
        """
        Initialize payment search response.
        
        Args:
            data: Dictionary containing response data
        """
        self.paging: Optional[PaginationResponse] = None
        if 'paging' in data:
            self.paging = PaginationResponse(data['paging'])
        
        self.results: List[Dict[str, Any]] = data.get('results', [])
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert response object to dictionary.
        
        Returns:
            Dictionary representation of the response
        """
        response = {
            'results': self.results
        }
        
        if self.paging:
            response['paging'] = self.paging.to_dict()
        
        return response


class PaymentSearch:
    """
    Payment search resource with updated pagination (without has_more field).
    """
    
    def __init__(self, client: HttpClient, config: Optional[Config] = None):
        """
        Initialize PaymentSearch resource.
        
        Args:
            client: HTTP client for making requests
            config: Optional configuration object
        """
        self.client = client
        self.config = config or Config()
    
    def search(self, filters: Optional[Dict[str, Any]] = None) -> PaymentSearchResponse:
        """
        Search payments with pagination (updated structure).
        
        Args:
            filters: Optional dictionary with search filters
                - limit: Number of results per page
                - offset: Starting position
                - sort: Sort field and order
                - criteria: Search criteria
                - range: Date range
                - begin_date: Start date
                - end_date: End date
                - etc.
        
        Returns:
            PaymentSearchResponse object with updated pagination structure
        
        Example:
            >>> search = PaymentSearch(client)
            >>> response = search.search({
            ...     'limit': 30,
            ...     'offset': 0,
            ...     'sort': 'date_created',
            ...     'criteria': 'desc'
            ... })
            >>> print(f"Total: {response.paging.total}")
            >>> print(f"Limit: {response.paging.limit}")
            >>> print(f"Offset: {response.paging.offset}")
        """
        params = filters or {}
        
        response = self.client.get('/v1/payments/search', params=params)
        
        return PaymentSearchResponse(response)
    
    def get_all_pages(self, 
                      filters: Optional[Dict[str, Any]] = None,
                      limit: int = 30) -> List[Dict[str, Any]]:
        """
        Retrieve all pages of payment search results.
        
        Args:
            filters: Optional dictionary with search filters
            limit: Number of results per page (default: 30)
        
        Returns:
            List of all payment results across all pages
        
        Example:
            >>> search = PaymentSearch(client)
            >>> all_payments = search.get_all_pages({'status': 'approved'}, limit=50)
            >>> print(f"Total payments retrieved: {len(all_payments)}")
        """
        all_results = []
        offset = 0
        filters = filters or {}
        
        while True:
            filters['limit'] = limit
            filters['offset'] = offset
            
            response = self.search(filters)
            
            if not response.results:
                break
            
            all_results.extend(response.results)
            
            # Check if we've retrieved all results
            if response.paging and offset + limit >= response.paging.total:
                break
            
            offset += limit
        
        return all_results
    
    def iterate_pages(self, 
                      filters: Optional[Dict[str, Any]] = None,
                      limit: int = 30):
        """
        Generator to iterate through payment search pages.
        
        Args:
            filters: Optional dictionary with search filters
            limit: Number of results per page (default: 30)
        
        Yields:
            PaymentSearchResponse for each page
        
        Example:
            >>> search = PaymentSearch(client)
            >>> for page in search.iterate_pages({'status': 'approved'}, limit=50):
            ...     print(f"Page with {len(page.results)} results")
            ...     print(f"Total available: {page.paging.total}")
        """
        offset = 0
        filters = filters or {}
        
        while True:
            filters['limit'] = limit
            filters['offset'] = offset
            
            response = self.search(filters)
            
            if not response.results:
                break
            
            yield response
            
            # Check if we've retrieved all results
            if response.paging and offset + limit >= response.paging.total:
                break
            
            offset += limit


def create_pagination_dict(total: int, limit: int, offset: int) -> Dict[str, int]:
    """
    Helper function to create pagination dictionary (without has_more).
    
    Args:
        total: Total number of results
        limit: Number of results per page
        offset: Starting position
    
    Returns:
        Dictionary with pagination data
    
    Example:
        >>> paging = create_pagination_dict(total=150, limit=30, offset=60)
        >>> print(paging)
        {'total': 150, 'limit': 30, 'offset': 60}
    """
    return {
        'total': total,
        'limit': limit,
        'offset': offset
    }


def calculate_total_pages(total: int, limit: int) -> int:
    """
    Calculate total number of pages based on total results and limit.
    
    Args:
        total: Total number of results
        limit: Number of results per page
    
    Returns:
        Total number of pages
    
    Example:
        >>> pages = calculate_total_pages(total=150, limit=30)
        >>> print(pages)  # Output: 5
    """
    if limit <= 0:
        return 0
    return (total + limit - 1) // limit


def has_next_page(total: int, limit: int, offset: int) -> bool:
    """
    Check if there is a next page available.
    Replacement for the removed has_more field.
    
    Args:
        total: Total number of results
        limit: Number of results per page
        offset: Current offset
    
    Returns:
        True if there is a next page, False otherwise
    
    Example:
        >>> has_next = has_next_page(total=150, limit=30, offset=120)
        >>> print(has_next)  # Output: False (120 + 30 >= 150)
    """
    return offset + limit < total


def get_next_offset(current_offset: int, limit: int, total: int) -> Optional[int]:
    """
    Get the next offset value, or None if no more pages.
    
    Args:
        current_offset: Current offset position
        limit: Number of results per page
        total: Total number of results
    
    Returns:
        Next offset value, or None if no more pages
    
    Example:
        >>> next_off = get_next_offset(current_offset=30, limit=30, total=150)
        >>> print(next_off)  # Output: 60
    """
    next_offset = current_offset + limit
    if next_offset >= total:
        return None
    return next_offset


def get_previous_offset(current_offset: int, limit: int) -> Optional[int]:
    """
    Get the previous offset value, or None if on first page.
    
    Args:
        current_offset: Current offset position
        limit: Number of results per page
    
    Returns:
        Previous offset value, or None if on first page
    
    Example:
        >>> prev_off = get_previous_offset(current_offset=60, limit=30)
        >>> print(prev_off)  # Output: 30
    """
    if current_offset == 0:
        return None
    previous_offset = current_offset - limit
    return max(0, previous_offset)