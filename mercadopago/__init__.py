"""MercadoPago Python SDK.

Provides a high-level client for the MercadoPago REST API.  Import the
:class:`SDK` class and initialise it with your access token to get
started::

    import mercadopago
    sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")
    payment = sdk.payment().create({...})
"""
from mercadopago.sdk import SDK


__all__ = (
    'SDK',
)
