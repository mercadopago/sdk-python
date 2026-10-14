# Configure the Python SDK

Create one `SDK` instance with an access token stored outside source control:

```python
import os
import mercadopago

sdk = mercadopago.SDK(os.environ["MP_ACCESS_TOKEN"])
```

All API methods accept an optional `RequestOptions` instance for a single call:

```python
from mercadopago.config import RequestOptions

options = RequestOptions(
    access_token=os.environ["MP_ACCESS_TOKEN"],
    connection_timeout=30.0,
    max_retries=3,
    custom_headers={"x-idempotency-key": "order-2026-0001"},
)
result = sdk.order().get("ORDER_ID", options)
```

`RequestOptions` also supports `corporation_id`, `integrator_id`, `platform_id`, retry delays, jitter, custom retry status codes, and an `on_retry` callback. Prefer per-request overrides when different credentials or policies share one process.

Create and reuse the `SDK` instance for the lifetime of the application instead of rebuilding it inside every handler. Treat `connection_timeout` as a per-attempt limit: retry delays can make the complete operation longer, so keep the combined worst case below the request or job deadline.

If multiple seller credentials share a process, pass the correct token in request-scoped options and keep tenant selection outside user-controlled headers. Corporation, integrator, and platform identifiers are partner metadata; set them only when they were assigned to the integration.

Never log an access token or commit it to the repository.
