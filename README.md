# Mercado Pago SDK for Python

[![PyPI](https://img.shields.io/pypi/v/mercadopago.svg)](https://pypi.python.org/pypi/mercadopago)
[![PyPI Downloads](https://img.shields.io/pypi/dm/mercadopago.svg)](https://pypi.python.org/pypi/mercadopago)
[![APM](https://img.shields.io/apm/l/vim-mode)](https://github.com/mercadopago/sdk-python)

This library provides developers with a simple set of bindings to help you integrate Mercado Pago API to a website and start receiving payments.

## 💡 Requirements

Python 3.7 or higher.

## 📲 Installation 

Run ```pip3 install mercadopago```

## 🌟 Getting Started

First time using Mercado Pago? Create your [Mercado Pago account](https://www.mercadopago.com).

Copy your `Access Token` in the [credentials panel](https://www.mercadopago.com/developers/panel/credentials) and replace the text `YOUR_ACCESS_TOKEN` with it.

### Simple usage
  
```python
import mercadopago

sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")

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
result = sdk.payment().create(payment_data)
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

Visit our Dev Site for further information regarding:
 - [APIs](https://www.mercadopago.com/developers/en/reference)
 - [Checkout Pro](https://www.mercadopago.com/developers/en/guides/online-payments/checkout-pro/introduction)
 - [Checkout API](https://www.mercadopago.com/developers/en/guides/online-payments/checkout-api/introduction)
 - [Web Tokenize Checkout](https://www.mercadopago.com/developers/en/guides/online-payments/web-tokenize-checkout/introduction)

Check our official code reference to explore all available functionalities.

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
