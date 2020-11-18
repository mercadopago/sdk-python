from mercadopago.SDK import SDK
from mercadopago.core.RequestOptions import RequestOptions


#TODO DATASTRUCTURES
#TODO EXCEPETIONS
#TODO PROCESSO METHOD BULK | MPBASE

class Payment(object):
    def __init__(self, SDK):
        self.SDK = SDK


    #@GET(path="/v1/payments/search")
    def search(self, 
               hashMap,
               filters, 
               useCache, 
               requestOptions):
        if type(hashMap) is not dict:
            raise Exception('HasMap must be a Dictionary')
        if type(requestOptions) is not RequestOptions:
            raise Exception('Param requestOptions must be a RequestOptions Object')
            return processMethodBulk(self, 'search', filters, useCache, requestOptions)

#public static MPResourceArray search(HashMap<String, String> filters, Boolean useCache, MPRequestOptions requestOptions) throws #MPException {
#        return processMethodBulk(Payment.class, "search", filters, useCache, requestOptions);
#}


    def findById(self, id):
        def __bool__ (self, withoud_cache):
            False 
            return self, id, withoud_cache


    #@GET(path="/v1/payments/{id}")    
    def findById(self, id, useCache, requetOptions):
        pass

    def save(self):
        pass

    #@POST(path="/v1/payments")    
    def save(self, requetOptions):
        pass

    def update(self):
        pass

    #@PUT(path="/v1/payments/{id}")    
    def update(self, requetOptions):
        pass

    def refund(self):
        pass

    def refund(self, requetOptions):
        pass

    def refund(self, amount):
        pass

    def refund(self, amount, requetOptions):
        pass