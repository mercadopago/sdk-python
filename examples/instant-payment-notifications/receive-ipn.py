# coding: UTF-8

"""
MercadoPago SDK
Receive IPN
@date 2012/03/29
@author hcasatti
"""

# Import Mercadopago library
import os, sys
sys.path.append(os.path.dirname(__file__)+"/../../lib")
import mercadopago

import json

def index(req, **kwargs):
    # Create an instance with your MercadoPago credentials (CLIENT_ID and CLIENT_SECRET): 
    # Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
    # Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes
    mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")
    
    # Get the payment reported by the IPN. Glossary of attributes response in https://developers.mercadopago.com
    paymentInfo = mp.get_payment_info (kwargs["id"])
    
    # Show payment information
    if paymentInfo["status"] == 200:
        return paymentInfo["response"]
    else:
        return None
