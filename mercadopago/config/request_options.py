class RequestOptions(object):

    """
    This object hold all configurations that will be used in ur REST call.

    All here u can customize as well add params in the requisition header (custom_headers)
    """
    
    def __init__(self, 
                 access_token=None, 
                 connection_timeout=60.0, 
                 custom_headers=None,
                 max_retries=3):
        """Initialize

        Args:
            access_token (str, optional): [description]. Defaults to None.
            connection_timeout (float, optional): [description]. Defaults to 60.0.
            custom_headers (dict, optional): [description]. Defaults to None.
            max_retries (int, optional): [description]. Defaults to 3.

        Raises:
            Exception: Param access_token must be a String
            Exception: Param connection_timeout must be a Float
            Exception: Param custom_headers must be a Dictionary
            Exception: Param max_retries must be an Integer
        """
        if access_token is not None and type(access_token) is not str:
            raise Exception('Param access_token must be a String')
        if connection_timeout is not None and type(connection_timeout) is not float:
            raise Exception('Param connection_timeout must be a Float')
        if custom_headers is not None and type(custom_headers) is not dict:
            raise Exception('Param custom_headers must be a Dictionary')  
        if max_retries is not None and type(max_retries) is not int:
            raise Exception('Param max_retries must be an Integer')      

        from mercadopago.config import Config

        self.access_token = access_token
        self.connection_timeout = connection_timeout
        self.custom_headers = custom_headers
        self.max_retries = max_retries
        self.config = Config()

    def get_headers(self):
        headers = {'Authorization': 'Bearer ' + self.access_token,
                'x-product-id': self.config.PRODUCT_ID, 
                'x-tracking-id': self.config.TRACKING_ID, 
                'User-Agent':self.config.USER_AGENT,
                'Accept':self.config.MIME_JSON}

        if self.custom_headers is not None:
            headers.update(self.custom_headers)

        return headers

