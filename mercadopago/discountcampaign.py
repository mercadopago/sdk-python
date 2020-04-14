from .mercadopagorestclient import MercadoPagoRestClient

class DiscountCampaign(MercadoPagoRestClient):
    def __init__(self, client_id, client_secret, access_token, version):
        super(DiscountCampaign, self).__init__(client_id, client_secret, access_token, version)

    def get(self, transaction_amount, payer_email, coupon_code):
        access_token = self.get_access_token()
        filters = {}
        filters["access_token"] = access_token
        filters["transaction_amount"] = transaction_amount
        filters["payer_email"] = payer_email
        filters["coupon_code"] = coupon_code

        payment_result = self.get_rest_client().get("/v1/discount_campaigns", filters)
        return payment_result
