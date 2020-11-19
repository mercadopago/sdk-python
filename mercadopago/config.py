from json.encoder import JSONEncoder
from mercadopago.SDK import SDK

import platform


class Config(object):

    def __init__(self, SDK):
        self.SDK = SDK

    #TODO RETRY STRATEGY
    MAX_DELAY = 2
    INITIAL_DELAY = 0.5
    MAX_RETRY_AFTER = 60

    __API_BASE_URL = "https://api.mercadopago.com"
    MIME_JSON = "application/json"
    MIME_FORM = "application/x-www-form-urlencoded"

    def configuration(self):
        #TODO VERIFICAR COM DANILO O NÚMERO CORRETO DESTA VERSÃO
        version = "2.0.0" 
        self.USER_AGENT = "MercadoPago Python SDK v" + version
        self.PRODUCT_ID = "bc32bpftrpp001u8nhlg"
        self.TRACKING_ID = "platform:" + platform.python_version() + ",type:SDK" + version + ",so;"

        def corporationId(self):
            pass

        def integratorId(self):
            pass

        def platformId(self):
            pass

        #TODO HTTP CLIENT
        #TODO SERIALIZER



       