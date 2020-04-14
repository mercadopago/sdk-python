from .mercadopagorestclient import MercadoPagoRestClient

class Card(MercadoPagoRestClient):
    def __init__(self, client_id, client_secret, access_token, version):
        super(Card, self).__init__(client_id, client_secret, access_token, version)

    def create(self, card):
        access_token = self.get_access_token()
        result = self.get_rest_client().post("/v1/customers/" + id + "/cards?access_token=" + access_token, card)
        return result

    def update(self, id, card):
        access_token = self.get_access_token()
        result = self.get_rest_client().put("/v1/customers/" + id + "/cards?access_token=" + access_token, card)
        return result

    def delete(self, id):
        access_token = self.get_access_token()
        result = self.get_rest_client().delete("/v1/customers/" + id + "/cards?access_token=" + access_token)
        return result

    def get(self, id):
        access_token = self.get_access_token()
        result = self.get_rest_client().get("/v1/customers/" + id + "/cards?access_token=" + access_token)
        return result