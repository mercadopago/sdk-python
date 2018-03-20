# coding: UTF-8

"""
MercadoPago SDK
Search funded payments with 12 installments and product name "product_name"
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
        "installments": 12,
        "description": "product_name",
        "operation_type": "regular_payment"
    }
    
    # Search payment data according to filters
    searchResult = mp.search_payment(filters)
    
    # Show payment information
    output = """
    <!doctype html>
    <html>
        <head>
            <title>Search funded payments with 12 installments and product name "product_name"</title>
        </head>
        <body>
            <table border='1'>
                <tr><th>id</th><th>external_reference</th><th>status</th></tr>"""
    for payment in searchResult["response"]["results"]:
        output += "<tr>"
        output += "<td>"+payment["id"]+"\n"
        output += "<td>"+payment["external_reference"]+"\n"
        output += "<td>"+payment["status"]+"\n"
        output += "</tr>"
    output += """
            </table>
        </body>
    </html>
    """
    
    return output
