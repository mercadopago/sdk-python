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
        # Orders API returns total/limit/offset as strings; other APIs as ints
        def _int(v, default=0):
            try:
                return int(v)
            except (TypeError, ValueError):
                return default
        return cls(
            total=_int(d.get("total"), 0),
            limit=_int(d.get("limit"), 0),
            offset=_int(d.get("offset"), 0),
        )
