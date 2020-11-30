class RequestOptions(object):

    """
    This object hold all configurations that will be used in ur REST call.

    All here u can customize as well add params in the requisition header (custom_headers)
    """
    
    __access_token = None
    __connection_timeout = None
    __custom_headers = None
    __max_retries = None
    
    def __init__(self, 
                 access_token=None, 
                 connection_timeout=60.0, 
                 custom_headers=None,
                 max_retries=30):
        """Initialize

        Args:
            access_token (str, optional): [description]. Defaults to None.
            connection_timeout (float, optional): [description]. Defaults to 60.0.
            custom_headers (dict, optional): [description]. Defaults to None.
            max_retries (int, optional): [description]. Defaults to 3.

        Raises:
            ValueError: Param access_token must be a String
            ValueError: Param connection_timeout must be a Float
            ValueError: Param custom_headers must be a Dictionary
            ValueError: Param max_retries must be an Integer
        """
        from mercadopago.config import Config

        if access_token is not None:
            self.access_token = access_token
        if connection_timeout is not None:
            self.connection_timeout = connection_timeout
        if custom_headers is not None:
            self.custom_headers = custom_headers
        if max_retries is not None:
            self.max_retries = max_retries

        self.__config = Config()

    def get_headers(self):
        headers = {'Authorization': 'Bearer ' + self.__access_token,
                'x-product-id': self.__config.productId, 
                'x-tracking-id': self.__config.trackingId, 
                'User-Agent':self.__config.userAgent,
                'Accept':self.__config.mimeJson}

        if self.__custom_headers is not None:
            headers.update(self.__custom_headers)

        return headers

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        if type(value) is not str:
            raise ValueError('Param access_token must be a String')
        self.__access_token = value

    @property
    def connection_timeout(self):
        return self.__connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, value):
        if type(value) is not float:
            raise ValueError('Param connection_timeout must be a Float')
        self.__connection_timeout = value

    @property
    def custom_headers(self):
        return self.__custom_headers

    @custom_headers.setter
    def custom_headers(self, value):
        if type(value) is not dict:
            raise ValueError('Param custom_headers must be a Dictionary')
        self.__custom_headers = value

    @property
    def max_retries(self):
        return self.__max_retries

    @max_retries.setter
    def max_retries(self, value):
        if type(value) is not int:
            raise ValueError('Param max_retries must be an Integer')
        self.__max_retries = value

