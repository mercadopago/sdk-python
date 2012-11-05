# MercadoPago SDK module for Payments integration

* [Usage](#usage)
* [Using MercadoPago Checkout](#checkout)
* [Using MercadoPago Payment collection](#payments)

<a name="usage"></a>
## Usage:

1. Copy bin/mercadopago.dll and bin/Newtonsoft.Json.dll to your project desired folder.

* Get your **CLIENT_ID** and **CLIENT_SECRET** in the following address:
	* Argentina: [https://www.mercadopago.com/mla/herramientas/aplicaciones](https://www.mercadopago.com/mla/herramientas/aplicaciones)
	* Brazil: [https://www.mercadopago.com/mlb/ferramentas/aplicacoes](https://www.mercadopago.com/mlb/ferramentas/aplicacoes)

```C#
using mercadopago;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

MP mp = new MP ("CLIENT_ID", "CLIENT_SECRET");
```

<a name="checkout"></a>
## Using MercadoPago Checkout

### Get an existent Checkout preference:

```C#
JObject preference = mp.getPreference("PREFERENCE_ID");

Response.Write(preference);
```

### Create a Checkout preference:

```C#
JObject preference = mp.createPreference("{'items':[{'title':'sdk-dotnet','quantity':1,'currency_id':'ARS','unit_price':10.5}]}");    

Response.Write(preference);
```

### Update an existent Checkout preference:

```C#
JObject preference = mp.updatePreference("PREFERENCE_ID", "{'items':[{'title':'sdk-dotnet','quantity':1,'currency_id':'USD','unit_price':2}]}");    

Response.Write(preference);
```

<a name="payments"></a>
## Using MercadoPago Payment

### Searching:

```C#
// Sets the filters you want
Dictionary<String, String> filters = new Dictionary<String, String> ();
	filters.Add("site_id", "MLA"); // Argentina: MLA; Brasil: MLB
	filters.Add("external_reference", "Bill001");
      
// Search payment data according to filters
JObject searchResult = mp.searchPayment (filters);

foreach (JObject payment in searchResult.SelectToken ("response.results")) {
	Response.Write(payment["collection"]["id"]);
	Response.Write(payment["collection"]["status"]);
}
```

### Receiving IPN notification:

* Go to **Mercadopago IPN configuration**:
	* Argentina: [https://www.mercadopago.com/mla/herramientas/notificaciones](https://www.mercadopago.com/mla/herramientas/notificaciones)
	* Brasil: [https://www.mercadopago.com/mlb/ferramentas/notificacoes](https://www.mercadopago.com/mlb/ferramentas/notificacoes)<br />
	
```C#
JObject payment_info = mp.getPaymentInfo("ID");

Response.Write(payment_info["response"]);
```    

### Cancel (only for pending payments):

```C#
JObject result = mp.cancelPayment("ID");

// Show result
Response.Write(result);
```

### Refund (only for accredited payments):

```C#
JObject result = mp.refundPayment("ID");

// Show result
Response.Write(result);
```
