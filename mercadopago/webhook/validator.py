"""MercadoPago webhook signature validator.

Verifies the authenticity of incoming webhook notifications by recomputing
the HMAC-SHA256 signature locally and comparing it against the value carried
in the ``x-signature`` header.

The validator is stateless, performs no outbound HTTP calls, and does not
depend on any SDK configuration object; the integrator passes the secret
signature explicitly on every call.
"""
import hmac
import hashlib
import re
import time
from enum import Enum


class SignatureFailureReason(Enum):
    """Reasons why :class:`WebhookSignatureValidator` may reject a notification.

    Integrators are encouraged to log this value alongside the
    ``x-request-id`` for correlation against the MercadoPago notifications
    dashboard.
    """

    MISSING_SIGNATURE_HEADER = "MissingSignatureHeader"
    """The ``x-signature`` header was missing, empty, or whitespace."""

    MALFORMED_SIGNATURE_HEADER = "MalformedSignatureHeader"
    """The header did not match the expected ``ts=...,vN=...`` format."""

    MISSING_TIMESTAMP = "MissingTimestamp"
    """The header parsed correctly but no ``ts=`` component was present."""

    MISSING_HASH = "MissingHash"
    """No hash was found for any of the requested ``supported_versions``."""

    SIGNATURE_MISMATCH = "SignatureMismatch"
    """The computed HMAC did not match the value in the header."""

    TIMESTAMP_OUT_OF_TOLERANCE = "TimestampOutOfTolerance"
    """The header timestamp fell outside the configured ``tolerance`` window."""


class InvalidWebhookSignatureError(Exception):
    """Raised by :func:`WebhookSignatureValidator.validate` on signature failure.

    Carries enough context to support structured logging without exposing
    internal details in the HTTP response body.

    Attributes:
        reason: Specific :class:`SignatureFailureReason` that triggered the error.
        request_id: ``x-request-id`` header value, when available.
        timestamp: ``ts`` value extracted from the signature header, when parsing
            reached that point.
    """

    def __init__(self, reason, request_id=None, timestamp=None):
        """Initialises the error.

        Args:
            reason: Specific failure mode.
            request_id: ``x-request-id`` value associated with the request.
            timestamp: ``ts`` extracted from the header, if available.
        """
        super().__init__("Invalid webhook signature: {0}".format(reason.value))
        self.reason = reason
        self.request_id = request_id
        self.timestamp = timestamp


_DEFAULT_SUPPORTED_VERSIONS = ("v1",)
_VERSION_KEY_REGEX = re.compile(r"^v\d+$")


class WebhookSignatureValidator:
    """Stateless utility that validates the signature of a MercadoPago webhook.

    On failure :func:`validate` raises :class:`InvalidWebhookSignatureError`;
    on success it returns ``None``. The comparison is performed in constant
    time via :func:`hmac.compare_digest` to mitigate timing attacks.

    QR Code notifications are **not signed** by MercadoPago — do not call this
    validator for those events; they will always fail signature verification.
    """

    @staticmethod
    def validate(
        x_signature,
        x_request_id,
        data_id,
        secret,
        tolerance_seconds=None,
        supported_versions=None,
        now=None,
    ):
        """Validates the signature of a MercadoPago webhook notification.

        Args:
            x_signature: Raw value of the ``x-signature`` request header.
                Expected format: ``ts=<ms>,v1=<hex>``.
            x_request_id: Value of the ``x-request-id`` request header. May be
                ``None``; in that case the ``request-id:`` pair is omitted from
                the manifest before computing the HMAC.
            data_id: Value of the ``data.id`` query parameter. May be ``None``;
                in that case the ``id:`` pair is omitted. When present, the
                value is lowercased before being included in the manifest.
            secret: Secret signature configured for the application in Tus
                Integraciones.
            tolerance_seconds: Optional maximum allowed drift in seconds
                between the timestamp in the header and the current clock.
                When ``None``, no timestamp check is performed.
            supported_versions: Optional ordered iterable of signature versions
                the validator will accept. Defaults to ``("v1",)``. The first
                version found in the header is used.
            now: Optional callable returning the current time in milliseconds
                since the Unix epoch. Defaults to ``time.time() * 1000``.
                Intended for tests.

        Raises:
            InvalidWebhookSignatureError: When the signature is missing,
                malformed, or does not match the expected HMAC.
            ValueError: When ``secret`` is ``None``.
        """
        if secret is None:
            raise ValueError("secret must not be None")

        x_signature = _normalize(x_signature)
        x_request_id = _normalize(x_request_id)
        data_id = _normalize(data_id)
        versions = tuple(supported_versions) if supported_versions else _DEFAULT_SUPPORTED_VERSIONS
        if now is None:
            now = lambda: int(time.time() * 1000)

        if x_signature is None:
            raise InvalidWebhookSignatureError(
                SignatureFailureReason.MISSING_SIGNATURE_HEADER, x_request_id
            )

        ts, hashes = _parse_signature_header(x_signature)

        if ts is None and not hashes:
            raise InvalidWebhookSignatureError(
                SignatureFailureReason.MALFORMED_SIGNATURE_HEADER, x_request_id
            )

        if ts is None:
            raise InvalidWebhookSignatureError(
                SignatureFailureReason.MISSING_TIMESTAMP, x_request_id
            )

        if not ts.isdigit():
            raise InvalidWebhookSignatureError(
                SignatureFailureReason.MALFORMED_SIGNATURE_HEADER, x_request_id, ts
            )

        received_hash = None
        for version in versions:
            if version in hashes:
                received_hash = hashes[version]
                break

        if received_hash is None:
            raise InvalidWebhookSignatureError(
                SignatureFailureReason.MISSING_HASH, x_request_id, ts
            )

        manifest = _build_manifest(data_id, x_request_id, ts)
        computed = hmac.new(
            secret.encode("utf-8"), manifest.encode("utf-8"), hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(computed, received_hash):
            raise InvalidWebhookSignatureError(
                SignatureFailureReason.SIGNATURE_MISMATCH, x_request_id, ts
            )

        if tolerance_seconds is not None:
            drift_ms = abs(now() - int(ts))
            if drift_ms > tolerance_seconds * 1000:
                raise InvalidWebhookSignatureError(
                    SignatureFailureReason.TIMESTAMP_OUT_OF_TOLERANCE, x_request_id, ts
                )


def _normalize(value):
    """Returns the trimmed string or ``None`` for missing/whitespace values."""
    if value is None:
        return None
    text = str(value).strip()
    return text if text else None


def _parse_signature_header(header):
    """Parses the ``x-signature`` header into ``(ts, {vN: hash})``."""
    hashes = {}
    ts = None
    for part in header.split(","):
        if "=" not in part:
            continue
        key, value = part.split("=", 1)
        key = key.strip().lower()
        value = value.strip()
        if not key or not value:
            continue
        if key == "ts":
            ts = value
        elif _VERSION_KEY_REGEX.match(key):
            hashes[key] = value
    return ts, hashes


def _build_manifest(data_id, request_id, ts):
    """Builds the HMAC manifest, omitting empty pairs per the documented rule."""
    parts = []
    if data_id:
        parts.append("id:{0}".format(data_id.lower()))
    if request_id:
        parts.append("request-id:{0}".format(request_id))
    parts.append("ts:{0}".format(ts))
    return ";".join(parts) + ";"
