# Mercado Pago SDK for Python

[![PyPI](https://img.shields.io/pypi/v/mercadopago.svg)](https://pypi.python.org/pypi/mercadopago)
[![PyPI Downloads](https://img.shields.io/pypi/dm/mercadopago.svg)](https://pypi.python.org/pypi/mercadopago)
[![APM](https://img.shields.io/apm/l/vim-mode)](https://github.com/mercadopago/sdk-python)

This library provides developers with a simple set of bindings to help you integrate Mercado Pago API to a website and start receiving payments.

## 💡 Requirements

Python 2 or higher

## 📲 Installation 

First time using Mercado Pago? Create your [Mercado Pago account](https://www.mercadopago.com), if you don’t have one already.

**On Python 2.x**

`pip install mercadopago`

**On Python 3.x**

`pip3 install mercadopago`

Copy the access_token in the [credentials](https://www.mercadopago.com/mlb/account/credentials) section of the page and replace YOUR_ACCESS_TOKEN with it.

That's it! Mercado Pago SDK has been successfully installed.

## 🌟 Getting Started

  Simple usage looks like:
  
```python
import mercadopago
import json

mp = mercadopago.MP("YOUR_ACCESS_TOKEN")

def index(req, **kwargs):
    preference = {
        "items": [
            {
                "title": "Test",
                "quantity": 1,
                "currency_id": "USD",
                "unit_price": 10.4
            }
        ]
    }

    mp.create_preference(preference)
```

## 📚 Documentation 

Visit our Dev Site for further information regarding:
 - Payments APIs: [Spanish](https://www.mercadopago.com.ar/developers/es/guides/payments/api/introduction/) / [Portuguese](https://www.mercadopago.com.br/developers/pt/guides/payments/api/introduction/)
 - Mercado Pago checkout: [Spanish](https://www.mercadopago.com.ar/developers/es/guides/payments/web-payment-checkout/introduction/) / [Portuguese](https://www.mercadopago.com.br/developers/pt/guides/payments/web-payment-checkout/introduction/)
 - Web Tokenize checkout: [Spanish](https://www.mercadopago.com.ar/developers/es/guides/payments/web-tokenize-checkout/introduction/) / [Portuguese](https://www.mercadopago.com.br/developers/pt/guides/payments/web-tokenize-checkout/introduction/)

Check our official code reference to explore all available functionalities.

## ❤️ Support 

If you require technical support, please contact our support team at [developers.mercadopago.com](https://developers.mercadopago.com)

## 🏻 License 

```
MIT license. Copyright (c) 2018 - Mercado Pago / Mercado Libre 
For more information, see the LICENSE file.
```