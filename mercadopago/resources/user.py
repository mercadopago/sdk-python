from mercadopago.core.mp_base import MPBase

class User(MPBase):
    def __init__(self, request_options):
        super(User, self).__init__(request_options)

    def find(self, request_options=None):
        return self._get(uri="/users/me", request_options=request_options)    
