# mercadopago/resources/update_pagination___remove_has_more_field.py

"""
Update Pagination - remove has_more field

This module updates pagination response structure by removing the has_more property.
Only total, limit, and offset properties are kept.

Affected endpoints: GET /v1/payments/search
"""

from mercadopago.core import MPRequestOptions
from mercadopago.resources.base import MPResourceBase


class UpdatedPaginationResource(MPResourceBase):
    """
    Resource handler for endpoints with updated pagination structure.
    Removes has_more field and keeps only total, limit, and offset.
    """

    def __init__(self, client):
        """
        Initialize the resource.
        
        Args:
            client: MercadoPago SDK client instance
        """
        super().__init__(client)

    def search_payments(self, filters=None, request_options=None):
        """
        Search for payments with updated pagination structure.
        
        Args:
            filters (dict, optional): Search filters including pagination parameters
            request_options (MPRequestOptions, optional): Request options
            
        Returns:
            dict: Response containing:
                - results (list): List of payment objects
                - paging (dict): Pagination info with:
                    - total (int): Total number of results
                    - limit (int): Number of results per page
                    - offset (int): Starting position
                    
        Example:
            >>> resource = UpdatedPaginationResource(client)
            >>> response = resource.search_payments({
            ...     'limit': 10,
            ...     'offset': 0,
            ...     'status': 'approved'
            ... })
            >>> print(response['paging'])
            {'total': 100, 'limit': 10, 'offset': 0}
        """
        if filters is None:
            filters = {}
            
        if request_options is None:
            request_options = MPRequestOptions()

        response = self._client.get(
            "/v1/payments/search",
            params=filters,
            request_options=request_options
        )
        
        # Process pagination to remove has_more if present
        if response and 'paging' in response:
            response['paging'] = self._normalize_pagination(response['paging'])
            
        return response

    def _normalize_pagination(self, paging):
        """
        Normalize pagination object by keeping only required fields.
        
        Args:
            paging (dict): Original pagination object
            
        Returns:
            dict: Normalized pagination with only total, limit, offset
        """
        normalized = {}
        
        # Keep only the allowed fields
        if 'total' in paging:
            normalized['total'] = int(paging['total'])
        else:
            normalized['total'] = 0
            
        if 'limit' in paging:
            normalized['limit'] = int(paging['limit'])
        else:
            normalized['limit'] = 10
            
        if 'offset' in paging:
            normalized['offset'] = int(paging['offset'])
        else:
            normalized['offset'] = 0
            
        return normalized

    def get_next_page(self, current_response):
        """
        Helper method to get parameters for the next page.
        
        Args:
            current_response (dict): Current response with paging information
            
        Returns:
            dict: Filters for next page or None if no more pages
            
        Example:
            >>> response = resource.search_payments({'limit': 10, 'offset': 0})
            >>> next_params = resource.get_next_page(response)
            >>> if next_params:
            ...     next_response = resource.search_payments(next_params)
        """
        if not current_response or 'paging' not in current_response:
            return None
            
        paging = current_response['paging']
        total = paging.get('total', 0)
        limit = paging.get('limit', 10)
        offset = paging.get('offset', 0)
        
        next_offset = offset + limit
        
        # Check if there are more results
        if next_offset >= total:
            return None
            
        return {
            'limit': limit,
            'offset': next_offset
        }

    def get_previous_page(self, current_response):
        """
        Helper method to get parameters for the previous page.
        
        Args:
            current_response (dict): Current response with paging information
            
        Returns:
            dict: Filters for previous page or None if on first page
        """
        if not current_response or 'paging' not in current_response:
            return None
            
        paging = current_response['paging']
        limit = paging.get('limit', 10)
        offset = paging.get('offset', 0)
        
        if offset <= 0:
            return None
            
        previous_offset = max(0, offset - limit)
        
        return {
            'limit': limit,
            'offset': previous_offset
        }

    def has_next_page(self, response):
        """
        Check if there are more pages available.
        
        Args:
            response (dict): Response with paging information
            
        Returns:
            bool: True if more pages exist, False otherwise
        """
        if not response or 'paging' not in response:
            return False
            
        paging = response['paging']
        total = paging.get('total', 0)
        limit = paging.get('limit', 10)
        offset = paging.get('offset', 0)
        
        return (offset + limit) < total

    def has_previous_page(self, response):
        """
        Check if there is a previous page available.
        
        Args:
            response (dict): Response with paging information
            
        Returns:
            bool: True if previous page exists, False otherwise
        """
        if not response or 'paging' not in response:
            return False
            
        paging = response['paging']
        offset = paging.get('offset', 0)
        
        return offset > 0

    def get_total_pages(self, response):
        """
        Calculate total number of pages.
        
        Args:
            response (dict): Response with paging information
            
        Returns:
            int: Total number of pages
        """
        if not response or 'paging' not in response:
            return 0
            
        paging = response['paging']
        total = paging.get('total', 0)
        limit = paging.get('limit', 10)
        
        if limit <= 0:
            return 0
            
        return (total + limit - 1) // limit  # Ceiling division

    def get_current_page(self, response):
        """
        Calculate current page number (1-based).
        
        Args:
            response (dict): Response with paging information
            
        Returns:
            int: Current page number
        """
        if not response or 'paging' not in response:
            return 1
            
        paging = response['paging']
        limit = paging.get('limit', 10)
        offset = paging.get('offset', 0)
        
        if limit <= 0:
            return 1
            
        return (offset // limit) + 1


def migrate_pagination_response(old_response):
    """
    Utility function to migrate old pagination format to new format.
    Removes has_more field from existing responses.
    
    Args:
        old_response (dict): Response with old pagination format
        
    Returns:
        dict: Response with updated pagination format
    """
    if not old_response or 'paging' not in old_response:
        return old_response
        
    new_response = old_response.copy()
    paging = new_response['paging'].copy()
    
    # Remove has_more if it exists
    if 'has_more' in paging:
        del paging['has_more']
    
    # Ensure only required fields exist
    new_paging = {
        'total': int(paging.get('total', 0)),
        'limit': int(paging.get('limit', 10)),
        'offset': int(paging.get('offset', 0))
    }
    
    new_response['paging'] = new_paging
    
    return new_response