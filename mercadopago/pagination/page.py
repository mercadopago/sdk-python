"""Pagination helpers for MercadoPago search results."""


class Paging:
    """Pagination metadata extracted from a search response."""

    def __init__(self, total=0, limit=0, offset=0):
        self.total = total
        self.limit = limit
        self.offset = offset

    @classmethod
    def from_dict(cls, d):
        if not d:
            return cls()
        return cls(
            total=d.get("total", 0),
            limit=d.get("limit", 0),
            offset=d.get("offset", 0),
        )
