# coding: UTF-8

"""
MercadoPago SDK
Create Preference and Show Checkout Example
"""

import os, sys
import mercadopago
import json

def index(req, **kwargs):
    preapprovalPayment = {
        "payer_email": "my_customer@my_site.com",
        "back_url": "http://www.my_site.com",
        "reason": "Monthly subscription to premium package",
        "external_reference": "OP-1234",
        "auto_recurring": {
            "frequency": 1,
            "frequency_type": "months",
            "transaction_amount": 60,
            "currency_id": "BRL",
            "start_date": "2012-12-10T14:58:11.778-03:00",
            "end_date": "2013-06-10T14:58:11.778-03:00"
        }
    }

    mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")

    preapprovalPaymentResult = mp.create_preapproval_payment(preapprovalPayment)

    url = preapprovalPaymentResult["response"]["init_point"]

    output = """
    <!doctype html>
    <html>
        <head>
            <title>MercadoPago SDK - Create Preapproval Payment and Show Subscription Example</title>
        </head>
      <body>
        <a href="{url}" name="MP-Checkout" class="blue-l-arall-rn">Pagar</a>
        <script type="text/javascript" src="//resources.mlstatic.com/mptools/render.js"></script>
      </body>
    </html>
    """.format (url=url)
    
    return output
