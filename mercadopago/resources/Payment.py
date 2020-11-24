from mercadopago.http.httpClient import HttpClient
#from .resources.refund import Refund
from mercadopago.core.RequestOptions import RequestOptions
from mercadopago.SDK import Sdk

#TODO DATASTRUCTURES
#TODO EXCEPETIONS
#TODO PROCESSO METHOD BULK | MPBASE

class Payment(Sdk):
    def __init__(self, Sdk):
        self.Sdk = Sdk

#TODO EXEMPLO DE CONSTRUÇÃO
#SDK.Payment.save({
#    'atributo': 'valor',
#    'atributo': 'valor',
#})

    #TODO @GET(path="/v1/payments/search")
    def search(self, 
               filters, 
               requestOptions=None):
        if type(filters) is not dict:
            raise Exception('Filters must be a Dictionary')
        if requestOptions !=None and type(requestOptions) is not RequestOptions:
            raise Exception('Param requestOptions must be a RequestOptions Object')
        
        http_client = HttpClient(self.Sdk)
        return http_client.get("/v1/payments/search", filters, requestOptions)

    def findById(self, 
                 id):
        if type(id) is not str:
            raise Exception('ID must be a String') 
               
        #return

    #TODO @GET(path="/v1/payments/{id}")    
    def findById(self, 
                 id, 
                 useCache, 
                 requestOptions):
        if type(id) is not str:
            raise Exception('ID must be a String')     
        if type(requestOptions) is not RequestOptions:
            raise Exception('Param requestOptions must be a RequestOptions Object')    
        
        #return self, useCache, useCache, requestOptions, id

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
            refund.setPaymentId == id
            refund.setAmount(amount)
            refund.save(requestOptions)
            self.lastApiResponse = refund.getLastApiResponse()

        #TODO VERIFICAR ESSA CONSTRUÇÃO
        #if id is None:
        #    payment = Payment.findById(self, id, requestOptions, withoutCache=False)
        #    self.status = payment.getStatus(self)
        #    self.statusDetail = payment.getStatusDetail(self)
        #    self.refunds = payment.getRefunds(self)
        #    self.transactionAmountRefunded = payment.getTransactionAmountRefunded(self)

        return self        