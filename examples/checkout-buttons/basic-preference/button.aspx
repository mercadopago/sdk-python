<%@ Page Language="c#" %>
<%@ Import Namespace="mercadopago" %>
<%@ Import Namespace="Newtonsoft.Json" %>
<%@ Import Namespace="Newtonsoft.Json.Linq" %>

	<%
    	MP mp = new MP ("CLIENT_ID", "CLIENT_SECRET");
    	
    	JObject preference = mp.createPreference("{'items':[{'title':'sdk-dotnet','quantity':1,'currency_id':'ARS','unit_price':10.5}]}");    
    %>
    
<!doctype html>
<html>
    <head>
        <title>MercadoPago SDK - Create Preference and Show Checkout Example</title>
    </head>
    <body>
       	<a href="<% Response.Write(preference["response"]["init_point"]); %>" name="MP-Checkout" class="orange-ar-m-sq-arall">Pay</a>
		<script type="text/javascript" src="http://mp-tools.mlstatic.com/buttons/render.js"></script>
    </body>
</html>
