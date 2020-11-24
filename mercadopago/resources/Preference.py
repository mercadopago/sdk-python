from mercadopago.http.httpClient import HttpClient
from mercadopago.core.RequestOptions import RequestOptions
from mercadopago.SDK import Sdk


class Preference():
    def __init__(self, Sdk):
        self.Sdk = Sdk
        
    #TODO TESTE OK!!
    def search(self, id):
        if type(id) is not str:
            raise Exception('ID must be a String') 
               
        http_client = HttpClient(self.Sdk)
        return http_client.get(uri="/checkout/preferences/search", params=id)

    #TODO SEM TESTE
    def findById(self, 
                 id, 
                 requestOptions=None):
        if type(id) is not str:
            raise Exception('ID must be a String')     
        if type(requestOptions) is not RequestOptions:
            raise Exception('Param requestOptions must be a RequestOptions Object')    
                       
        http_client = HttpClient(self.Sdk)
        return http_client.get(uri="/checkout/preferences/" + id, requestOptions=requestOptions)

    #TODO SEM TESTE
    def save(self, requestOptions):        
        if requestOptions != None:
        
            http_client = HttpClient(self.Sdk)
            return http_client.post(uri="/checkout/preferences/", requestOptions=requestOptions)

    #TODO SEM TESTE
    def update(self, requestOptions):
        if requestOptions != None:

            http_client = HttpClient(self.Sdk)
            return http_client.put(uri="/v1/payments/" + id, requestOptions=requestOptions)
