from mercadopago.http.httpClient import HttpClient
from mercadopago.core.RequestOptions import RequestOptions
from mercadopago.SDK import Sdk


class Payment(Sdk):
    def __init__(self, Sdk):
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
        return http_client.get(uri="/v1/payments/search", params=filters, requestOptions=requestOptions)

    #TODO SEM TESTE
    def find_by_id(self, 
                 id, 
                 requestOptions=None):
        if type(id) is not str:
            raise Exception('ID must be a String')     
        if requestOptions !=None and type(requestOptions) is not RequestOptions:
            raise Exception('Param requestOptions must be a RequestOptions Object')    
                       
        http_client = HttpClient(self.Sdk)
        return http_client.get(uri="/v1/payments/" + str(id), requestOptions=requestOptions)

    #TODO SEM TESTE
    def save(self, requestOptions):        
        if requestOptions !=None:
        
            http_client = HttpClient(self.Sdk)
            return http_client.post(uri="/v1/payments/", requestOptions=requestOptions)

    #TODO SEM TESTE 
    def update(self, requestOptions):
        if requestOptions !=None:

            http_client = HttpClient(self.Sdk)
            return http_client.put(uri="/v1/payments/" + id, requestOptions=requestOptions)
