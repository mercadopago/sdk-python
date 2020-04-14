from .mercadopagorestclient import MercadoPagoRestClient

class GenericCall(MercadoPagoRestClient):
    def __init__(self, client_id, client_secret, access_token, version):
        super(GenericCall, self).__init__(client_id, client_secret, access_token, version)

    def get(self, uri, params=None, authenticate=True):
        if params is None:
            params = {}

        if authenticate:
            access_token = self.get_access_token()
            params["access_token"] = access_token

        result = self.get_rest_client().get(uri, params)
        return result

    def post(self, uri, data, params=None):
        if params is None:
            params = {}

        access_token = self.get_access_token()
        params["access_token"] = access_token
        result = self.get_rest_client().post(uri, data, params)
        return result

    def put(self, uri, data, params=None):
        if params is None:
            params = {}

        access_token = self.get_access_token()
        params["access_token"] = access_token
        result = self.get_rest_client().put(uri, data, params)
        return result

    def delete(self, uri, params=None):
        if params is None:
            params = {}

        access_token = self.get_access_token()
        params["access_token"] = access_token
        result = self.get_rest_client().delete(uri, params)
        return result
