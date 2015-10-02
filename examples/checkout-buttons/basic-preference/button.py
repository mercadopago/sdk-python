# coding: UTF-8

"""
MercadoPago SDK
Create Preference and Show Checkout Example
"""

import os, sys
import mercadopago
import json

def index(req, **kwargs):
    preference = {
      "items": [
        {
          "title": "sdk-python",
          "quantity": 1,
          "currency_id": "ARS",
          "unit_price": 10.5
        }
      ]
    }
    mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")

    preferenceResult = mp.create_preference(preference)

    url = preferenceResult["response"]["init_point"]

    output = """
    <!doctype html>
    <html>
        <head>
            <title>MercadoPago SDK - Create Preference and Show Checkout Example</title>
        </head>
      <body>
        <a href="{url}" name="MP-Checkout" class="blue-l-arall-rn">Pagar</a>
        <script type="text/javascript" src="//resources.mlstatic.com/mptools/render.js"></script>
      </body>
    </html>
    """.format (url=url)
    
    return output
