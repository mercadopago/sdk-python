from mercadopago.core import MPBase

class User(MPBase):

    """
    Access to Users
    """
    
    def __init__(self, request_options, http_client):
        super(User, self).__init__(request_options, http_client)

    def find(self, request_options=None):
        return self._get(uri="/users/me", request_options=request_options)    
