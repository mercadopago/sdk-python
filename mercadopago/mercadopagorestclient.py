from .mpinvalidcredentials import MPInvalidCredentials
from .restclient import RestClient

class MercadoPagoRestClient(object):
    __access_data = None
    __ll_access_token = None
    __client_id = None
    __client_secret = None
    __rest_client = None

    def __init__(self, client_id, client_secret, access_token, version):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__ll_access_token = access_token
        self.__rest_client = RestClient(version)

    def get_access_token(self):
        if not self.__ll_access_token is None:
            return self.__ll_access_token

        app_client_values = {
                           "client_id": self.__client_id,
                           "client_secret": self.__client_secret,
                           "grant_type": "client_credentials"
                           }

        access_data = self.__rest_client.post("/oauth/token", None, app_client_values, RestClient.MIME_FORM)

        if access_data["status"] == 200:
            self.__access_data = access_data["response"]
            return  self.__access_data["access_token"]
        else:
            raise MPInvalidCredentials(str(access_data))
    
    def get_rest_client(self):
        return self.__rest_client