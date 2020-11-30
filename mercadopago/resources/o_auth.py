from mercadopago.core import MPBase

class OAuth(MPBase):

    """
    gdfbdgh
    """
    
    def __init__(self, request_options, http_client):
        super(OAuth, self).__init__(request_options, http_client)

    def save(self, o_auth_object, request_options=None):
        if type(o_auth_object) is not dict:
            raise Exception('Param o_auth_object must be a Dictionary')

        return self._post(uri="/oauth/token", data=o_auth_object, request_options=request_options)
