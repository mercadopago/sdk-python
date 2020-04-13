from .mercadopagorestclient import MercadoPagoRestClient

class IdentificationType(MercadoPagoRestClient):
    def __init__(self, client_id, client_secret, access_token):
        super(IdentificationType, self).__init__(client_id, client_secret, access_token)

    def get(self, id):
        access_token = self.get_access_token()
        result = self.__rest_client.get("/v1/identification_types?access_token=" + access_token)
        return result