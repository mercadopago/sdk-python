"""HTTP transport layer for the MercadoPago SDK.

Exposes :class:`HttpClient`, the default ``requests``-based implementation
used to execute REST calls against the MercadoPago API.
"""
from mercadopago.http.http_client import HttpClient


__all__ = (
    'HttpClient',
)
