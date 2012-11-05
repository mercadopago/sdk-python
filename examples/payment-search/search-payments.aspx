<%@ Page Language="C#" %>
<!doctype html>
<html>
    <head>
        <title>Search payments</title>
    </head>
    <body>
		<%-- Include Mercadopago library --%>
		<%@ Import Namespace="mercadopago" %>
		<%@ Import Namespace="Newtonsoft.Json" %>
		<%@ Import Namespace="Newtonsoft.Json.Linq" %>
		<%@ Import Namespace="System.Collections.Generic" %>
        <%
        /**
         * MercadoPago SDK
         * Search payments
         * @date 2012/03/29
         * @author hcasatti
         */
        
        // Create an instance with your MercadoPago credentials (CLIENT_ID and CLIENT_SECRET): 
        // Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
        // Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes
        MP mp = new MP ("CLIENT_ID", "CLIENT_SECRET");
      
        // Sets the filters you want
		Dictionary<String, String> filters = new Dictionary<String, String> ();
			filters.Add("site_id", "MLA"); // Argentina: MLA; Brasil: MLB
      
        // Search payment data according to filters
        JObject searchResult = mp.searchPayment (filters);
        
        // Show payment information
            foreach (JObject payment in searchResult.SelectToken ("response.results")) {
                Response.Write(payment["collection"]["id"]+"<br>");
            }
            %>
    </body>
</html>