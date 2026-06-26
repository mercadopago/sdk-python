"""Pagination resource for MercadoPago SDK."""


class Pagination:
    """Represents pagination information for list responses."""

    def __init__(self, total: int = 0, limit: int = 0, offset: int = 0):
        """
        Initialize Pagination.

        Args:
            total: Total number of items available
            limit: Maximum number of items per page
            offset: Number of items to skip
        """
        self.total = total
        self.limit = limit
        self.offset = offset

    def to_dict(self):
        """
        Convert pagination to dictionary.

        Returns:
            dict: Dictionary representation of pagination
        """
        return {
            "total": self.total,
            "limit": self.limit,
            "offset": self.offset,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create Pagination instance from dictionary.

        Args:
            data: Dictionary containing pagination data

        Returns:
            Pagination: New Pagination instance
        """
        return cls(
            total=data.get("total", 0),
            limit=data.get("limit", 0),
            offset=data.get("offset", 0),
        )

    def __repr__(self):
        """String representation of Pagination."""
        return f"Pagination(total={self.total}, limit={self.limit}, offset={self.offset})"