# coding: UTF-8

"""
MercadoPago SDK
Checkout button with MD5 hash, using AJAX - Form
@date 2012/03/29
@author hcasatti
"""

def index(req, **kwargs):
    output = """
    <!doctype html>
    <html>
        <head>
            <title>Checkout button with MD5 hash, using AJAX - Form</title>
        </head>
        <body>
            <form action="md5-generator.py" method="post" enctype="application/x-www-form-urlencoded" target="">
                <!--
                Required authentication. Get the CLIENT_ID: 
                Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
                Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes
                -->
                <input type="hidden" name="client_id" value="CLIENT_ID"/>
                
                <!-- Required -->
                <input type="hidden" name="item_title" value="Title"/>
                <label for="item_quantity">Quantity:</label>
                <select name="item_quantity">
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="5">5</option>
                    <option value="10">10</option>
                </select>
                <input type="hidden" name="item_currency_id" value="ARS"/>
                <input type="hidden" name="item_unit_price" value="10.00"/>
                
                <!-- Optional -->
                <input type="hidden" name="item_id" value="COD_012"/>
                <input type="hidden" name="external_reference" value="BILL_001"/>
                <input type="hidden" name="item_picture_url" value="Image URL"/>
                <input type="hidden" name="payer_name" value="BILL_001"/>
                <input type="hidden" name="payer_surname" value=""/>
                <input type="hidden" name="payer_email" value=""/>
                <input type="hidden" name="back_url_success" value=""/>
                <input type="hidden" name="back_url_pending" value=""/>
                
                <!-- Checkout Button -->
                <button type="submit" class="lightblue-rn-m-tr-arall" name="MP-payButton">Pay</button>
            </form>
            
            <!-- AJAX functionality requires JQuery -->
            <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.1.min.js"></script>		
            <!-- More info about render.js: https://developers.mercadopago.com -->
            <script type="text/javascript" src="http://mp-tools.mlstatic.com/buttons/render.beta.js"></script>
        </body>
    </html>
    """
    
    return output
