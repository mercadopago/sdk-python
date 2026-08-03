"""Auto-paging iterator for MercadoPago search resources.

Creates a lazy generator that fetches pages of results on demand so
callers can iterate over every matching item without managing offsets.

Example:
    ::

        for payment in sdk.payment().search_auto_paging_iter({"status": "approved"}):
            process(payment)
"""
from .page import Paging


def search_auto_paging_iter(search_fn, filters=None, request_options=None, limit=100):
    """Lazy generator that auto-fetches all pages of a search result.

    Yields individual items (dicts) from successive paginated API calls.
    The original ``search()`` method is called once per page; iteration
    stops when the results list is empty or the offset reaches the total.

    Args:
        search_fn: Callable matching ``search(filters, request_options) -> MPResponse``.
        filters: Initial search filters dict. ``limit`` and ``offset`` are
            managed automatically — callers should NOT include them here.
        request_options: Per-request overrides forwarded to each page call.
        limit: Items per page. Defaults to 100.

    Yields:
        dict: Individual result items from each page.
    """
    filters = dict(filters or {})
    filters.setdefault("limit", limit)
    filters["offset"] = filters.get("offset", 0)
    offset = filters["offset"]

    while True:
        filters["offset"] = offset
        result = search_fn(filters, request_options)

        body = result.get("response") or {}
        results = body.get("results", [])
        paging = Paging.from_dict(body.get("paging"))

        if not results:
            return

        for item in results:
            yield item

        offset += len(results)
        if offset >= paging.total:
            return
