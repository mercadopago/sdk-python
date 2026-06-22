# Mercado Pago SDK for Python

[![PyPI](https://img.shields.io/pypi/v/mercadopago.svg)](https://pypi.python.org/pypi/mercadopago)
[![PyPI Downloads](https://img.shields.io/pypi/dm/mercadopago.svg)](https://pypi.python.org/pypi/mercadopago)
[![APM](https://img.shields.io/apm/l/vim-mode)](https://github.com/mercadopago/sdk-python)

This library provides developers with a simple set of bindings to help you integrate Mercado Pago API to a website and start receiving payments.

## 🤖 Automated Code Generation

This SDK is partially generated using [OpenAPI Generator](https://openapi-generator.tech/) from the official Mercado Pago API specifications. New features and endpoints are automatically created when the OpenAPI specs are updated, ensuring the SDK stays synchronized with the latest API changes.

### Generation Process

- **Base client code**: Generated from OpenAPI specifications
- **Custom refinements**: Applied to follow SDK conventions and best practices
- **Manual implementations**: Some resources include handcrafted code for enhanced developer experience

The automated generation allows us to rapidly deliver new API features while maintaining consistency and type safety across the SDK.

## 💡 Requirements

Python 3.9 or higher.

## 📲 Installation 

Run ```pip3 install mercadopago```

## 🌟 Getting Started

First time using Mercado Pago? Create your [Mercado Pago account](https://www.mercadopago.com).

Copy your `Access Token` in the [credentials panel](https://www.mercadopago.com/developers/panel/credentials) and replace the text `YOUR_ACCESS_TOKEN` with it.

### Simple usage
  
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

Visit our Dev Site for further information regarding:
 - [APIs](https://www.mercadopago.com/developers/en/reference)
 - [Checkout Pro](https://www.mercadopago.com/developers/en/guides/online-payments/checkout-pro/introduction)
 - [Checkout API](https://www.mercadopago.com/developers/en/guides/online-payments/checkout-api/introduction)
 - [Web Tokenize Checkout](https://www.mercadopago.com/developers/en/guides/online-payments/web-tokenize-checkout/introduction)

Check our official code reference to explore all available functionalities.

## 🔄 OpenAPI Specifications

This SDK leverages OpenAPI specifications to ensure accuracy and completeness. If you notice any discrepancies between the SDK and the API documentation, please:

1. Check the [API Reference](https://www.mercadopago.com/developers/en/reference) for the latest specifications
2. Report issues in our [GitHub repository](https://github.com/mercadopago/sdk-python/issues)
3. Include the OpenAPI spec version if applicable

## 🤝 Contributing

All contributions are welcome, ranging from people wanting to triage issues, others wanting to write documentation, to people wanting to contribute code.

Please read and follow our [contribution guidelines](CONTRIBUTING.md). Contributions not following this guidelines will be disregarded. The guidelines are in place to make all of our lives easier and make contribution a consistent process for everyone.

### Contributing to Generated Code

When contributing to resources that are auto-generated from OpenAPI specs, please note:

- Direct modifications to generated files may be overwritten on the next generation cycle
- Suggest changes to the OpenAPI specification or the generation templates instead
- Custom extensions and refinements should be clearly documented

## ❤️ Support

If you require technical support, please contact our support team at [developers.mercadopago.com](https://developers.mercadopago.com).

## 🏻 License

```
MIT license. Copyright (c) 2021 - Mercado Pago / Mercado Libre
For more information, see the LICENSE file.
```