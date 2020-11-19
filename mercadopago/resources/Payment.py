from mercadopago.http.http_client import HttpClient
from mercadopago.resources.refund import Refund
from mercadopago.core.requestOptions import RequestOptions
from mercadopago.SDK import SDK

#TODO DATASTRUCTURES
#TODO EXCEPETIONS
#TODO PROCESSO METHOD BULK | MPBASE

class Payment(MPBase):
    def __init__(self, SDK):
        self.SDK = SDK

#TODO EXEMPLO DE CONSTRUÇÃO
#SDK.Payment.save({
#    'atributo': 'valor',
#    'atributo': 'valor',
#})

    #TODO @GET(path="/v1/payments/search")
    def search(self, 
               search,
               filters, 
               useCache, 
               requestOptions):
        if type(search) is not dict:
            raise Exception('Search must be a Dictionary')
        if type(requestOptions) is not RequestOptions:
            raise Exception('Param requestOptions must be a RequestOptions Object')
        
        return self, search, filters, useCache, requestOptions


    def findById(self, 
                 id, 
                 withoutCache=False):
        if type(id) is not str:
            raise Exception('HasMap must be a String')

        return self, id, withoutCache

    def findById(self, 
                 id, 
                 useCache):
        if type(id) is not str:
            raise Exception('ID must be a String') 
               
        return self, id, useCache, RequestOptions.createDefault()

    #TODO @GET(path="/v1/payments/{id}")    
    def findById(self, 
                 id, 
                 useCache, 
                 requestOptions):
        if type(id) is not str:
            raise Exception('ID must be a String')     
        if type(requestOptions) is not RequestOptions:
            raise Exception('Param requestOptions must be a RequestOptions Object')    
        
        return self, useCache, useCache, requestOptions, id

    def save(self):        
        return self, RequestOptions.createDefault()

    #TODO @POST(path="/v1/payments")    
    def save(self, 
             requestOptions, 
             withoutCache=False):
        if requestOptions is None:
            requestOptions = requestOptions.createDefault
            requestOptions.addTrackingHeaders(requestOptions)
    #TODO addTrackingHeaders
        return self, requestOptions, withoutCache

    def update(self):
        return self, RequestOptions.createDefault()

    #TODO @PUT(path="/v1/payments/{id}")    
    def update(self, 
               requestOptions, 
               withoutCache=False):
        return self, requestOptions, withoutCache

    def refund(self, 
               r):
        return self, r is None, RequestOptions.createDefault() 

    def refund(self, 
               r, 
               requestOptions):
        return self, r is None, requestOptions

    def refund(self, 
               amount):
        if type(amount) is not float:
            raise Exception('Amount must be a Float')  

        return self, amount, RequestOptions.createDefault()

    def refund(self, 
               amount, 
               requestOptions):

        def __init__(refund):
            Refund.setPaymentId == id
            Refund.setAmount(amount)
            Refund.save(requestOptions)
            self.lastApiResponse = Refund.getLastApiResponse()

        #TODO VERIFICAR ESSA CONSTRUÇÃO
        #if id is None:
        #    payment = Payment.findById(self, id, requestOptions, withoutCache=False)
        #    self.status = payment.getStatus(self)
        #    self.statusDetail = payment.getStatusDetail(self)
        #    self.refunds = payment.getRefunds(self)
        #    self.transactionAmountRefunded = payment.getTransactionAmountRefunded(self)

        return self        
