# coding: UTF-8

"""
MercadoPago SDK
Search payments from two e-mails in January
"""

# Import Mercadopago library
import os, sys
import mercadopago

import json

def index(req, **kwargs):
    # Create an instance with your MercadoPago credentials (CLIENT_ID and CLIENT_SECRET): 
    # Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
    # Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes
    mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")
    
    filters = {
        "payer_email": "mail02@mail02.com%20mail01@mail01.com",
        "begin_date": "2011-01-01T00:00:00Z",
        "end_date": "2011-02-01T00:00:00Z"
    }

    # Search payment data according to filters
    searchResult = mp.search_payment(filters)
    
    # Show payment information
    output = """
    <!doctype html>
    <html>
        <head>
            <title>Search payments from two e-mails in January</title>
        </head>
        <body>
            <table border='1'>
                <tr><th>id</th><th>site_id</th><th>payment_type</th><th>status</th></tr>"""
    for payment in searchResult["response"]["results"]:
        output += "<tr>"
        output += "<td>"+payment["collection"]["id"]+"\n"
        output += "<td>"+payment["collection"]["site_id"]+"\n"
        output += "<td>"+payment["collection"]["payment_type"]+"\n"
        output += "<td>"+payment["collection"]["status"]+"\n"
        output += "</tr>"
    output += """
            </table>
        </body>
    </html>
    """
    
    return output
