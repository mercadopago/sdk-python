"""MPResponse — backward-compatible dict wrapper with typed error support.

Wraps the raw ``{"status": ..., "response": ...}`` dict returned by every
:class:`~mercadopago.core.mp_base.MPBase` helper.  Existing code that
reads ``result["status"]`` or ``result["response"]`` continues to work
unchanged; new code may call :meth:`raise_for_status` to get a typed
exception instead of checking ``result["status"]`` manually.
"""
from .exceptions import build_error


class MPResponse(dict):
    """Dictionary subclass for MercadoPago API responses.

    All :class:`~mercadopago.core.mp_base.MPBase` methods return an
    instance of this class.  It behaves identically to a plain ``dict``
    so existing code remains unaffected.

    Example:
        Existing usage (unchanged)::

            result = sdk.payment().get(123)
            print(result["status"])   # 200
            print(result["response"]["status"])  # "approved"

        New typed usage::

            result = sdk.payment().get(123)
            result.raise_for_status()   # raises MPNotFoundError if 404

    Attributes:
        status_code: HTTP status code (alias for ``self["status"]``).
        is_success: True when the status code is 2xx.
    """

    def __init__(self, raw, request_id=None):
        """Wraps a raw response dict.

        Args:
            raw: Dict with ``"status"`` (int) and ``"response"`` keys.
            request_id: Value of the ``x-request-id`` response header,
                used for support diagnostics.
        """
        super().__init__(raw)
        self._request_id = request_id

    # ── Convenience properties ────────────────────────────────────────────────

    @property
    def status_code(self):
        """HTTP status code integer."""
        return self.get("status", 0)

    @property
    def is_success(self):
        """True for 2xx status codes."""
        return 200 <= self.status_code < 300

    @property
    def error_message(self):
        """Human-readable error message from the API body, or empty string."""
        body = self.get("response") or {}
        if isinstance(body, dict):
            return body.get("message", "")
        return ""

    @property
    def error_causes(self):
        """List of cause dicts from the API body, or empty list."""
        body = self.get("response") or {}
        if isinstance(body, dict):
            return body.get("cause", [])
        return []

    @property
    def request_id(self):
        """``x-request-id`` header value for support diagnosis, or None."""
        return self._request_id

    # ── Error raising ─────────────────────────────────────────────────────────

    def raise_for_status(self):
        """Raises a typed :class:`~mercadopago.errors.exceptions.MercadoPagoError`
        if the response status code indicates an error.

        Raises:
            MercadoPagoError (or subtype): When status >= 300.
        """
        if not self.is_success:
            body = self.get("response") or {}
            err = build_error(self.status_code, body)
            err.request_id = self._request_id
            raise err
