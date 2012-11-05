<%@ Page Language="C#" %>
<%--
MercadoPago SDK
Receive IPN
@date 2012/03/29
@author hcasatti
--%>
<%-- Include Mercadopago library --%>
<%@ Import Namespace="mercadopago" %>
<%@ Import Namespace="Newtonsoft.Json" %>
<%@ Import Namespace="Newtonsoft.Json.Linq" %>
<%
// Create an instance with your MercadoPago credentials (CLIENT_ID and CLIENT_SECRET): 
// Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
// Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes
MP mp = new MP ("CLIENT_ID", "CLIENT_SECRET");

// Get the payment reported by the IPN. Glossary of attributes response in https://developers.mercadopago.com
JObject payment_info = mp.getPaymentInfo(Request["id"]);

// Show payment information
if ((int)payment_info["status"] == 200) {
    Response.Write (payment_info["response"]);
}
%>