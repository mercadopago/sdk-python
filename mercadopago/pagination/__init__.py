"""Pagination utilities for the MercadoPago Python SDK."""
from .iterator import search_auto_paging_iter
from .page import Paging


__all__ = ["search_auto_paging_iter", "Paging"]
