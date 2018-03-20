# coding: UTF-8

"""
MercadoPago SDK
Search payments
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
        "external_reference": "Bill001"
    }

    # Search payment data according to filters
    searchResult = mp.search_payment(filters)
    
    # Show payment information
    output = """
    <!doctype html>
    <html>
        <head>
            <title>Search payments</title>
        </head>
        <body>
            <table border='1'>
                <tr><th>id</th><th>external_reference</th><th>status</th></tr>"""
    for payment in searchResult["response"]["results"]:
        output += "<tr>"
        output += "<td>"+payment["id"]+"</td>\n"
        output += "<td>"+payment["external_reference"]+"</td>\n"
        output += "<td>"+payment["status"]+"</td>\n"
        output += "</tr>"
    output += """
            </table>
        </body>
    </html>
    """
    
    return output
