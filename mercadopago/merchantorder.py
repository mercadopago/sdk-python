from .mercadopagorestclient import MercadoPagoRestClient

class MerchantOrder(MercadoPagoRestClient):
    def __init__(self, client_id, client_secret, access_token, version):
        super(MerchantOrder, self).__init__(client_id, client_secret, access_token, version)

    def create(self, merchant_order):
        access_token = self.get_access_token()
        result = self.get_rest_client().post("/merchant_orders?access_token=" + access_token, merchant_order)
        return result

    def update(self, id, merchant_order):
        access_token = self.get_access_token()
        result = self.get_rest_client().put("/merchant_orders/" + id + "?access_token=" + access_token, merchant_order)
        return result

    def get(self, id):
        access_token = self.get_access_token()
        result = self.get_rest_client().get("/merchant_orders/" + id + "?access_token=" + access_token)
        return result