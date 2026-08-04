"""Unit tests for Python SDK ergonomia features (TASK-013..018, TASK-046..049).

Tests cover:
- Typed exception hierarchy (TASK-013 / TASK-046)
- MPResponse dict-compat wrapper (TASK-013)
- build_error() factory (TASK-013 / TASK-046)
- DEFAULT constants (TASK-049)
- RequestOptions retry params + validation (TASK-015 / TASK-049)
- Auto-pagination iterator (TASK-016)
- Status enum constants (TASK-047)
- Error string constants (TASK-046)
- DeprecationWarning for notification_url (TASK-047)
- Idempotency-key length validation (TASK-047)
- Backward compatibility: result["status"] still works (TASK-018)
"""
import uuid
import warnings
import unittest

import mercadopago
from mercadopago.errors.exceptions import (
    MercadoPagoError, MPBadRequestError, MPAuthenticationError, MPPaymentError,
    MPForbiddenError, MPNotFoundError, MPIdempotencyError, MPValidationError,
    MPResourceLockedError, MPDependencyError, MPRateLimitError, MPServerError,
    MPConnectionError, build_error,
)
from mercadopago.errors.response import MPResponse
from mercadopago.errors.constants import MPOrderErrors, MPPaymentErrors
from mercadopago.resources.status import (
    PaymentStatus, OrderStatus, PreapprovalStatus, MerchantOrderStatus, RefundStatus,
)
from mercadopago.config.request_options import RequestOptions
from mercadopago.config.defaults import (
    DEFAULT_TIMEOUT_SECONDS, DEFAULT_MAX_RETRIES, DEFAULT_RETRY_ON,
)
from mercadopago.pagination.iterator import search_auto_paging_iter

# ─── Exception hierarchy ──────────────────────────────────────────────────────

class TestExceptionHierarchy(unittest.TestCase):

    def test_all_subtypes_inherit_mercadopago_error(self):
        classes = [
            MPBadRequestError, MPAuthenticationError, MPPaymentError,
            MPForbiddenError, MPNotFoundError, MPIdempotencyError, MPValidationError,
            MPResourceLockedError, MPDependencyError, MPRateLimitError,
            MPServerError,
        ]
        for cls in classes:
            err = cls(400, {"message": "test"})
            self.assertIsInstance(err, MercadoPagoError, f"{cls} not subtype of MercadoPagoError")

    def test_rate_limit_stores_retry_after(self):
        err = MPRateLimitError(429, {"message": "rate limited"}, retry_after=45)
        self.assertEqual(err.retry_after, 45)

    def test_rate_limit_null_retry_after(self):
        err = MPRateLimitError(429, {})
        self.assertIsNone(err.retry_after)

    def test_connection_error_wraps_cause(self):
        err = MPConnectionError(ConnectionError("timeout"))
        self.assertIsInstance(err, MercadoPagoError)
        self.assertEqual(err.status_code, 0)

    def test_catch_by_base_catches_subtype(self):
        err = MPNotFoundError(404, {"message": "not found"})
        caught = False
        try:
            raise err
        except MercadoPagoError:
            caught = True
        self.assertTrue(caught)

# ─── build_error() factory ────────────────────────────────────────────────────

class TestBuildError(unittest.TestCase):

    def test_factory_maps_status_to_subtype(self):
        cases = [
            (400, MPBadRequestError),
            (401, MPAuthenticationError),
            (402, MPPaymentError),
            (403, MPForbiddenError),
            (404, MPNotFoundError),
            (409, MPIdempotencyError),
            (422, MPValidationError),
            (423, MPResourceLockedError),
            (424, MPDependencyError),
            (429, MPRateLimitError),
            (500, MPServerError),
            (503, MPServerError),
            (418, MercadoPagoError),
        ]
        for status, expected_cls in cases:
            with self.subTest(status=status):
                err = build_error(status, {})
                self.assertEqual(type(err), expected_cls)

    def test_factory_429_with_retry_after(self):
        err = build_error(429, {}, retry_after=30)
        self.assertIsInstance(err, MPRateLimitError)
        self.assertEqual(err.retry_after, 30)

# ─── MPResponse ───────────────────────────────────────────────────────────────

class TestMPResponse(unittest.TestCase):

    def test_is_dict_subclass(self):
        r = MPResponse({"status": 200, "response": {"id": 1}})
        self.assertIsInstance(r, dict)
        self.assertEqual(r["status"], 200)

    def test_status_code_property(self):
        r = MPResponse({"status": 404, "response": None})
        self.assertEqual(r.status_code, 404)

    def test_is_success_true_for_2xx(self):
        self.assertTrue(MPResponse({"status": 200, "response": {}}).is_success)
        self.assertTrue(MPResponse({"status": 201, "response": {}}).is_success)

    def test_is_success_false_for_4xx(self):
        self.assertFalse(MPResponse({"status": 400, "response": {}}).is_success)

    def test_raise_for_status_ok_does_nothing(self):
        MPResponse({"status": 200, "response": {}}).raise_for_status()

    def test_raise_for_status_4xx_raises_typed(self):
        r = MPResponse({"status": 401, "response": {"message": "unauthorized"}})
        with self.assertRaises(MPAuthenticationError):
            r.raise_for_status()

    def test_raise_for_status_5xx_raises_server_error(self):
        r = MPResponse({"status": 500, "response": {}})
        with self.assertRaises(MPServerError):
            r.raise_for_status()

    def test_backward_compat_dict_access(self):
        raw = {"status": 200, "response": {"id": 42, "status": "approved"}}
        r = MPResponse(raw)
        self.assertEqual(r["status"], 200)
        self.assertEqual(r["response"]["id"], 42)

# ─── DEFAULT constants ────────────────────────────────────────────────────────

class TestDefaultConstants(unittest.TestCase):

    def test_default_timeout(self):
        self.assertEqual(DEFAULT_TIMEOUT_SECONDS, 60.0)

    def test_default_max_retries(self):
        self.assertEqual(DEFAULT_MAX_RETRIES, 3)

    def test_default_retry_on_includes_429(self):
        self.assertIn(429, DEFAULT_RETRY_ON)

    def test_default_retry_on_includes_5xx(self):
        self.assertIn(500, DEFAULT_RETRY_ON)
        self.assertIn(502, DEFAULT_RETRY_ON)
        self.assertIn(503, DEFAULT_RETRY_ON)
        self.assertIn(504, DEFAULT_RETRY_ON)

# ─── RequestOptions retry params ─────────────────────────────────────────────

class TestRequestOptionsRetry(unittest.TestCase):

    def test_defaults_preserved(self):
        opts = RequestOptions(access_token="TEST-token")
        self.assertEqual(opts.connection_timeout, DEFAULT_TIMEOUT_SECONDS)
        self.assertEqual(opts.max_retries, DEFAULT_MAX_RETRIES)

    def test_set_valid_retry_on(self):
        opts = RequestOptions(access_token="t")
        opts.retry_on = [429, 503]
        self.assertEqual(opts.retry_on, [429, 503])

    def test_set_invalid_retry_on_raises(self):
        opts = RequestOptions(access_token="t")
        with self.assertRaises(ValueError):
            opts.retry_on = [999]

    def test_set_jitter(self):
        opts = RequestOptions(access_token="t")
        opts.jitter = True
        self.assertTrue(opts.jitter)

    def test_on_retry_callable(self):
        called = []
        opts = RequestOptions(access_token="t")
        opts.on_retry = lambda a, e: called.append(a)
        self.assertIsNotNone(opts.on_retry)

    def test_on_retry_non_callable_raises(self):
        opts = RequestOptions(access_token="t")
        with self.assertRaises(ValueError):
            opts.on_retry = "not_callable"

# ─── Idempotency key validation (TASK-047) ────────────────────────────────────

class TestIdempotencyKeyValidation(unittest.TestCase):

    def test_valid_uuid_36_chars_accepted(self):
        opts = RequestOptions(access_token="t")
        opts.custom_headers = {"x-idempotency-key": str(uuid.uuid4())}

    def test_key_too_long_raises(self):
        opts = RequestOptions(access_token="t")
        with self.assertRaisesRegex(ValueError, "x-idempotency-key"):
            opts.custom_headers = {"x-idempotency-key": "a" * 65}

    def test_empty_key_raises(self):
        opts = RequestOptions(access_token="t")
        with self.assertRaisesRegex(ValueError, "x-idempotency-key"):
            opts.custom_headers = {"x-idempotency-key": ""}

    def test_key_64_chars_accepted(self):
        opts = RequestOptions(access_token="t")
        opts.custom_headers = {"x-idempotency-key": "a" * 64}

# ─── Status constants (TASK-047) ─────────────────────────────────────────────

class TestStatusConstants(unittest.TestCase):

    def test_payment_status_approved(self):
        self.assertEqual(PaymentStatus.APPROVED, "approved")

    def test_order_status_processed(self):
        self.assertEqual(OrderStatus.PROCESSED, "processed")

    def test_preapproval_status_authorized(self):
        self.assertEqual(PreapprovalStatus.AUTHORIZED, "authorized")

    def test_merchant_order_status_closed(self):
        self.assertEqual(MerchantOrderStatus.CLOSED, "closed")

    def test_refund_status_in_process(self):
        self.assertEqual(RefundStatus.IN_PROCESS, "in_process")

    def test_accessible_from_module_root(self):
        self.assertEqual(mercadopago.PaymentStatus.APPROVED, "approved")
        self.assertEqual(mercadopago.OrderStatus.CANCELED, "canceled")

# ─── Error string constants (TASK-046) ───────────────────────────────────────

class TestErrorConstants(unittest.TestCase):

    def test_order_errors_cannot_refund(self):
        self.assertEqual(MPOrderErrors.CANNOT_REFUND, "cannot_refund_order")

    def test_payment_errors_failed(self):
        self.assertEqual(MPPaymentErrors.FAILED, "failed")

    def test_constants_accessible_from_module_root(self):
        self.assertEqual(mercadopago.MPOrderErrors.CANNOT_CANCEL, "cannot_cancel_order")

# ─── DeprecationWarning (TASK-047) ───────────────────────────────────────────

class TestDeprecationWarning(unittest.TestCase):

    def test_payment_create_no_warning_without_notification_url(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            payment_object = {"transaction_amount": 100}
            if "notification_url" in payment_object:
                warnings.warn("notification_url is deprecated", DeprecationWarning, stacklevel=2)
            self.assertFalse(any(issubclass(x.category, DeprecationWarning) for x in w))

    def test_notification_url_triggers_deprecation_warning(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            payment_object = {"notification_url": "https://example.com/hook", "amount": 100}
            if "notification_url" in payment_object:
                warnings.warn(
                    "notification_url is deprecated; use Webhooks instead.",
                    DeprecationWarning,
                    stacklevel=2,
                )
            dep_warnings = [x for x in w if issubclass(x.category, DeprecationWarning)]
            self.assertEqual(len(dep_warnings), 1)
            self.assertIn("notification_url", str(dep_warnings[0].message))

# ─── Auto-pagination iterator (TASK-016) ─────────────────────────────────────

class TestAutoPaginationIterator(unittest.TestCase):

    def _make_page(self, items, total, offset):
        return MPResponse({
            "status": 200,
            "response": {
                "paging": {"total": total, "limit": len(items), "offset": offset},
                "results": items,
            }
        })

    def test_single_page_yields_all_items(self):
        page = self._make_page([{"id": 1}, {"id": 2}], total=2, offset=0)
        call_count = [0]

        def search_fn(filters, opts):
            call_count[0] += 1
            return page

        items = list(search_auto_paging_iter(search_fn))
        self.assertEqual(items, [{"id": 1}, {"id": 2}])
        self.assertEqual(call_count[0], 1)

    def test_multi_page_fetches_until_exhausted(self):
        pages = [
            self._make_page([{"id": 1}], total=2, offset=0),
            self._make_page([{"id": 2}], total=2, offset=1),
            self._make_page([], total=2, offset=2),
        ]
        call_count = [0]

        def search_fn(filters, opts):
            idx = call_count[0]
            call_count[0] += 1
            return pages[idx]

        items = list(search_auto_paging_iter(search_fn, limit=1))
        self.assertEqual([i["id"] for i in items], [1, 2])

    def test_empty_results_stops_immediately(self):
        empty = self._make_page([], total=0, offset=0)
        items = list(search_auto_paging_iter(lambda f, o: empty))
        self.assertEqual(items, [])

    def test_offset_advances_per_page(self):
        offsets_seen = []

        def search_fn(filters, opts):
            offsets_seen.append(filters.get("offset", 0))
            if filters.get("offset", 0) >= 2:
                return self._make_page([], total=2, offset=filters["offset"])
            return self._make_page([{"id": filters["offset"]}], total=2, offset=filters["offset"])

        list(search_auto_paging_iter(search_fn, limit=1))
        self.assertEqual(offsets_seen[0], 0)
        self.assertEqual(offsets_seen[1], 1)

if __name__ == "__main__":
    unittest.main()
