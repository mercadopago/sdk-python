from mercadopago.core import MPBase

class IdentificationType(MPBase):

    """
    Access to Identification Types
    """
    
    def __init__(self, request_options, http_client):
        super(IdentificationType, self).__init__(request_options, http_client)

    def find_all(self, request_options=None):
        return self._get(uri="/v1/identification_types", request_options=request_options)
            