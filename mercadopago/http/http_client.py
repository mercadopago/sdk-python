from mercadopago.config import Config
from mercadopago.SDK import SDK
from json.encoder import JSONEncoder

import http.client

#TODO VERIFICAR SE ISSO AINDA FUNCIONA PARA O REFACTOR


class HttpClient(object):

    def __init__(self, SDK):
        self.SDK = SDK
        self.Config = Config()


    def get_session(self):
        """Creates and returns a ready-to-use requests.
        Session, with all thecustomizations made to access MP

        """
        session = http.client.HTTPConnection.request()
        session.mount(self.Config.__API_BASE_URL,
                        self.get_mercadopago_transport_adapter())
        return session

    def get(self, uri, params=None):
        s = self.get_session()
        api_result = s.get(self.Config.__API_BASE_URL+uri, 
                            params=params, headers={
                                                    'accessToken': self.SDK.getAccessToken(),
                                                    'x-product-id': self.Config.PRODUCT_ID, 
                                                    'x-tracking-id': self.Config.TRACKING_ID, 
                                                    'User-Agent':self.Config.USER_AGENT,
                                                    'Accept':self.Config.MIME_JSON})

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response

    def post(self, uri, data=None, params=None, content_type=MIME_JSON):
        if data is not None and content_type == self.Config.MIME_JSON:
            data = JSONEncoder().encode(data)

        s = self.get_session()
        api_result = s.post(self.Config.__API_BASE_URL+uri, 
                            params=params, data=data, 
                            headers={
                                     'accessToken': self.SDK.getAccessToken(),
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

    def put(self, uri, data=None, params=None, content_type=MIME_JSON):
        if data is not None and content_type == self.Config.MIME_JSON:
            data = JSONEncoder().encode(data)

        s = self.get_session()
        api_result = s.put(self.Config.__API_BASE_URL+uri, 
                           params=params, data=data, 
                           headers={
                                    'accessToken': self.SDK.getAccessToken(),    
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
        api_result = s.delete(self.Config.__API_BASE_URL+uri, 
                              params=params, 
                              headers={
                                       'accessToken': self.SDK.getAccessToken(), 
                                       'x-product-id': self.Config.PRODUCT_ID, 
                                       'x-tracking-id': self.Config.TRACKING_ID, 
                                       'User-Agent':self.Config.USER_AGENT, 
                                       'Accept':self.Config.MIME_JSON})

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response
