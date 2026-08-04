"""Typed exception hierarchy for MercadoPago API errors.

All exceptions inherit from :class:`MercadoPagoError`, preserving
backward-compatible ``catch`` patterns while enabling specific handling
per HTTP status code.
"""


class MercadoPagoError(Exception):
    """Base exception for all MercadoPago API errors.

    Raised when the API returns a non-2xx status code.  Callers may catch
    this base class to handle any API error, or catch a subtype to react
    specifically to 401, 404, 429, etc.

    Attributes:
        status_code: HTTP status code (e.g. 400, 401, 500).
        message: Human-readable error summary from the API.
        error: Machine-readable error code (e.g. ``"unauthorized"``).
        causes: List of detailed cause dicts returned by the API.
        request_id: ``x-request-id`` header for support diagnosis.
    """

    def __init__(self, status_code, response_body):
        self.status_code = status_code
        self.response = response_body or {}
        self.message = self.response.get("message", "")
        self.error = self.response.get("error", "")
        self.causes = self.response.get("cause", [])
        self.request_id = None  # set by MPResponse if x-request-id header is available
        super().__init__(f"[{status_code}] {self.message or self.error}")


class MPBadRequestError(MercadoPagoError):
    """HTTP 400 Bad Request — validation or syntax error."""


class MPAuthenticationError(MercadoPagoError):
    """HTTP 401 Unauthorized — missing or invalid credentials."""


class MPPaymentError(MercadoPagoError):
    """HTTP 402 Payment Required — transaction processing error (AP/Orders)."""


class MPForbiddenError(MercadoPagoError):
    """HTTP 403 Forbidden."""


class MPNotFoundError(MercadoPagoError):
    """HTTP 404 Not Found."""


class MPIdempotencyError(MercadoPagoError):
    """HTTP 409 Conflict — idempotency-key conflict or state-machine conflict."""


class MPValidationError(MercadoPagoError):
    """HTTP 422 Unprocessable Entity — business-rule violation."""


class MPResourceLockedError(MercadoPagoError):
    """HTTP 423 Locked — idempotency key temporarily locked (retryable)."""


class MPDependencyError(MercadoPagoError):
    """HTTP 424 Failed Dependency — internal dependency failure (retryable)."""


class MPRateLimitError(MercadoPagoError):
    """HTTP 429 Too Many Requests.

    Attributes:
        retry_after: Seconds to wait before retrying, from the
            ``Retry-After`` header, or ``None`` if absent.
    """

    def __init__(self, status_code, response_body, retry_after=None):
        super().__init__(status_code, response_body)
        self.retry_after = retry_after


class MPServerError(MercadoPagoError):
    """HTTP 5xx Server Error."""


class MPConnectionError(MercadoPagoError):
    """Transport-level or network error (timeout, DNS failure, SSL error).

    *status_code* is set to ``0`` to indicate no HTTP response was received.
    """

    def __init__(self, cause):
        super().__init__(0, {"message": str(cause), "error": "connection_error"})
        self.__cause__ = cause


_STATUS_MAP = {
    400: MPBadRequestError,
    401: MPAuthenticationError,
    402: MPPaymentError,
    403: MPForbiddenError,
    404: MPNotFoundError,
    409: MPIdempotencyError,
    422: MPValidationError,
    423: MPResourceLockedError,
    424: MPDependencyError,
    429: MPRateLimitError,
}


def build_error(status_code, response_body, retry_after=None):
    """Factory: maps an HTTP status code to the most specific exception subtype.

    Args:
        status_code: HTTP status code from the API response.
        response_body: Parsed JSON response body dict.
        retry_after: Seconds from the ``Retry-After`` header (only for 429).

    Returns:
        MercadoPagoError: The appropriate subtype instance.
    """
    cls = _STATUS_MAP.get(status_code)
    if cls is MPRateLimitError:
        return MPRateLimitError(status_code, response_body, retry_after)
    if cls is not None:
        return cls(status_code, response_body)
    if status_code >= 500:
        return MPServerError(status_code, response_body)
    return MercadoPagoError(status_code, response_body)
