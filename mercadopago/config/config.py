import platform

class Config(object):

    """
    General infos of your SDK
    """
    
    def __init__(self):
        self.__version = "2.0.0" 
        self.__USER_AGENT = "MercadoPago Python SDK v" + self.__version
        self.__PRODUCT_ID = "bc32bpftrpp001u8nhlg"
        self.__TRACKING_ID = "platform:" + platform.python_version() + ",type:SDK" + self.__version + ",so;"

    __API_BASE_URL = "https://api.mercadopago.com"
    __MIME_JSON = "application/json"
    __MIME_FORM = "application/x-www-form-urlencoded"

    @property
    def version(self):
        return self.__version

    @property
    def userAgent(self):
        return self.__USER_AGENT

    @property
    def productId(self):
        return self.__PRODUCT_ID

    @property
    def trackingId(self):
        return self.__TRACKING_ID   

    @property
    def apiBaseUrl(self):
        return self.__API_BASE_URL

    @property
    def mimeJson(self):
        return self.__MIME_JSON

    @property
    def mimeForm(self):
        return self.__MIME_FORM
       