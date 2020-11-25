from mercadopago.core.mp_base import MPBase

class Preference(MPBase):
    def __init__(self, request_options):
        super(Preference, self).__init__(request_options)
    
    def find_by_id(self, id, request_options=None):
        return self._get(uri="/checkout/preferences/" + str(id), request_options=request_options)
