"""
MercadoPago Integration Library
Access MercadoPago for payments integration

@author hcasatti
"""

from json.encoder import JSONEncoder
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

import platform
import ssl
import sys

class MPSSLAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block)

class MPException(Exception):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value

class MPInvalidCredentials(MPException):
    pass


class MP(object):
    version = "1.2.0"
    __access_data = None
    __ll_access_token = None
    __sandbox = False
    platform_id = None
    integrator_id = None
    corporation_id = None

    def __init__(self, *args):
        """
        Instantiate MP with credentials:
        mp = mercadopago.MP(client_id, client_secret)

        Instantiate MP with Long Live Access Token:
        mp = mercadopago.MP(ll_access_token)
        """
        if len(args) == 2:
            self.__client_id = args[0]
            self.__client_secret = args[1]
        elif len(args) == 1:
            self.__ll_access_token = args[0]
        else:
            raise MPInvalidCredentials(None)

        self.__rest_client = self.__RestClient(self)

    def sandbox_mode(self, enable=None):
        if not enable is None:
            self.__sandbox = enable == True

        return self.__sandbox

    def get_access_token(self):
        if not self.__ll_access_token is None:
            return self.__ll_access_token

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

    def set_platform_id(self, platform_id):
        self.platform_id = platform_id

    def set_integrator_id(self, integrator_id):
        self.integrator_id = integrator_id

    def set_corporation_id(self, corporation_id):
        self.corporation_id = corporation_id

    def get_payment(self, id):
        """
        Get information for specific payment

        @param id
        @return json
        """

        payment_info = self.__rest_client.get("/v1/payments/"+id)
        return payment_info

    def get_payment_info(self, id):
        return self.get_payment(id)

    def get_authorized_payment(self, id):
        """
        Get information for specific authorized payment

        @param id
        @return json
        """
        authorized_payment_info = self.__rest_client.get("/authorized_payments/"+id)
        return authorized_payment_info


    def refund_payment(self, id):
        """
        Refund accredited payment

        @param id
        @return json
        """

        refund_status = {}
        response = self.__rest_client.post("/v1/payments/"+id+"/refunds", refund_status)
        return response


    def cancel_payment(self, id):
        """
        Cancel pending payment

        @param id
        @return json
        """

        cancel_status = {"status":"cancelled"}
        response = self.__rest_client.put("/v1/payments/"+id, cancel_status)
        return response


    def cancel_preapproval_payment(self, id):
        """
        Cancel preapproval payment

        @param id
        @return json
        """

        cancel_status = {"status":"cancelled"}
        response = self.__rest_client.put("/preapproval/"+id, cancel_status)
        return response


    def search_payment(self, filters, offset=0, limit=0):
        """
        Search payments according to filters, with pagination

        @param filters
        @param offset
        @param limit
        @return json
        """

        filters["offset"] = offset
        filters["limit"] = limit

        payment_result = self.__rest_client.get("/v1/payments/search", filters)
        return payment_result

    def create_preference(self, preference):
        """
        Create a checkout preference

        @param preference
        @return json
        """

        preference_result = self.__rest_client.post("/checkout/preferences", preference)
        return preference_result


    def update_preference(self, id, preference):
        """
        Update a checkout preference

        @param id
        @param preference
        @return json
        """

        preference_result = self.__rest_client.put("/checkout/preferences/"+id, preference)
        return preference_result


    def get_preference(self, id):
        """
        Update a checkout preference

        @param id
        @param preference
        @return json
        """
        preference_result = self.__rest_client.get("/checkout/preferences/"+id)
        return preference_result


    def create_preapproval_payment(self, preapproval_payment):
        """
        Create a preapproval payment

        @param preapproval_payment
        @return json
        """
        preapproval_payment_result = self.__rest_client.post("/preapproval", preapproval_payment)
        return preapproval_payment_result

    def get_preapproval_payment(self, id):
        """
        Get a preapproval payment
        @param id
        @param preference
        @return json

        """
        preapproval_payment_result = self.__rest_client.get("/preapproval/"+id)
        return preapproval_payment_result

    def update_preapproval_payment(self, id, preapproval_payment):
        """
        Update a preapproval payment
        @param id
        @param preference
        @return json

        """
        preapproval_payment_result = self.__rest_client.put("/preapproval/"+id, preapproval_payment)
        return preapproval_payment_result

    def get(self, uri, params=None, authenticate=True):
        """
        Generic resource get
        @param uri
        @param authenticate = true
        @return json

        """
        if params is None:
            params = {}

        result = self.__rest_client.get(uri, params)
        return result

    def post(self, uri, data, params=None):
        """
        Generic resource post
        @param uri
        @param data
        @return json

        """
        if params is None:
            params = {}

        result = self.__rest_client.post(uri, data, params)
        return result

    def put(self, uri, data, params=None):
        """
        Generic resource put
        @param uri
        @param data
        @return json

        """
        if params is None:
            params = {}

        result = self.__rest_client.put(uri, data, params)
        return result

    def delete(self, uri, params=None):
        """
        Generic resource delete
        @param uri
        @return json

        """
        if params is None:
            params = {}

        result = self.__rest_client.delete(uri, params)
        return result

    ##################################################################################
    class __RestClient(object):
        __API_BASE_URL = "https://api.mercadopago.com"
        MIME_JSON = "application/json"
        MIME_FORM = "application/x-www-form-urlencoded"
        AUTH_HEADER = "Authorization"
        def __init__(self, outer):
            self.__outer = outer
            self.USER_AGENT = "MercadoPago Python SDK v"+self.__outer.version
            self.PRODUCT_ID = "bc32bpftrpp001u8nhlg"
            self.TRACKING_ID = "platform:"+str(sys.version_info.major)+"|"+platform.python_version()+",type:SDK"+self.__outer.version+",so;"

        def get_mercadopago_transport_adapter(self):
            """Creates and returns the transport adaptor for MP"""
            return MPSSLAdapter()

        def get_session(self):
            """Creates and returns a ready-to-use requests.Session, with all the
            customizations made to access MP
            """
            session = requests.Session()
            session.mount(self.__API_BASE_URL,
                          self.get_mercadopago_transport_adapter())
            return session

        def getAuthorizationHeader(self):
            return 'Bearer ' + self.__outer.get_access_token()

        def get(self, uri, params=None):
            s = self.get_session()
            api_result = s.get(self.__API_BASE_URL+uri, params=params, headers={'x-product-id': self.PRODUCT_ID, 'x-tracking-id': self.TRACKING_ID, 'User-Agent':self.USER_AGENT, 'Accept':self.MIME_JSON, self.AUTH_HEADER: self.getAuthorizationHeader()})

            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

            return response

        def post(self, uri, data=None, params=None, content_type=MIME_JSON):
            if data is not None and content_type == self.MIME_JSON:
                data = JSONEncoder().encode(data)

            s = self.get_session()
            headers = {'x-product-id': self.PRODUCT_ID, 'x-tracking-id': self.TRACKING_ID, 'User-Agent':self.USER_AGENT, 'Content-type':content_type, 'Accept':self.MIME_JSON, 'x-platform-id':self.__outer.platform_id, 'x-integrator-id':self.__outer.integrator_id, 'x-corporation-id':self.__outer.corporation_id}
            if uri.find('/oauth/token') == -1:
                headers[self.AUTH_HEADER] = self.getAuthorizationHeader()
            api_result = s.post(self.__API_BASE_URL+uri, params=params, data=data, headers=headers)

            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

            return response

        def put(self, uri, data=None, params=None, content_type=MIME_JSON):
            if data is not None and content_type == self.MIME_JSON:
                data = JSONEncoder().encode(data)

            s = self.get_session()
            api_result = s.put(self.__API_BASE_URL+uri, params=params, data=data, headers={'x-product-id': self.PRODUCT_ID, 'x-tracking-id': self.TRACKING_ID, 'User-Agent':self.USER_AGENT, 'Content-type':content_type, 'Accept':self.MIME_JSON, self.AUTH_HEADER: self.getAuthorizationHeader()})

            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

            return response

        def delete(self, uri, params=None):
            s = self.get_session()
            api_result = s.delete(self.__API_BASE_URL+uri, params=params, headers={'x-product-id': self.PRODUCT_ID, 'x-tracking-id': self.TRACKING_ID, 'User-Agent':self.USER_AGENT, 'Accept':self.MIME_JSON, self.AUTH_HEADER: self.getAuthorizationHeader()})

            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

            return response
