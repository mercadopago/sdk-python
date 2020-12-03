from mercadopago.core import MPBase

class OAuth(MPBase):

    """
    This class will allow you to authorize your application to make request on others behalf.
    
    This is necessary to work with the Marketplace integration.
    
    [Click here for more infos](https://www.mercadopago.com.br/developers/en/guides/online-payments/marketplace/checkout-pro/create-marketplace)
    """
    
    def __init__(self, request_options, http_client):
        super(OAuth, self).__init__(request_options, http_client)

    def create(self, o_auth_object, request_options=None):
        if type(o_auth_object) is not dict:
            raise ValueError('Param o_auth_object must be a Dictionary')

        return self._post(uri="/oauth/token", data=o_auth_object, request_options=request_options)
