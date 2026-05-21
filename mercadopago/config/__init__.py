"""Configuration components for the MercadoPago Python SDK.

Exposes :class:`Config` (SDK-level constants) and :class:`RequestOptions`
(per-request settings such as access token, timeout, and custom headers).
"""
from mercadopago.config.config import Config
from mercadopago.config.request_options import RequestOptions


__all__ = (
    'Config',
    'RequestOptions',
)
