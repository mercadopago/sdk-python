# Validate webhook signatures

Use `WebhookSignatureValidator` before trusting a signed notification:

```python
from mercadopago.webhook import WebhookSignatureValidator

WebhookSignatureValidator.validate(
    x_signature=request.headers.get("x-signature"),
    x_request_id=request.headers.get("x-request-id"),
    data_id=request.args.get("data.id"),
    secret=os.environ["MP_WEBHOOK_SECRET"],
    tolerance_seconds=300,
)
```

The validator uses a constant-time comparison and raises `InvalidWebhookSignatureError` when validation fails. Pass header and query values exactly as received.

Respond with HTTP `200` or `201` promptly and process business work asynchronously. QR Code notifications are not signed and must not be passed to this validator.

After validation, deduplicate by notification or resource identifier, enqueue the identifier, and fetch the current resource from Mercado Pago in the worker. Apply changes idempotently because notifications may repeat or arrive out of order. The notification is a change signal; the API lookup is the current resource state.

Never log the secret or the complete signature.
