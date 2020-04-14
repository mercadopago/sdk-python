from .mercadopagorestclient import MercadoPagoRestClient

class Preference(MercadoPagoRestClient):
    def __init__(self, client_id, client_secret, access_token, version):
        super(Preference, self).__init__(client_id, client_secret, access_token, version)

    def create(self, preference):
        access_token = self.get_access_token()
        preference_result = self.get_rest_client().post("/checkout/preferences?access_token=" + access_token, preference)
        return preference_result

    def update(self, id, preference):
        access_token = self.get_access_token()
        preference_result = self.get_rest_client().put("/checkout/preferences/" + id + "?access_token=" + access_token, preference)
        return preference_result

    def get(self, id):
        access_token = self.get_access_token()
        preference_result = self.get_rest_client().get("/checkout/preferences/" + id + "?access_token=" + access_token)
        return preference_result