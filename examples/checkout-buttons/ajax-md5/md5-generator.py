# coding: UTF-8

"""
MercadoPago SDK
Checkout button with MD5 hash, using AJAX - MD5 Generator
@date 2012/03/29
@author hcasatti
"""

import hashlib
import json

def index(req, **kwargs):
    # Get your Mercadopago credentials (CLIENT_ID and CLIENT_SECRET): 
    # Argentina: https:#www.mercadopago.com/mla/herramientas/aplicaciones 
    # Brasil: https:#www.mercadopago.com/mlb/ferramentas/aplicacoes

    # Define item data according to form
    data =  "CLIENT_ID"+                    
            "CLIENT_SECRET"+                
            "1"+                            # item_quantity
            "ARS"+                          # item_currency_id
            "10.00"+                        # item_unit_price

            "CODE_012"+                     # item_id
            "BILL_001"+                     # external_reference
            ""+                             # excluded_payment_types_id
            ""+                             # excluded_payment_methods_id
            "";                             # credit_card_installments

    # Get md5 hash
    md5 = hashlib.md5(data).hexdigest()

    output = '{{"md5":"{0}"}}'.format (md5)
    return output
