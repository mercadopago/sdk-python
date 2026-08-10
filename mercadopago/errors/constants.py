"""Error string constants for MercadoPago API error codes.

Use these constants instead of hard-coding ``error`` string literals so
that code is refactoring-safe and benefits from IDE auto-complete.

Example::

    from mercadopago.errors.constants import MPOrderErrors
    except MPIdempotencyError as e:
        if e.error == MPOrderErrors.CANNOT_REFUND:
            handle_cannot_refund()
"""


class MPOrderErrors:
    """Machine-readable ``error`` strings returned for Order/v1 conflicts (HTTP 409)."""
    CANNOT_REFUND = "cannot_refund_order"
    CANNOT_CANCEL = "cannot_cancel_order"
    CANNOT_CAPTURE = "cannot_capture_order"
    ALREADY_REFUNDED = "order_already_refunded"
    ALREADY_CANCELED = "order_already_canceled"
    RESOURCE_LOCKED = "resource_locked"


class MPPaymentErrors:
    """Machine-readable ``error`` strings returned for payment errors (HTTP 402)."""
    FAILED = "failed"
