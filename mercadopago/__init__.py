"""MercadoPago Python SDK.

Provides a high-level client for the MercadoPago REST API.  Import the
:class:`SDK` class and initialise it with your access token to get
started::

    import mercadopago
    sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")
    payment = sdk.payment().create({...})
"""
from mercadopago.sdk import SDK
from mercadopago.errors.exceptions import (
    MercadoPagoError,
    MPBadRequestError,
    MPAuthenticationError,
    MPPaymentError,
    MPForbiddenError,
    MPNotFoundError,
    MPIdempotencyError,
    MPValidationError,
    MPResourceLockedError,
    MPDependencyError,
    MPRateLimitError,
    MPServerError,
    MPConnectionError,
)
from mercadopago.errors.constants import MPOrderErrors, MPPaymentErrors
from mercadopago.errors.response import MPResponse
from mercadopago.resources.status import (
    PaymentStatus,
    OrderStatus,
    PreapprovalStatus,
    MerchantOrderStatus,
    RefundStatus,
)


__all__ = (
    'SDK',
    'MercadoPagoError',
    'MPBadRequestError',
    'MPAuthenticationError',
    'MPPaymentError',
    'MPForbiddenError',
    'MPNotFoundError',
    'MPIdempotencyError',
    'MPValidationError',
    'MPResourceLockedError',
    'MPDependencyError',
    'MPRateLimitError',
    'MPServerError',
    'MPConnectionError',
    'MPOrderErrors',
    'MPPaymentErrors',
    'MPResponse',
    'PaymentStatus',
    'OrderStatus',
    'PreapprovalStatus',
    'MerchantOrderStatus',
    'RefundStatus',
)
