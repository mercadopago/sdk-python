# Handle errors in the Python SDK

The SDK raises subclasses of `MercadoPagoError` for API failures. Catch the most specific error you can recover from, then keep a final base-class handler.

```python
from mercadopago.errors import MPRateLimitError, MPValidationError, MercadoPagoError

try:
    result = sdk.order().create(order_data, request_options)
except MPRateLimitError as error:
    print("Retry after:", error.retry_after)
except MPValidationError as error:
    print("Invalid request:", error.causes)
except MercadoPagoError as error:
    print(error.status_code, error.error, error.request_id)
```

| Status | Exception | Typical action |
|---|---|---|
| 400 | `MPBadRequestError` | Fix syntax or required fields. |
| 401 | `MPAuthenticationError` | Replace the access token. |
| 409 | `MPIdempotencyError` | Check the idempotency key and previous result. |
| 422 | `MPValidationError` | Fix business-rule violations. |
| 423 | `MPResourceLockedError` | Retry later with the same idempotency key. |
| 429 | `MPRateLimitError` | Honor `retry_after`. |
| 5xx | `MPServerError` | Retry with a bounded policy. |

`MPConnectionError` represents failures where no HTTP response was received. See [retries and idempotency](retries-and-idempotency.md) before retrying a write.
