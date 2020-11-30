class RequestOptions(object):

    """
    gdfbdgh
    """
    
    def __init__(self, 
                 access_token=None, 
                 connection_timeout=60.0, 
                 custom_headers=None,
                 max_retries=3):
        if access_token is not None and type(access_token) is not str:
            raise Exception('Param access_token must be a String')
        if connection_timeout is not None and type(connection_timeout) is not float:
            raise Exception('Param connection_timeout must be a Float')
        if custom_headers is not None and type(custom_headers) is not dict:
            raise Exception('Param custom_headers must be a Dictionary')  
        if max_retries is not None and type(max_retries) is not int:
            raise Exception('Param max_retries must be an Int')      

        from mercadopago import Config

        self.access_token = access_token
        self.connection_timeout = connection_timeout
        self.custom_headers = custom_headers
        self.max_retries = max_retries
        self.config = Config()

    def default_headers(self):
        return {'Authorization': 'Bearer ' + self.access_token,
                'x-product-id': self.config.PRODUCT_ID, 
                'x-tracking-id': self.config.TRACKING_ID, 
                'User-Agent':self.config.USER_AGENT,
                'Accept':self.config.MIME_JSON}

