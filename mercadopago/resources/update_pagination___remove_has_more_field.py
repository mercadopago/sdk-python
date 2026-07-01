# mercadopago/resources/update_pagination___remove_has_more_field.py

"""
Update Pagination - remove has_more field

Change type: modify
Title: Update Pagination - remove has_more field
Detail: Remove the has_more property. Keep only: total (integer), limit (integer), offset (integer).
Affected endpoints: GET /v1/payments/search
"""

from typing import Optional, List, Dict, Any
from mercadopago.http import HttpClient
from mercadopago.config import Config


class PaginationResponse:
    """
    Pagination response model without has_more field.
    Contains only: total, limit, and offset.
    """
    
    def __init__(self, total: int, limit: int, offset: int):
        """
        Initialize pagination response.
        
        Args:
            total: Total number of results
            limit: Maximum number of results per page
            offset: Starting position for results
        """
        self.total = total
        self.limit = limit
        self.offset = offset
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PaginationResponse':
        """
        Create PaginationResponse from dictionary.
        
        Args:
            data: Dictionary containing pagination data
            
        Returns:
            PaginationResponse instance
        """
        return cls(
            total=data.get('total', 0),
            limit=data.get('limit', 0),
            offset=data.get('offset', 0)
        )
    
    def to_dict(self) -> Dict[str, int]:
        """
        Convert pagination response to dictionary.
        
        Returns:
            Dictionary with pagination fields
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
    
    def __init__(self, paging: PaginationResponse, results: List[Dict[str, Any]]):
        """
        Initialize payment search response.
        
        Args:
            paging: Pagination information
            results: List of payment results
        """
        self.paging = paging
        self.results = results
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PaymentSearchResponse':
        """
        Create PaymentSearchResponse from dictionary.
        
        Args:
            data: Dictionary containing response data
            
        Returns:
            PaymentSearchResponse instance
        """
        paging_data = data.get('paging', {})
        paging = PaginationResponse.from_dict(paging_data)
        results = data.get('results', [])
        
        return cls(paging=paging, results=results)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert response to dictionary.
        
        Returns:
            Dictionary with paging and results
        """
        return {
            'paging': self.paging.to_dict(),
            'results': self.results
        }


class PaymentSearch:
    """
    Payment search resource with updated pagination (without has_more field).
    """
    
    def __init__(self, client: HttpClient, config: Optional[Config] = None):
        """
        Initialize PaymentSearch resource.
        
        Args:
            client: HTTP client for making requests
            config: Optional configuration
        """
        self.client = client
        self.config = config or Config()
    
    def search(
        self,
        filters: Optional[Dict[str, Any]] = None,
        limit: int = 30,
        offset: int = 0
    ) -> PaymentSearchResponse:
        """
        Search payments with updated pagination structure.
        
        Args:
            filters: Search filters (e.g., status, date_from, date_to)
            limit: Maximum number of results per page (default: 30)
            offset: Starting position for results (default: 0)
            
        Returns:
            PaymentSearchResponse with pagination (total, limit, offset) and results
            
        Example:
            >>> search = PaymentSearch(client)
            >>> response = search.search(
            ...     filters={'status': 'approved'},
            ...     limit=50,
            ...     offset=0
            ... )
            >>> print(f"Total: {response.paging.total}")
            >>> print(f"Limit: {response.paging.limit}")
            >>> print(f"Offset: {response.paging.offset}")
        """
        params = filters.copy() if filters else {}
        params['limit'] = limit
        params['offset'] = offset
        
        response = self.client.get('/v1/payments/search', params=params)
        
        # Process response to ensure has_more is removed
        response_data = response if isinstance(response, dict) else response.json()
        
        # Remove has_more if it exists in the paging section
        if 'paging' in response_data and 'has_more' in response_data['paging']:
            del response_data['paging']['has_more']
        
        return PaymentSearchResponse.from_dict(response_data)
    
    def search_all(
        self,
        filters: Optional[Dict[str, Any]] = None,
        limit: int = 30
    ) -> List[Dict[str, Any]]:
        """
        Search all payments by iterating through pages using offset.
        
        Args:
            filters: Search filters
            limit: Maximum number of results per page
            
        Returns:
            List of all payment results
            
        Example:
            >>> search = PaymentSearch(client)
            >>> all_payments = search.search_all(filters={'status': 'approved'})
        """
        all_results = []
        offset = 0
        
        while True:
            response = self.search(filters=filters, limit=limit, offset=offset)
            all_results.extend(response.results)
            
            # Check if there are more results based on total count
            if offset + limit >= response.paging.total:
                break
            
            offset += limit
        
        return all_results


def migrate_pagination_response(old_response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Migrate old pagination response (with has_more) to new format (without has_more).
    
    Args:
        old_response: Response dictionary with old pagination format
        
    Returns:
        Response dictionary with updated pagination format
        
    Example:
        >>> old = {
        ...     'paging': {'total': 100, 'limit': 30, 'offset': 0, 'has_more': True},
        ...     'results': [...]
        ... }
        >>> new = migrate_pagination_response(old)
        >>> assert 'has_more' not in new['paging']
    """
    new_response = old_response.copy()
    
    if 'paging' in new_response and isinstance(new_response['paging'], dict):
        new_paging = new_response['paging'].copy()
        # Remove has_more field if it exists
        new_paging.pop('has_more', None)
        new_response['paging'] = new_paging
    
    return new_response


# Utility function to check if there are more results
def has_more_results(paging: PaginationResponse) -> bool:
    """
    Check if there are more results to fetch based on pagination info.
    
    Args:
        paging: Pagination response object
        
    Returns:
        True if there are more results, False otherwise
        
    Example:
        >>> paging = PaginationResponse(total=100, limit=30, offset=0)
        >>> has_more_results(paging)  # True
        >>> paging = PaginationResponse(total=100, limit=30, offset=90)
        >>> has_more_results(paging)  # False
    """
    return (paging.offset + paging.limit) < paging.total