<%@ Page Language="C#" %>
<!doctype html>
<html>
    <head>
        <title>Search approved payments in last month</title>
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
         * Search approved payments in last month
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
            filters.Add("begin_date", "NOW-1MONTH");
            filters.Add("end_date", "NOW");
            filters.Add("status", "approved");
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
                    <td><%=payment["collection"]["site_id"]%></td>
                    <td><%=payment["collection"]["date_created"]%></td>
                    <td><%=payment["collection"]["operation_type"]%></td>
                    <td><%=payment["collection"]["external_reference"]%></td>
                </tr>
                <%
            }
            %>
        </table>
    </body>
</html>