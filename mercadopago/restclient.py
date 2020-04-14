from json.encoder import JSONEncoder
import requests

from .mpssladapter import MPSSLAdapter

import platform

class RestClient(object):
    __API_BASE_URL = "https://api.mercadopago.com"
    MIME_JSON = "application/json"
    MIME_FORM = "application/x-www-form-urlencoded"

    def __init__(self, version):
        self.USER_AGENT = "MercadoPago Python SDK v" + version
        self.PRODUCT_ID = "bc32bpftrpp001u8nhlg"
        self.TRACKING_ID = "platform:" + platform.python_version() + ",type:SDK" + version + ",so;"

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

    def get(self, uri, params=None):
        s = self.get_session()
        api_result = s.get(self.__API_BASE_URL+uri, params=params, headers={'x-product-id': self.PRODUCT_ID, 'x-tracking-id': self.TRACKING_ID, 'User-Agent':self.USER_AGENT, 'Accept':self.MIME_JSON})

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response

    def post(self, uri, data=None, params=None, content_type=MIME_JSON):
        if data is not None and content_type == self.MIME_JSON:
            data = JSONEncoder().encode(data)

        s = self.get_session()
        api_result = s.post(self.__API_BASE_URL+uri, params=params, data=data, headers={'x-product-id': self.PRODUCT_ID, 'x-tracking-id': self.TRACKING_ID, 'User-Agent':self.USER_AGENT, 'Content-type':content_type, 'Accept':self.MIME_JSON})

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response

    def put(self, uri, data=None, params=None, content_type=MIME_JSON):
        if data is not None and content_type == self.MIME_JSON:
            data = JSONEncoder().encode(data)

        s = self.get_session()
        api_result = s.put(self.__API_BASE_URL+uri, params=params, data=data, headers={'x-product-id': self.PRODUCT_ID, 'x-tracking-id': self.TRACKING_ID, 'User-Agent':self.USER_AGENT, 'Content-type':content_type, 'Accept':self.MIME_JSON})

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response

    def delete(self, uri, params=None):
        s = self.get_session()
        api_result = s.delete(self.__API_BASE_URL+uri, params=params, headers={'x-product-id': self.PRODUCT_ID, 'x-tracking-id': self.TRACKING_ID, 'User-Agent':self.USER_AGENT, 'Accept':self.MIME_JSON})

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response

