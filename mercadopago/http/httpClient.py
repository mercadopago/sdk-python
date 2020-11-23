from ..config import Config
from ..sdk import Sdk
from json.encoder import JSONEncoder

import requests

#TODO VERIFICAR SE ISSO AINDA FUNCIONA PARA O REFACTOR


class HttpClient():

    def __init__(self, Sdk):
        self.Sdk = Sdk
        self.Config = Config()


    def get_session(self):
        """Creates and returns a ready-to-use requests.
        Session, with all thecustomizations made to access MP

        """
        
        session = requests.Session()
        #session.mount(self.Config.API_BASE_URL,
        #              self.get_mercadopago_transport_adapter())
        return session

    def get(self, uri, params=None, requestOptions=None):
        s = self.get_session()
        accessToken = requestOptions is None and self.Sdk.accessToken or requestOptions.accessToken
        print(accessToken)

        api_result = s.get(self.Config.API_BASE_URL+uri, 
                            params=params, headers={
                                                    'accessToken': accessToken,
                                                    'x-product-id': self.Config.PRODUCT_ID, 
                                                    'x-tracking-id': self.Config.TRACKING_ID, 
                                                    'User-Agent':self.Config.USER_AGENT,
                                                    'Accept':self.Config.MIME_JSON})

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response

    def post(self, uri, data=None, params=None, content_type=None):
        if data is not None and content_type == self.Config.MIME_JSON:
            data = JSONEncoder().encode(data)

        s = self.get_session()
        api_result = s.post(self.Config.API_BASE_URL+uri, 
                            params=params, data=data, 
                            headers={
                                     'accessToken': self.Sdk.getAccessToken(),
                                     'x-product-id': self.Config.PRODUCT_ID, 
                                     'x-tracking-id': self.Config.TRACKING_ID, 
                                     'User-Agent':self.Config.USER_AGENT, 
                                     'Content-type':content_type, 
                                     'Accept':self.Config.MIME_JSON})

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response

    def put(self, uri, data=None, params=None, content_type=None):
        if data is not None and content_type == self.Config.MIME_JSON:
            data = JSONEncoder().encode(data)

        s = self.get_session()
        api_result = s.put(self.Config.API_BASE_URL+uri, 
                           params=params, data=data, 
                           headers={
                                    'accessToken': self.Sdk.getAccessToken(),    
                                    'x-product-id': self.Config.PRODUCT_ID, 
                                    'x-tracking-id': self.Config.TRACKING_ID, 
                                    'User-Agent':self.Config.USER_AGENT, 
                                    'Content-type':content_type, 
                                    'Accept':self.Config.MIME_JSON})

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response

    def delete(self, uri, params=None):
        s = self.get_session()
        api_result = s.delete(self.Config.API_BASE_URL+uri, 
                              params=params, 
                              headers={
                                       'accessToken': self.Sdk.getAccessToken(), 
                                       'x-product-id': self.Config.PRODUCT_ID, 
                                       'x-tracking-id': self.Config.TRACKING_ID, 
                                       'User-Agent':self.Config.USER_AGENT, 
                                       'Accept':self.Config.MIME_JSON})

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response
