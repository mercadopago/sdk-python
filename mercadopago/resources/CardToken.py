from mercadopago.http.httpClient import HttpClient
from mercadopago.core.RequestOptions import RequestOptions
from mercadopago.SDK import Sdk


class CardToken(Sdk):
    def __init__(self, Sdk):
        self.Sdk = Sdk

    #TODO TESTADO OK!!
    def find_by_id(self, 
                   id,
                   requestOptions):
        if type(id) is not str:
            raise Exception('ID must be a String')     
        if requestOptions !=None and type(requestOptions) is not RequestOptions:
            raise Exception('Param requestOptions must be a RequestOptions Object')   

        http_client = HttpClient(self.Sdk)
        return http_client.get(uri='/v1/card_tokens/' + str(id), requestOptions=requestOptions)
