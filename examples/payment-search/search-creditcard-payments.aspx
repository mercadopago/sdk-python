<%@ Page Language="C#" %>
<!doctype html>
<html>
    <head>
        <title>Search approved credit card payments from 21/10/2011 to 25/10/2011</title>
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
         * Search approved credit card payments from 21/10/2011 to 25/10/2011
         * @date 2012/03/29
         * @author hcasatti
         */
        
        // Create an instance with your MercadoPago credentials (CLIENT_ID and CLIENT_SECRET): 
        // Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
        // Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes
        MP mp = new MP ("CLIENT_ID", "CLIENT_SECRET");
      
        // Sets the filters you want
		Dictionary<String, String> filters = new Dictionary<String, String> ();
            filters.Add("range", "date_created");
            filters.Add("begin_date", "2011-10-21T00:00:00Z");
            filters.Add("end_date", "2011-10-25T24:00:00Z");
            filters.Add("payment_type", "credit_card");
            filters.Add("operation_type", "regular_payment");

        // Search payment data according to filters
        JObject searchResult = mp.searchPayment (filters);
        
        // Show payment information
        %>
        <table border='1'>
            <tr><th>id</th><th>site_id</th><th>external_reference</th><th>status</th></tr>
            <%
            foreach (JObject payment in searchResult.SelectToken ("response.results")) {
                %>
                <tr>
                    <td><%=payment["collection"]["id"]%></td>
                    <td><%=payment["collection"]["external_reference"]%></td>
                    <td><%=payment["collection"]["status"]%></td>
                </tr>
                <%
            }
            %>
        </table>
    </body>
</html>