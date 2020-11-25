from mercadopago.config import Config

class RequestOptions():

    def __init__(self, 
                 access_token=None, 
                 connection_timeout=None, 
                 custom_headers=None):
        
        if access_token is not None and type(access_token) is not str:
            raise Exception('Warning: access_token must be a String')
        if connection_timeout is not None and type(connection_timeout) is not int:
            raise Exception('Warning: connection_timeout must be a Integer')
        if custom_headers is not None and type(custom_headers) is not dict:
            raise Exception('Warning: custom_headers must be a Dictionary')        

        self.access_token = access_token
        self.connection_timeout = connection_timeout
        self.custom_headers = custom_headers
        self.config = Config()

    def default_headers(self):
        return {'Authorization': 'Bearer ' + self.access_token,
                'x-product-id': self.config.PRODUCT_ID, 
                'x-tracking-id': self.config.TRACKING_ID, 
                'User-Agent':self.config.USER_AGENT,
                'Accept':self.config.MIME_JSON}

