# coding: UTF-8

"""
MercadoPago SDK
Search approved payments in last month
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
        "range": "date_created",
        "begin_date": "NOW-1MONTH",
        "end_date": "NOW",
        "status": "approved",
        "operation_type": "regular_payment"
    }

    # Search payment data according to filters
    searchResult = mp.search_payment(filters)
    
    # Processes the payment information
    output = """
    <!doctype html>
    <html>
        <head>
            <title>Search approved payments in last month</title>
        </head>
        <body>
            <table border='1'>
                <tr><th>id</th><th>site_id</th><th>date_created</th><th>operation_type</th><th>external_reference</th></tr>"""
    for payment in searchResult["response"]["results"]:
        output += "<tr>"
        output += "<td>"+payment["collection"]["id"]+"</td>\n"
        output += "<td>"+payment["collection"]["site_id"]+"</td>\n"
        output += "<td>"+payment["collection"]["date_created"]+"</td>\n"
        output += "<td>"+payment["collection"]["operation_type"]+"</td>\n"
        output += "<td>"+payment["collection"]["external_reference"]+"</td>\n"
        output += "</tr>"
    output += """
            </table>
        </body>
    </html>
    """
    
    return output
