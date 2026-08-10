"""Errors package for the MercadoPago Python SDK."""
from .exceptions import (
    MercadoPagoError,
    MPAuthenticationError,
    MPBadRequestError,
    MPConnectionError,
    MPDependencyError,
    MPForbiddenError,
    MPIdempotencyError,
    MPNotFoundError,
    MPPaymentError,
    MPRateLimitError,
    MPResourceLockedError,
    MPServerError,
    MPValidationError,
    build_error,
)
from .response import MPResponse


__all__ = [
    "MercadoPagoError",
    "MPBadRequestError",
    "MPAuthenticationError",
    "MPPaymentError",
    "MPForbiddenError",
    "MPNotFoundError",
    "MPIdempotencyError",
    "MPValidationError",
    "MPResourceLockedError",
    "MPDependencyError",
    "MPRateLimitError",
    "MPServerError",
    "MPConnectionError",
    "build_error",
    "MPResponse",
]
