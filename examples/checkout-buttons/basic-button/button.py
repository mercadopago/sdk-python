# coding: UTF-8

"""
MercadoPago SDK
Checkout button with MD5 hash
@date 2012/03/29
@author hcasatti
"""

import hashlib
import json

def index(req, **kwargs):
    # Get your Mercadopago credentials (CLIENT_ID and CLIENT_SECRET): 
    # Argentina: https:#www.mercadopago.com/mla/herramientas/aplicaciones 
    # Brasil: https:#www.mercadopago.com/mlb/ferramentas/aplicacoes

    data = {
        # Required
        "item_title": "Title",
        "item_quantity": "1",
        "item_unit_price": "10.00",
        "item_currency_id": "ARS", # Argentina: ARS, Brasil: BRL
        
        # Optional
        "item_id": "CODE_012",
        "item_description": "Description",
        "item_picture_url": "Image URL",
        "external_reference": "BILL_001",
        "payer_name": "",
        "payer_surname": "",
        "payer_email": "",
        "back_url_success": "https://www.success.com",
        "back_url_pending": ""
    }

    # Define item data according to form
    md5String = "CLIENT_ID"+                    
                "CLIENT_SECRET"+                
                data["item_quantity"]+                 # item_quantity
                data["item_currency_id"]+              # item_currency_id
                data["item_unit_price"]+               # item_unit_price
                data["item_id"]+                       # item_id
                data["external_reference"];            # external_reference

    # Get md5 hash
    md5 = hashlib.md5(md5String).hexdigest()

    output = """
    <!doctype html>
    <html>
        <head>
            <title>Checkout button with MD5 hash</title>
        </head>
        <body>
            <form action="https://www.mercadopago.com/checkout/init" method="post" enctype="application/x-www-form-urlencoded" target="">
                    <!--Required authentication. Get the CLIENT_ID: 
                    Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
                    Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes -->
                    <input type="hidden" name="client_id" value="CLIENT_ID"/>
                    
                    <!-- hash MD5 -->
                    <input type="hidden" name="md5" value="{md5}"/>
                    
                    <!-- Required -->
                    <input type="hidden" name="item_title" value="{data[item_title]}"/>
                    <input type="hidden" name="item_quantity" value="{data[item_quantity]}"/>
                    <input type="hidden" name="item_currency_id" value="{data[item_currency_id]}"/>
                    <input type="hidden" name="item_unit_price" value="{data[item_unit_price]}"/>
                    
                    <!-- Optional -->
                    <input type="hidden" name="item_id" value="{data[item_id]}"/>
                    <input type="hidden" name="external_reference" value="{data[external_reference]}"/>
                    <input type="hidden" name="item_picture_url" value="{data[item_picture_url]}"/>
                    <input type="hidden" name="payer_name" value="{data[payer_name]}"/>
                    <input type="hidden" name="payer_surname" value="{data[payer_surname]}"/>
                    <input type="hidden" name="payer_email" value="{data[payer_email]}"/>
                    <input type="hidden" name="back_url_success" value="{data[back_url_success]}"/>
                    <input type="hidden" name="back_url_pending" value="{data[back_url_pending]}"/>
                    
                    <!-- Checkout Button -->
                    <button type="submit" class="lightblue-rn-m-tr-arall" name="MP-payButton">Pagar</button>
            </form>
            <!-- More info about render.form.js: https://developers.mercadopago.com -->
            <script type="text/javascript" src="http://mp-tools.mlstatic.com/buttons/render.beta.js"></script>
        </body>
    </html>
    """.format (data=data, md5=md5)
    
    return output
