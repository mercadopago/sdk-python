"""
Update Pagination - remove has_more field

This module handles the modification of pagination response structure
by removing the has_more property and keeping only total, limit, and offset.

Affected endpoints: GET /v1/payments/search
"""

from typing import Dict, Any, Optional


class PaginationResponse:
    """
    Pagination response structure without has_more field.
    
    Attributes:
        total (int): Total number of items available
        limit (int): Maximum number of items per page
        offset (int): Number of items to skip
    """
    
    def __init__(self, total: int, limit: int, offset: int):
        """
        Initialize pagination response.
        
        Args:
            total: Total number of items available
            limit: Maximum number of items per page
            offset: Number of items to skip
        """
        self.total = total
        self.limit = limit
        self.offset = offset
    
    def to_dict(self) -> Dict[str, int]:
        """
        Convert pagination to dictionary format.
        
        Returns:
            Dictionary with pagination data (total, limit, offset only)
        """
        return {
            "total": self.total,
            "limit": self.limit,
            "offset": self.offset
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PaginationResponse':
        """
        Create PaginationResponse from dictionary.
        
        Args:
            data: Dictionary containing pagination data
            
        Returns:
            PaginationResponse instance
        """
        # Remove has_more if present in legacy data
        total = data.get("total", 0)
        limit = data.get("limit", 0)
        offset = data.get("offset", 0)
        
        return cls(total=total, limit=limit, offset=offset)


def normalize_pagination(pagination_data: Dict[str, Any]) -> Dict[str, int]:
    """
    Normalize pagination data by removing has_more field.
    
    This function ensures backward compatibility by accepting pagination
    data that may contain has_more field and returning only the allowed fields.
    
    Args:
        pagination_data: Raw pagination data that may contain has_more
        
    Returns:
        Normalized pagination dictionary with only total, limit, offset
    """
    normalized = {
        "total": pagination_data.get("total", 0),
        "limit": pagination_data.get("limit", 0),
        "offset": pagination_data.get("offset", 0)
    }
    
    return normalized


def update_search_response(response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update payment search response to use new pagination format.
    
    Specifically handles GET /v1/payments/search endpoint responses
    by removing has_more from pagination (paging) object.
    
    Args:
        response: Raw API response containing paging information
        
    Returns:
        Updated response with normalized pagination
    """
    if "paging" in response:
        response["paging"] = normalize_pagination(response["paging"])
    
    return response


class PaginationUpdater:
    """
    Helper class to update pagination structures across responses.
    """
    
    @staticmethod
    def remove_has_more(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Remove has_more field from pagination data.
        
        Args:
            data: Dictionary that may contain pagination with has_more
            
        Returns:
            Data with has_more removed from pagination
        """
        if isinstance(data, dict):
            # Handle paging/pagination keys
            for key in ["paging", "pagination"]:
                if key in data and isinstance(data[key], dict):
                    data[key] = normalize_pagination(data[key])
            
            # Recursively handle nested structures
            for key, value in data.items():
                if isinstance(value, dict):
                    data[key] = PaginationUpdater.remove_has_more(value)
                elif isinstance(value, list):
                    data[key] = [
                        PaginationUpdater.remove_has_more(item) 
                        if isinstance(item, dict) else item 
                        for item in value
                    ]
        
        return data
    
    @staticmethod
    def validate_pagination(pagination: Dict[str, Any]) -> bool:
        """
        Validate that pagination only contains allowed fields.
        
        Args:
            pagination: Pagination dictionary to validate
            
        Returns:
            True if pagination is valid (no has_more field)
        """
        allowed_fields = {"total", "limit", "offset"}
        pagination_fields = set(pagination.keys())
        
        # Check for has_more field
        if "has_more" in pagination_fields:
            return False
        
        # Check that only allowed fields are present
        return pagination_fields.issubset(allowed_fields)


# Migration helper for existing code
def migrate_pagination_response(old_response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Migrate old pagination responses to new format.
    
    This helper function assists in migrating existing responses that
    may contain has_more field to the new format.
    
    Args:
        old_response: Response with old pagination format
        
    Returns:
        Response with new pagination format
    """
    return PaginationUpdater.remove_has_more(old_response)


__all__ = [
    'PaginationResponse',
    'normalize_pagination',
    'update_search_response',
    'PaginationUpdater',
    'migrate_pagination_response'
]