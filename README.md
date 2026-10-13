<div align="center">
  <img src=".github/assets/mercado-pago.svg" alt="Mercado Pago" width="120" />
  <h1>Mercado Pago SDK for Python</h1>
  <p><strong>The official Mercado Pago SDK for Python applications.</strong></p>
  <p>Integrate Mercado Pago APIs into your Python application and start receiving payments.</p>
  <p>
    <a href="https://github.com/mercadopago/sdk-python/actions/workflows/ci.yml"><img src=".github/assets/badges/ci.svg" alt="CI workflow" /></a>
    <a href="#installation"><img src=".github/assets/badges/package.svg" alt="Python package" /></a>
    <img src=".github/assets/badges/runtime.svg" alt="Python 3.10 or later" />
    <a href="LICENSE"><img src=".github/assets/badges/license.svg" alt="MIT license" /></a>
  </p>
  <p>
    <a href="#installation">Installation</a> ·
    <a href="#getting-started">Getting started</a> ·
    <a href="#documentation">Documentation</a> ·
    <a href="#contributing">Contributing</a>
  </p>
</div>

---

## 💡 Requirements

Python 3.10 or higher.

## 📲 Installation

Run ```pip3 install mercadopago```

## 🌟 Getting Started

First time using Mercado Pago? Create your [Mercado Pago account](https://www.mercadopago.com).

Copy your `Access Token` in the [credentials panel](https://www.mercadopago.com/developers/panel/credentials) and replace the text `YOUR_ACCESS_TOKEN` with it.

### Simple usage — Orders API

The [Orders API](https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/create-order/post) (`/v1/orders`) is the recommended way to accept payments. `sdk.order().create()` accepts either a plain `dict` or the optional typed request dataclasses (`OrderCreateRequest` and friends). Both routes produce the exact same JSON body.

```python
import mercadopago

sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")

request_options = mercadopago.config.RequestOptions()
request_options.custom_headers = {
    'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
}

order_data = {
    "type": "online",
    "total_amount": "100.00",
    "external_reference": "ext_ref_1234",
    "transactions": {
        "payments": [
            {
                "amount": "100.00",
                "payment_method": {
                    "id": "master",
                    "type": "credit_card",
                    "token": "CARD_TOKEN",
                    "installments": 1,
                },
            }
        ]
    },
    "payer": {
        "email": "test_user_123456@testuser.com"
    },
}
result = sdk.order().create(order_data, request_options)
order = result["response"]

print(order)
```

#### Typed request classes (optional)

Instead of a `dict`, you can build the request with the typed dataclasses. `None`
fields are omitted from the JSON body automatically, matching the `dict` route.

```python
import mercadopago
from mercadopago.resources.order_create import OrderCreateRequest
from mercadopago.resources.payer import PayerRequest
from mercadopago.resources.item import ItemRequest

sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")

order = OrderCreateRequest(
    type="online",
    total_amount="100.00",
    external_reference="ext_ref_1234",
    payer=PayerRequest(email="test_user_123456@testuser.com"),
    items=[ItemRequest(title="A book", unit_price="100.00", quantity=1)],
)

result = sdk.order().create(order)
print(result["response"])
```

For a complete recurring / Automatic Payments example (stored credential,
subscription data, integration data), see
[`examples/order/create_order_automatic_payment.py`](examples/order/create_order_automatic_payment.py).

### Creating a payment (legacy Payments API)

```python
import mercadopago

sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")

request_options = mercadopago.config.RequestOptions()
request_options.custom_headers = {
    'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
}

payment_data = {
    "transaction_amount": 100,
    "token": "CARD_TOKEN",
    "description": "Payment description",
    "payment_method_id": 'visa',
    "installments": 1,
    "payer": {
        "email": 'test_user_123456@testuser.com'
    }
}
result = sdk.payment().create(payment_data, request_options)
payment = result["response"]

print(payment)
```

### Per-request configuration

All methods that make API calls accept an optional `RequestOptions` object. This can be used to configure some special options of the request, such as changing credentials or custom headers.

```python
import mercadopago
from mercadopago.config import RequestOptions

request_options = RequestOptions(access_token='YOUR_ACCESS_TOKEN')
# ...

result = sdk.payment().create(payment_data, request_options)
payment = result["response"]
```

## 📚 Documentation

- [SDK guides](docs/README.md): configuration, errors, retries, pagination, and webhooks.
- [Examples](examples/README.md): runnable integration flows supported by this SDK.
- [API resources](docs/api-resources.md): SDK clients and their common operations.
- [API reference](https://www.mercadopago.com/developers/en/reference): request fields and response schemas.

## 🤝 Contributing

All contributions are welcome, ranging from people wanting to triage issues, others wanting to write documentation, to people wanting to contribute code.

Please read and follow our [contribution guidelines](CONTRIBUTING.md). Contributions not following this guidelines will be disregarded. The guidelines are in place to make all of our lives easier and make contribution a consistent process for everyone.

## ❤️ Support

If you require technical support, please contact our support team at [developers.mercadopago.com](https://developers.mercadopago.com).

## 🏻 License

```
MIT license. Copyright (c) 2021 - Mercado Pago / Mercado Libre
For more information, see the LICENSE file.
```
