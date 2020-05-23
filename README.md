# Mercado Pago SDK for Python

[![PyPI](https://img.shields.io/pypi/v/mercadopago.svg)](https://pypi.python.org/pypi/mercadopago)

## 💡 Requirements

Python 2 or major

## 📲 Installation 

First time using Mercado Pago? Create your [Mercado Pago account](https://www.mercadopago.com), if you don’t have one already.

**On Python 2.x**

`pip install mercadopago`

**On Python 3.x**

`pip3 install mercadopago`

Copy the access_token in the [credentials](https://www.mercadopago.com/mlb/account/credentials) section of the page and replace YOUR_ACCESS_TOKEN with it.

Thats all, you have Mercado Pago SDK installed.

## 🌟 Getting Started

  Simple usage looks like:
  
```python
      import mercadopago
      import json

      mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")
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

See our Documentation with all APIs you can integrate in our DevSite: [Spanish](https://www.mercadopago.com.ar/developers/es/guides/payments/api/introduction/) / [Portuguese](https://www.mercadopago.com.br/developers/pt/guides/payments/api/introduction/)

Check our official code reference to explore all available functionalities.

## ❤️ Support 

If you require technical support, please contact our support team at [developers.mercadopago.com](https://developers.mercadopago.com)

## 🏻 License 

```
MIT license. Copyright (c) 2018 - Mercado Pago / Mercado Libre 
For more information, see the LICENSE file.
```
