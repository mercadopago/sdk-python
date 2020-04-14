from .mercadopagorestclient import MercadoPagoRestClient

class Customer(MercadoPagoRestClient):
    def __init__(self, client_id, client_secret, access_token, version):
        super(Customer, self).__init__(client_id, client_secret, access_token, version)

    def get(self, id):
        access_token = self.get_access_token()
        result = self.get_rest_client().get("/v1/customers/" + id + "?access_token=" + access_token)
        return result

    def create(self, customer):
        access_token = self.get_access_token()
        response = self.get_rest_client().post("/v1/customers?access_token=" + access_token, customer)
        return response

    def update(self, id, customer):
        access_token = self.get_access_token()
        response = self.get_rest_client().put("/v1/customers/" + id + "?access_token=" + access_token, customer)
        return response

    def delete(self, id):
        access_token = self.get_access_token()
        result = self.get_rest_client().delete("/v1/customers/" + id + "?access_token=" + access_token)
        return result

    def search(self, filters):#, offset=0, limit=0
        access_token = self.get_access_token()
        #tem?
        #filters["offset"] = offset
        #filters["limit"] = limit
        filters["access_token"] = access_token

        result = self.get_rest_client().get("/v1/customers/search", filters)
        return result
