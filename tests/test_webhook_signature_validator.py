"""
    Module: test_webhook_signature_validator

Unit tests for :class:`mercadopago.webhook.WebhookSignatureValidator`.
These tests are self-contained and do not require any environment variables
or network access.
"""
import hashlib
import hmac
import time
import unittest

from mercadopago.webhook import (
    InvalidWebhookSignatureError,
    SignatureFailureReason,
    WebhookSignatureValidator,
)


SECRET = "your_secret_key_here"
REQUEST_ID = "2066ca19-c6f1-498a-be75-1923005edd06"
DATA_ID_RAW = "ORD01JQ4S4KY8HWQ6NA5PXB65B3D3"
DATA_ID_LOWER = "ord01jq4s4ky8hwq6na5pxb65b3d3"
TS = "1742505638683"
TS_NUM = int(TS)


def compute_hash(data_id, request_id, ts, secret):
    parts = []
    if data_id:
        parts.append(f"id:{data_id}")
    if request_id:
        parts.append(f"request-id:{request_id}")
    parts.append(f"ts:{ts}")
    manifest = ";".join(parts) + ";"
    return hmac.new(secret.encode("utf-8"), manifest.encode("utf-8"), hashlib.sha256).hexdigest()


def build_header(h, ts=TS, version="v1"):
    return f"ts={ts},{version}={h}"


VALID_HASH = compute_hash(DATA_ID_LOWER, REQUEST_ID, TS, SECRET)
VALID_HEADER = build_header(VALID_HASH)


class TestWebhookSignatureValidator(unittest.TestCase):
    """Covers the 12 canonical cases plus supportedVersions and arg validation."""

    # --- case 1 ---
    def test_happy_path_lowercase(self):
        WebhookSignatureValidator.validate(VALID_HEADER, REQUEST_ID, DATA_ID_LOWER, SECRET)

    # --- case 2 ---
    def test_uppercase_dataid_is_preserved(self):
        upper_hash = compute_hash(DATA_ID_RAW, REQUEST_ID, TS, SECRET)
        upper_header = build_header(upper_hash)
        WebhookSignatureValidator.validate(upper_header, REQUEST_ID, DATA_ID_RAW, SECRET)

    # --- case 3 ---
    def test_malformed_header_raises_malformed(self):
        with self.assertRaises(InvalidWebhookSignatureError) as ctx:
            WebhookSignatureValidator.validate("this-is-garbage", REQUEST_ID, DATA_ID_LOWER, SECRET)
        self.assertEqual(ctx.exception.reason, SignatureFailureReason.MALFORMED_SIGNATURE_HEADER)
        self.assertEqual(ctx.exception.request_id, REQUEST_ID)

    # --- case 4 ---
    def test_missing_header_raises_missing_header(self):
        with self.assertRaises(InvalidWebhookSignatureError) as ctx:
            WebhookSignatureValidator.validate(None, REQUEST_ID, DATA_ID_LOWER, SECRET)
        self.assertEqual(ctx.exception.reason, SignatureFailureReason.MISSING_SIGNATURE_HEADER)

    # --- case 5 ---
    def test_missing_ts_raises_missing_timestamp(self):
        header = f"v1={VALID_HASH}"
        with self.assertRaises(InvalidWebhookSignatureError) as ctx:
            WebhookSignatureValidator.validate(header, REQUEST_ID, DATA_ID_LOWER, SECRET)
        self.assertEqual(ctx.exception.reason, SignatureFailureReason.MISSING_TIMESTAMP)

    # --- case 6 ---
    def test_missing_v1_raises_missing_hash(self):
        with self.assertRaises(InvalidWebhookSignatureError) as ctx:
            WebhookSignatureValidator.validate(
                f"ts={TS}", REQUEST_ID, DATA_ID_LOWER, SECRET
            )
        self.assertEqual(ctx.exception.reason, SignatureFailureReason.MISSING_HASH)
        self.assertEqual(ctx.exception.timestamp, TS)

    # --- case 7 ---
    def test_tampered_hash_raises_signature_mismatch(self):
        tampered = VALID_HASH[:-2] + ("ff" if VALID_HASH.endswith("00") else "00")
        with self.assertRaises(InvalidWebhookSignatureError) as ctx:
            WebhookSignatureValidator.validate(
                build_header(tampered), REQUEST_ID, DATA_ID_LOWER, SECRET
            )
        self.assertEqual(ctx.exception.reason, SignatureFailureReason.SIGNATURE_MISMATCH)

    # --- case 8 ---
    def test_timestamp_outside_tolerance_raises(self):
        stale_ts = str(int(time.time() * 1000) - 30 * 60 * 1000)
        h = compute_hash(DATA_ID_LOWER, REQUEST_ID, stale_ts, SECRET)
        with self.assertRaises(InvalidWebhookSignatureError) as ctx:
            WebhookSignatureValidator.validate(
                build_header(h, stale_ts), REQUEST_ID, DATA_ID_LOWER, SECRET,
                tolerance_seconds=300,
            )
        self.assertEqual(ctx.exception.reason, SignatureFailureReason.TIMESTAMP_OUT_OF_TOLERANCE)

    def test_timestamp_within_tolerance_passes(self):
        current_ts = str(int(time.time() * 1000))
        h = compute_hash(DATA_ID_LOWER, REQUEST_ID, current_ts, SECRET)
        WebhookSignatureValidator.validate(
            build_header(h, current_ts), REQUEST_ID, DATA_ID_LOWER, SECRET,
            tolerance_seconds=300,
        )

    # --- case 9 ---
    def test_dataid_absent_excludes_id_pair(self):
        h = compute_hash(None, REQUEST_ID, TS, SECRET)
        WebhookSignatureValidator.validate(build_header(h), REQUEST_ID, None, SECRET)

    # --- case 10 ---
    def test_request_id_absent_excludes_request_id_pair(self):
        h = compute_hash(DATA_ID_LOWER, None, TS, SECRET)
        WebhookSignatureValidator.validate(build_header(h), None, DATA_ID_LOWER, SECRET)

    # --- case 11 ---
    def test_both_absent_yields_ts_only(self):
        h = compute_hash(None, None, TS, SECRET)
        WebhookSignatureValidator.validate(build_header(h), "", "  ", SECRET)

    # --- case 12 ---
    def test_non_payment_topic_uses_same_algorithm(self):
        order_id = "ord01abc123"
        h = compute_hash(order_id, REQUEST_ID, TS, SECRET)
        WebhookSignatureValidator.validate(build_header(h), REQUEST_ID, order_id, SECRET)

    # --- supportedVersions ---
    def test_supports_v1_when_both_present(self):
        header = f"ts={TS},v1={VALID_HASH},v2=aaaa"
        WebhookSignatureValidator.validate(header, REQUEST_ID, DATA_ID_LOWER, SECRET,
                                           supported_versions=["v1"])

    def test_only_v2_in_header_only_v1_supported_raises_missing_hash(self):
        header = f"ts={TS},v2=somehash"
        with self.assertRaises(InvalidWebhookSignatureError) as ctx:
            WebhookSignatureValidator.validate(header, REQUEST_ID, DATA_ID_LOWER, SECRET,
                                               supported_versions=["v1"])
        self.assertEqual(ctx.exception.reason, SignatureFailureReason.MISSING_HASH)

    # --- secret null guard ---
    def test_null_secret_raises_value_error(self):
        with self.assertRaises(ValueError):
            WebhookSignatureValidator.validate(VALID_HEADER, REQUEST_ID, DATA_ID_LOWER, None)


if __name__ == "__main__":
    unittest.main()
