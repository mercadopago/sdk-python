# coding: UTF-8

"""
MercadoPago SDK
Receive IPN
"""

# Import Mercadopago library
import os, sys
import mercadopago

import json

def index(req, **kwargs):
    # Create an instance with your MercadoPago credentials (CLIENT_ID and CLIENT_SECRET): 
    # Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
    # Venezuela: https://www.mercadopago.com/mlv/herramientas/aplicaciones 
    # Mexico: https://www.mercadopago.com/mlm/herramientas/aplicaciones
    # Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes
    mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")
    
    # Get the payment reported by the IPN. Glossary of attributes response in https://developers.mercadopago.com
    paymentInfo = mp.get_payment_info(kwargs["id"])
    
    # Show payment information
    if paymentInfo["status"] == 200:
        return paymentInfo["response"]
    else:
        return None
