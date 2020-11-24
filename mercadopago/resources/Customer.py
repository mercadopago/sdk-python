from mercadopago.http.httpClient import HttpClient
from mercadopago.core.RequestOptions import RequestOptions
from mercadopago.SDK import Sdk


class Customer(Sdk):
    def __init__(self):
        self.Sdk = Sdk

    #TODO TESTADO OK!!
    def search(self, 
               filters, 
               requestOptions=None):
        if type(filters) is not dict:
            raise Exception('Filters must be a Dictionary')
        if requestOptions !=None and type(requestOptions) is not RequestOptions:
            raise Exception('Param requestOptions must be a RequestOptions Object')

        http_client = HttpClient(self.Sdk)
        return http_client.get(uri='/v1/customers/search', params=filters, requestOptions=requestOptions)
