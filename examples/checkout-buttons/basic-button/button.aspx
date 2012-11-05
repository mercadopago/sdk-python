<%@ Page Language="C#" %>
<!doctype html>
<%--
MercadoPago SDK
Checkout button with MD5 hash
@date 2012/03/29
@author hcasatti
--%>
<%@ Import Namespace="System.Collections.Generic" %>
<%@ Import Namespace="System.Security.Cryptography" %>
<%
// Define item data according to form
Dictionary<String, String> data = new Dictionary<String, String> ();
    // Required
    data.Add ("item_title", "Title");
    data.Add ("item_quantity", "1");
    data.Add ("item_unit_price", "10.00");
    data.Add ("item_currency_id", "ARS"); //Argentina: ARS, Brasil: BRL

    // Optional
    data.Add ("item_id", "CODE_012");
    data.Add ("item_picture_url", "Image URL");
    data.Add ("external_reference", "BILL_001");
    data.Add ("payer_name", "");
    data.Add ("payer_surname", "");
    data.Add ("payer_email", "");
    data.Add ("back_url_success", "https://www.success.com");
    data.Add ("back_url_pending", "");

// Get your Mercadopago credentials (CLIENT_ID and CLIENT_SECRET): 
// Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
// Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes

string md5String =   "CLIENT_ID"+                    
                "CLIENT_SECRET"+                
                data["item_quantity"]+                  // item_quantity
                data["item_currency_id"]+               // item_currency_id
                data["item_unit_price"]+                // item_unit_price

                data["item_id"]+                        // item_id
                data["external_reference"];             // external_reference

// Get md5 hash
string md5 = "";
byte[] textBytes = System.Text.Encoding.Default.GetBytes (md5String);

MD5CryptoServiceProvider cryptHandler;
cryptHandler = new MD5CryptoServiceProvider ();
byte[] hash = cryptHandler.ComputeHash (textBytes);
foreach (byte a in hash) {
    md5 += a.ToString ("x2");
}
%>
<html>
    <head>
        <title>Checkout button with MD5 hash, using AJAX - Form</title>
    </head>
	<body>
		<form action="https://www.mercadopago.com/checkout/init" method="post" enctype="application/x-www-form-urlencoded" target="">
			<!--Required authentication. Get the CLIENT_ID: 
			Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
			Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes -->	
			<input type="hidden" name="client_id" value="CLIENT_ID"/>
		
			<!-- Hash MD5 -->
			<input type="hidden" name="md5" value="<%=md5%>"/>
		   
			<!-- Required -->
			<input type="hidden" name="item_title" value="<%=data["item_title"]%> "/>
			<input type="hidden" name="item_quantity" value="<%=data["item_quantity"]%>"/>
			<input type="hidden" name="item_currency_id" value="<%=data["item_currency_id"]%>"/>
			<input type="hidden" name="item_unit_price" value="<%=data["item_unit_price"]%>"/>
		   
			<!-- Optional -->
			<input type="hidden" name="item_id" value="<%=data["item_id"]%>"/>
			<input type="hidden" name="external_reference" value="<%=data["external_reference"]%>"/>
			<input type="hidden" name="item_picture_url" value="<%=data["item_picture_url"]%>"/>
			<input type="hidden" name="payer_name" value="<%=data["payer_name"]%>"/>
			<input type="hidden" name="payer_surname" value="<%=data["payer_surname"]%>"/>
			<input type="hidden" name="payer_email" value="<%=data["payer_email"]%>"/>
			<input type="hidden" name="back_url_success" value="<%=data["back_url_success"]%>"/>
			<input type="hidden" name="back_url_pending" value="<%=data["back_url_pending"]%>"/>
		   
			<!-- Checkout Button -->
			<button type="submit" class="lightblue-rn-m-tr-arall" name="MP-Checkout">Pagar</button>
		</form>
		
		<!-- More info about render.js: https://developers.mercadopago.com -->
		<script type="text/javascript" src="http://mp-tools.mlstatic.com/buttons/render.js"></script>
	</body>
</html>
