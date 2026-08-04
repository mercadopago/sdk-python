"""Status enum constants for MercadoPago resources.

Use these constants instead of hard-coding status string literals to
avoid typos and benefit from IDE auto-complete.

Example::

    from mercadopago import PaymentStatus
    if result["response"]["status"] == PaymentStatus.APPROVED:
        fulfill_order()
"""


class PaymentStatus:
    """Valid values for ``payment.status``."""
    PENDING = "pending"
    APPROVED = "approved"
    AUTHORIZED = "authorized"
    IN_PROCESS = "in_process"
    IN_MEDIATION = "in_mediation"
    REJECTED = "rejected"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"
    CHARGED_BACK = "charged_back"


class OrderStatus:
    """Valid values for ``order.status``."""
    CREATED = "created"
    PROCESSED = "processed"
    ACTION_REQUIRED = "action_required"
    PROCESSING = "processing"
    CANCELED = "canceled"


class PreapprovalStatus:
    """Valid values for ``preapproval.status``."""
    PENDING = "pending"
    AUTHORIZED = "authorized"
    PAUSED = "paused"
    CANCELLED = "cancelled"


class MerchantOrderStatus:
    """Valid values for ``merchant_order.status``."""
    OPENED = "opened"
    CLOSED = "closed"
    EXPIRED = "expired"


class RefundStatus:
    """Valid values for ``refund.status``."""
    APPROVED = "approved"
    IN_PROCESS = "in_process"
    REJECTED = "rejected"
