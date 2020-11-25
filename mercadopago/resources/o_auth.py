from mercadopago.core.mp_base import MPBase

class OAuth(MPBase):
    def __init__(self, request_options):
        super(OAuth, self).__init__(request_options)

    def save(self, o_auth, request_options=None):
        return self._post(uri="/oauth/token", request_options=request_options)
