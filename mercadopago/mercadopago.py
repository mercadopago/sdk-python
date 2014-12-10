from json.encoder import JSONEncoder
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl

"""
MercadoPago Integration Library
Access MercadoPago for payments integration

@author hcasatti

"""

class MPSSLAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1)

class MPException(Exception):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value

class MPInvalidCredentials(MPException):
    pass


class MP(object):
    version = "0.3.0"
    __access_data = None
    __sandbox = False

    def __init__(self, client_id, client_secret):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__rest_client = self.__RestClient(self)

    def sandbox_mode(self, enable=None):
        if not enable is None:
            self.__sandbox = enable == True

        return self.__sandbox

    def get_access_token(self):
        app_client_values = {
                           "client_id": self.__client_id,
                           "client_secret": self.__client_secret,
                           "grant_type": "client_credentials"
                           }

        access_data = self.__rest_client.post("/oauth/token", None, app_client_values, self.__RestClient.MIME_FORM)

        if access_data["status"] == 200:
            self.__access_data = access_data["response"]
            return  self.__access_data["access_token"]
        else:
            raise MPInvalidCredentials(str(access_data))

    """
    Get information for specific payment
    @param id
    @return json

    """
    def get_payment(self, id):
        access_token = self.get_access_token()

        uri_prefix = "/sandbox" if self.__sandbox else ""

        payment_info = self.__rest_client.get(uri_prefix+"/collections/notifications/"+id+"?access_token="+access_token)
        return payment_info

    def get_payment_info(self, id):
        return self.get_payment(id)

    """
    Get information for specific authorized payment
    @param id
    @return json

    """    
    def get_authorized_payment(self, id):
        try:
            access_token = self.get_access_token()
        except Exception,e:
            raise e
        
        authorized_payment_info = self.__rest_client.get("/authorized_payments/"+id+"?access_token="+access_token)
        return authorized_payment_info

    """
    Refund accredited payment
    @param id
    @return json

    """
    def refund_payment(self, id):
        access_token = self.get_access_token()

        refund_status = {"status":"refunded"}

        response = self.__rest_client.put("/collections/"+id+"?access_token="+access_token, refund_status)
        return response

    """
    Cancel pending payment
    @param id
    @return json

    """
    def cancel_payment(self, id):
        access_token = self.get_access_token()

        cancel_status = {"status":"cancelled"}

        response = self.__rest_client.put("/collections/"+id+"?access_token="+access_token, cancel_status)
        return response

    """
    Cancel preapproval payment
    @param id
    @return json

    """    
    def cancel_preapproval_payment(self, id):
        try:
            access_token = self.get_access_token()
        except Exception,e:
            raise e

        cancel_status = {"status":"cancelled"}
        
        response = self.__rest_client.put("/preapproval/"+id+"?access_token="+access_token, cancel_status)
        return response
    
    """
    Search payments according to filters, with pagination
    @param filters
    @param offset
    @param limit
    @return json

    """
    def search_payment(self, filters, offset=0, limit=0):
        access_token = self.get_access_token()

        filters["access_token"] = access_token
        filters["offset"] = offset
        filters["limit"] = limit

        uri_prefix = "/sandbox" if self.__sandbox else ""

        payment_result = self.__rest_client.get(uri_prefix+"/collections/search", filters)
        return payment_result

    """
    Create a checkout preference
    @param preference
    @return json

    """
    def create_preference(self, preference):
        access_token = self.get_access_token()

        preference_result = self.__rest_client.post("/checkout/preferences?access_token="+access_token, preference)
        return preference_result

    """
    Update a checkout preference
    @param id
    @param preference
    @return json

    """
    def update_preference(self, id, preference):
        access_token = self.get_access_token()

        preference_result = self.__rest_client.put("/checkout/preferences/"+id+"?access_token="+access_token, preference)
        return preference_result

    """
    Update a checkout preference
    @param id
    @param preference
    @return json

    """
    def get_preference(self, id):
        access_token = self.get_access_token()

        preference_result = self.__rest_client.get("/checkout/preferences/"+id+"?access_token="+access_token)
        return preference_result
    
    """
    Create a preapproval payment
    @param preapproval_payment
    @return json

    """
    def create_preapproval_payment(self, preapproval_payment):
        try:
            access_token = self.get_access_token()
        except Exception,e:
            raise e

        preapproval_payment_result = self.__rest_client.post("/preapproval?access_token="+access_token, preapproval_payment)
        return preapproval_payment_result
    
    """
    Get a preapproval payment
    @param id
    @param preference
    @return json

    """
    def get_preapproval_payment(self, id):
        try:
            access_token = self.get_access_token()
        except Exception,e:
            raise e
        
        preapproval_payment_result = self.__rest_client.get("/preapproval/"+id+"?access_token="+access_token)
        return preapproval_payment_result
    
    """
    Update a preapproval payment
    @param id
    @param preference
    @return json

    """
    def update_preapproval_payment(self, id, preapproval_payment):
        try:
            access_token = self.get_access_token()
        except Exception,e:
            raise e
        
        preapproval_payment_result = self.__rest_client.put("/preapproval/"+id+"?access_token="+access_token, preapproval_payment)
        return preapproval_payment_result
    
    """
    Generic resource get
    @param uri
    @param authenticate = true
    @return json

    """
    def get(self, uri, params=None, authenticate=True):
        if params is None:
            params = {}

        if authenticate:
            try:
                access_token = self.get_access_token()
                params["access_token"] = access_token
            except Exception,e:
                raise e

        result = self.__rest_client.get(uri, params)
        return result
    
    """
    Generic resource post
    @param uri
    @param data
    @return json

    """
    def post(self, uri, data, params=None):
        if params is None:
            params = {}

        try:
            access_token = self.get_access_token()
            params["access_token"] = access_token
        except Exception,e:
            raise e

        result = self.__rest_client.post(uri, data, params)
        return result
    
    """
    Generic resource put
    @param uri
    @param data
    @return json

    """
    def put(self, uri, data, params=None):
        if params is None:
            params = {}

        try:
            access_token = self.get_access_token()
            params["access_token"] = access_token
        except Exception,e:
            raise e

        result = self.__rest_client.put(uri, data, params)
        return result
    
    ##################################################################################
    class __RestClient(object):
        __API_BASE_URL = "https://api.mercadolibre.com"
        MIME_JSON = "application/json"
        MIME_FORM = "application/x-www-form-urlencoded"

        def __init__(self, outer):
            self.__outer = outer
            self.USER_AGENT = "MercadoPago Python SDK v"+self.__outer.version

        def get(self, uri, params=None):
            s = requests.Session()
            s.mount(self.__API_BASE_URL, MPSSLAdapter())
            api_result = s.get(self.__API_BASE_URL+uri, params=params, headers={'User-Agent':self.USER_AGENT, 'Accept':self.MIME_JSON})

            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

            return response

        def post(self, uri, data=None, params=None, content_type=MIME_JSON):
            if data is not None and content_type == self.MIME_JSON:
                data = JSONEncoder().encode(data)

            s = requests.Session()
            s.mount(self.__API_BASE_URL, MPSSLAdapter())
            api_result = s.post(self.__API_BASE_URL+uri, params=params, data=data, headers={'User-Agent':self.USER_AGENT, 'Content-type':content_type, 'Accept':self.MIME_JSON})

            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

            return response

        def put(self, uri, data=None, params=None, content_type=MIME_JSON):
            if data is not None and content_type == self.MIME_JSON:
                data = JSONEncoder().encode(data)

            s = requests.Session()
            s.mount(self.__API_BASE_URL, MPSSLAdapter())
            api_result = s.put(self.__API_BASE_URL+uri, params=params, data=data, headers={'User-Agent':self.USER_AGENT, 'Content-type':content_type, 'Accept':self.MIME_JSON})

            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

            return response
