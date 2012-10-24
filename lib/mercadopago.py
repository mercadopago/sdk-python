import json
import urllib
import os, sys
from json.encoder import JSONEncoder
sys.path.append(os.path.dirname(__file__)+"/lib")
from restful_lib import Connection

"""
MercadoPago Integration Library
Access MercadoPago for payments integration

@author hcasatti

"""
class MP:
    __access_data = None

    def __init__(self, client_id, client_secret):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__restClient = self.__RestClient()
        
    def __get_access_token(self):
        appClientValues = {
                           "client_id": self.__client_id,
                           "client_secret": self.__client_secret,
                           "grant_type": "client_credentials"
                           }

        access_data = self.__restClient.post("/oauth/token", self.__build_query(appClientValues), self.__RestClient.MIME_FORM) 
        
        if access_data['status'] == "200":
            self.__access_data = access_data["response"]
        else:
            self.__access_data = None
        
        if self.__access_data != None and "access_token" in self.__access_data:
            return  self.__access_data["access_token"]
        else:
            return None
        
    """
    Get information for specific payment
    @param id
    @return json
    """    
    def get_payment_info(self, id):
        accessToken = self.__get_access_token()
        
        paymentInfo = self.__restClient.get("/collections/notifications/"+id+"?access_token="+accessToken)
        return paymentInfo
    
    """
    Refund accredited payment
    @param id
    @return json
    """    
    def refund_payment(self, id):
        accessToken = self.__get_access_token()

        refund_status = {"status":"refunded"}
        
        response = self.__restClient.put("/collections/"+id+"?access_token="+accessToken, refund_status)
        return response
    
    """
    Cancel pending payment
    @param id
    @return json
    """    
    def cancel_payment(self, id):
        accessToken = self.__get_access_token()

        cancel_status = {"status":"cancelled"}
        
        response = self.__restClient.put("/collections/"+id+"?access_token="+accessToken, cancel_status)
        return response
    
    """
    Search payments according to filters, with pagination
    @param filters
    @param offset
    @param limit
    @return json
    """
    def search_payment(self, filters, offset=0, limit=0):
        accessToken = self.__get_access_token()

        filters["offset"] = offset
        filters["limit"] = limit
        
        filters = self.__build_query(filters)
        
        collectionResult = self.__restClient.get("/collections/search?"+filters+"&access_token="+accessToken)
        return collectionResult        
        
    """
    Create a checkout preference
    @param preference
    @return json
    """
    def create_preference(self, preference):
        accessToken = self.__get_access_token()

        preferenceResult = self.__restClient.post("/checkout/preferences?access_token="+accessToken, preference)
        return preferenceResult
    
    """
    Update a checkout preference
    @param id
    @param preference
    @return json
    """
    def update_preference(self, id, preference):
        accessToken = self.__get_access_token()
        
        preferenceResult = self.__restClient.put("/checkout/preferences/"+id+"?access_token="+accessToken, preference)
        return preferenceResult
    
    """
    Update a checkout preference
    @param id
    @param preference
    @return json
    """
    def get_preference(self, id):
        accessToken = self.__get_access_token()
        
        preferenceResult = self.__restClient.get("/checkout/preferences/"+id+"?access_token="+accessToken)
        return preferenceResult
    
    ##################################################################################
    def __build_query(self, params):
        elements = []
        
        for key,val in params.iteritems():
            if val == None:
                val = ""
                
            elements.append(key+"="+urllib.quote(str(val)))
        
        return "&".join(elements)
    
    class __RestClient:
        __API_BASE_URL = "https://api.mercadolibre.com"
        MIME_JSON = "application/json"
        MIME_FORM = "application/x-www-form-urlencoded"
        
        def __init__(self):
            self.__conn = Connection(self.__API_BASE_URL)
    
        def __exec(self, method, uri, data, contentType):

            if contentType == self.MIME_JSON:
                data = JSONEncoder().encode(data)
            else:
                data = str(data)
            
            apiResult = self.__conn.request(uri, method, body=data, headers={'Content-type':contentType, 'Accept':self.MIME_JSON})
            apiHttpCode = apiResult[u'headers']['status']
            
            response = {
                        "status": apiHttpCode,
                        "response": json.loads(apiResult[u'body'])
                        }
            
            return response
        
        def get(self, uri, contentType=MIME_JSON):
            return self.__exec("get", uri, None, contentType)
            
        def post(self, uri, data=None, contentType=MIME_JSON):
            return self.__exec("post", uri, data, contentType)
            
        def put(self, uri, data=None, contentType=MIME_JSON):
            return self.__exec("put", uri, data, contentType)
