# Mercado Pago Python SDK documentation

Use the root README to install the SDK and send a first request. This index provides the shortest path from a runnable Orders example to a production-ready integration.

## Start with Orders

Orders is the recommended learning path because it demonstrates the complete payment lifecycle. Begin with [create_order](../mercadopago/examples/order/create_order.py), inspect the result with [get_order](../mercadopago/examples/order/get_order.py), and continue with [process_order](../mercadopago/examples/order/process_order.py), [capture_order](../mercadopago/examples/order/capture_order.py), [cancel_order](../mercadopago/examples/order/cancel_order.py), or [refund_total](../mercadopago/examples/order/refund_total.py).

Before production traffic, configure [retries and idempotency](retries-and-idempotency.md), [typed errors](error-handling.md), and the [production checklist](production-checklist.md). The [Orders-first example catalog](../examples/README.md#orders-first) also covers Checkout Pro, transactions, PSE, stored credentials, and automatic payments.

## Operational guides

| Question | Guide |
|---|---|
| How should credentials and request options be configured? | [Configuration](configuration.md) |
| How should failures be classified? | [Error handling](error-handling.md) |
| When is a repeated write safe? | [Retries and idempotency](retries-and-idempotency.md) |
| How should search results be iterated? | [Pagination](pagination.md) |
| How should signed notifications be processed? | [Webhook validation](webhooks.md) |
| Which resources are exposed? | [API resources](api-resources.md) |
| What should be checked before launch or during an incident? | [Production checklist](production-checklist.md) · [Troubleshooting](troubleshooting.md) |

Endpoint fields and response schemas belong to the [Mercado Pago API reference](https://www.mercadopago.com/developers/en/reference).
