import platform

class Config(object):

    """
    General infos of your SDK
    """
    
    def __init__(self):
        #TODO VERIFICAR COM DANILO O NÚMERO CORRETO DESTA VERSÃO
        version = "2.0.0" 
        self.USER_AGENT = "MercadoPago Python SDK v" + version
        self.PRODUCT_ID = "bc32bpftrpp001u8nhlg"
        self.TRACKING_ID = "platform:" + platform.python_version() + ",type:SDK" + version + ",so;"

    API_BASE_URL = "https://api.mercadopago.com"
    MIME_JSON = "application/json"
    MIME_FORM = "application/x-www-form-urlencoded"

       