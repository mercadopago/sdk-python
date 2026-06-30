"""
Update Pagination - remove has_more field

This module handles the modification of pagination structure by removing
the has_more property and keeping only total, limit, and offset fields.

Affected endpoints:
- GET /v1/payments/search
"""

from typing import Any, Dict, Optional


class PaginationUpdate:
    """
    Handles pagination response updates by removing has_more field
    and standardizing the pagination structure.
    """

    @staticmethod
    def update_pagination_response(response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update pagination response to remove has_more field.

        Args:
            response: The original API response containing pagination data

        Returns:
            Updated response with standardized pagination structure
        """
        if not response:
            return response

        paging = response.get('paging', {})
        
        # Create updated paging structure with only required fields
        updated_paging = {
            'total': paging.get('total', 0),
            'limit': paging.get('limit', 0),
            'offset': paging.get('offset', 0)
        }
        
        # Remove has_more if it exists
        if 'has_more' in paging:
            paging.pop('has_more', None)
        
        # Update the response with the new paging structure
        response['paging'] = updated_paging
        
        return response

    @staticmethod
    def validate_pagination_params(
        total: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> Dict[str, int]:
        """
        Validate and return pagination parameters.

        Args:
            total: Total number of items
            limit: Maximum number of items per page
            offset: Number of items to skip

        Returns:
            Dictionary with validated pagination parameters
        """
        return {
            'total': max(0, total if total is not None else 0),
            'limit': max(0, limit if limit is not None else 0),
            'offset': max(0, offset if offset is not None else 0)
        }

    @staticmethod
    def create_pagination_object(
        total: int,
        limit: int,
        offset: int
    ) -> Dict[str, int]:
        """
        Create a standardized pagination object.

        Args:
            total: Total number of items available
            limit: Maximum number of items returned per page
            offset: Starting position in the result set

        Returns:
            Dictionary containing pagination information
        """
        return {
            'total': int(total),
            'limit': int(limit),
            'offset': int(offset)
        }

    @staticmethod
    def calculate_has_next_page(total: int, limit: int, offset: int) -> bool:
        """
        Calculate if there are more pages available.
        
        Note: This replaces the has_more field with a calculated property.

        Args:
            total: Total number of items
            limit: Items per page
            offset: Current offset

        Returns:
            Boolean indicating if more pages exist
        """
        if limit <= 0:
            return False
        return (offset + limit) < total

    @staticmethod
    def calculate_remaining_items(total: int, limit: int, offset: int) -> int:
        """
        Calculate the number of remaining items after current page.

        Args:
            total: Total number of items
            limit: Items per page
            offset: Current offset

        Returns:
            Number of remaining items
        """
        remaining = total - (offset + limit)
        return max(0, remaining)


class PaymentSearchPagination:
    """
    Specific implementation for GET /v1/payments/search endpoint pagination.
    """

    def __init__(self):
        self.updater = PaginationUpdate()

    def process_search_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process payment search response and update pagination.

        Args:
            response: Raw API response from payments search

        Returns:
            Processed response with updated pagination
        """
        # Update pagination structure
        updated_response = self.updater.update_pagination_response(response)
        
        # Ensure results key exists
        if 'results' not in updated_response:
            updated_response['results'] = []
        
        return updated_response

    def get_pagination_info(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract pagination information from response.

        Args:
            response: API response

        Returns:
            Dictionary with pagination details and calculated fields
        """
        paging = response.get('paging', {})
        total = paging.get('total', 0)
        limit = paging.get('limit', 0)
        offset = paging.get('offset', 0)

        return {
            'total': total,
            'limit': limit,
            'offset': offset,
            'has_next_page': self.updater.calculate_has_next_page(total, limit, offset),
            'remaining_items': self.updater.calculate_remaining_items(total, limit, offset),
            'current_page': (offset // limit) + 1 if limit > 0 else 1,
            'total_pages': (total + limit - 1) // limit if limit > 0 else 1
        }

    def build_next_page_params(
        self,
        current_offset: int,
        limit: int,
        total: int
    ) -> Optional[Dict[str, int]]:
        """
        Build parameters for the next page request.

        Args:
            current_offset: Current offset value
            current_limit: Current limit value
            total: Total items available

        Returns:
            Dictionary with next page parameters or None if no next page
        """
        if not self.updater.calculate_has_next_page(total, limit, current_offset):
            return None

        return {
            'offset': current_offset + limit,
            'limit': limit
        }


def remove_has_more_field(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Utility function to remove has_more field from any pagination structure.

    Args:
        data: Dictionary potentially containing pagination with has_more

    Returns:
        Dictionary with has_more removed
    """
    if isinstance(data, dict):
        if 'paging' in data and isinstance(data['paging'], dict):
            data['paging'].pop('has_more', None)
            
            # Ensure only required fields are present
            allowed_fields = {'total', 'limit', 'offset'}
            data['paging'] = {
                k: v for k, v in data['paging'].items()
                if k in allowed_fields
            }
    
    return data


def standardize_pagination(paging_data: Dict[str, Any]) -> Dict[str, int]:
    """
    Standardize pagination data to the new format.

    Args:
        paging_data: Raw pagination data

    Returns:
        Standardized pagination dictionary
    """
    return {
        'total': int(paging_data.get('total', 0)),
        'limit': int(paging_data.get('limit', 0)),
        'offset': int(paging_data.get('offset', 0))
    }