"""Core base class for all MercadoPago API resource modules.

Exposes :class:`MPBase`, the abstract superclass that provides authenticated
HTTP helpers (``_get``, ``_post``, ``_put``, ``_delete``) to every resource.
"""
from mercadopago.core.mp_base import MPBase


__all__ = (
    'MPBase',
)
