# Python examples

These programs demonstrate integration flows implemented by the Python SDK. Start with Orders, then choose another API only when the payment product requires it.

## Orders first

Orders is the most complete learning path in this repository: it covers creation, retrieval, processing, capture, cancellation, refunds, and transaction management.

| Stage | Goal | Example |
|---|---|---|
| 1. Create | Submit a basic order | [`create_order.py`](../mercadopago/examples/order/create_order.py) |
| 2. Inspect | Retrieve the server-side result | [`get_order.py`](../mercadopago/examples/order/get_order.py) |
| 3. Advance | Process or capture an order | [`process_order.py`](../mercadopago/examples/order/process_order.py) · [`capture_order.py`](../mercadopago/examples/order/capture_order.py) |
| 4. Reverse | Cancel, partially refund, or fully refund | [`cancel_order.py`](../mercadopago/examples/order/cancel_order.py) · [`refund_partial.py`](../mercadopago/examples/order/refund_partial.py) · [`refund_total.py`](../mercadopago/examples/order/refund_total.py) |
| 5. Manage transactions | Create, update, or delete a transaction | [`create_transaction.py`](../mercadopago/examples/order/create_transaction.py) · [`update_transaction.py`](../mercadopago/examples/order/update_transaction.py) · [`delete_transaction.py`](../mercadopago/examples/order/delete_transaction.py) |
| 6. Add a payment flow | Use Checkout Pro or PSE | [`create_order_checkout_pro.py`](../mercadopago/examples/order/create_order_checkout_pro.py) · [`create_order_pse.py`](../mercadopago/examples/order/create_order_pse.py) |
| 7. Use stored credentials | Create credential-on-file or automatic payments | [`create_order_credential_on_file.py`](order/create_order_credential_on_file.py) · [`create_order_automatic_payment.py`](order/create_order_automatic_payment.py) |

Before production use, persist the idempotency key and handle typed exceptions. See [retries and idempotency](../docs/retries-and-idempotency.md), [error handling](../docs/error-handling.md), and the [production checklist](../docs/production-checklist.md).

## Other supported examples

| Goal | API | Examples |
|---|---|---|
| Create a hosted checkout | Preferences API | [`mercadopago/examples/preference/`](../mercadopago/examples/preference/) |
| Connect a seller account | OAuth API | [`mercadopago/examples/oauth/`](../mercadopago/examples/oauth/) |

## Before running an example

1. Install this checkout with `python -m pip install -e .`.
2. Replace placeholders with test credentials and test data.
3. Set a stable `x-idempotency-key` for each logical write.
4. Confirm fields in the [API reference](https://www.mercadopago.com/developers/en/reference).

Never commit credentials or use production card data in examples.
