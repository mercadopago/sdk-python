from mercadopago.core.mp_base import MPBase

class IdentificationType(MPBase):
    def __init__(self, request_options):
        super(IdentificationType, self).__init__(request_options)

    def find_all(self, request_options=None):
        return self._get(uri="/v1/identification_types", request_options=request_options)
            