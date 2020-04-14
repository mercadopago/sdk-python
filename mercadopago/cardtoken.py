from .mercadopagorestclient import MercadoPagoRestClient

class CardToken(MercadoPagoRestClient):
    def __init__(self, client_id, client_secret, access_token, version):
        super(CardToken, self).__init__(client_id, client_secret, access_token, version)

    def create(self, cardtoken):
        access_token = self.get_access_token()
        result = self.get_rest_client().post("/v1/card_tokens?access_token=" + access_token, cardtoken)
        return result

    def get(self, id):
        access_token = self.get_access_token()
        result = self.get_rest_client().get("/v1/card_tokens/" + id + "?access_token=" + access_token)
        return result