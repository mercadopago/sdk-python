# Retries and idempotency

`RequestOptions` defaults to three retries. The policy can be changed per request with `max_retries`, `initial_delay`, `max_delay`, `jitter`, and `retry_on`.

```python
from mercadopago.config import RequestOptions

options = RequestOptions(
    access_token=os.environ["MP_ACCESS_TOKEN"],
    max_retries=3,
    initial_delay=250,
    max_delay=5_000,
    jitter=True,
    custom_headers={"x-idempotency-key": "checkout-0001"},
)
```

Use one stable idempotency key for every logical write operation. Reuse it when retrying the same operation; generate a new key for a new operation. The SDK generates a key when none is supplied, but an application-owned key is safer when a retry can happen across processes.

Persist the key beside the internal order or command before sending the request. After a timeout or `MPConnectionError`, reconcile by resource ID or external reference before repeating the write: the API may have completed it even though the response never arrived. Request option validation accepts keys from 1 to 64 characters.

Retry transport failures, `423`, `429`, and transient `5xx` responses. Do not blindly retry validation or authentication failures. Honor `Retry-After` when present.
