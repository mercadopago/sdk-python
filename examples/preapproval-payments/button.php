<?php
require_once "../../lib/mercadopago.php";

$mp = new MP("CLIENT_ID", "CLIENT_SECRET");

$preapprovalPayment = array(
    "payer_email" => "my_customer@my_site.com",
    "back_url" => "http://www.my_site.com",
    "reason" => "Monthly subscription to premium package",
    "external_reference" => "OP-1234",
    "auto_recurring" => array(
        "frequency" => 1,
        "frequency_type" => "months",
        "transaction_amount" => 60,
        "currency_id" => "BRL",
        "start_date" => "2012-12-10T14:58:11.778-03:00",
        "end_date" => "2013-06-10T14:58:11.778-03:00"
    )
);

$preapprovalPaymentResult = $mp->create_preapproval_payment($preapprovalPayment);
?>

<!doctype html>
<html>
    <head>
        <title>MercadoPago SDK - Create Preapproval Payment and Show Subscription Example</title>
    </head>
    <body>
       	<a href="<?php echo $preapprovalPaymentResult["response"]["init_point"]; ?>" name="MP-Checkout" class="orange-ar-m-sq-arall">Pay</a>
        <script type="text/javascript" src="http://mp-tools.mlstatic.com/buttons/render.js"></script>
    </body>
</html>
