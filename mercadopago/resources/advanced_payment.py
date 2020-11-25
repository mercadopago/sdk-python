from mercadopago.core.mp_base import MPBase

class AdvancedPayment(MPBase):
    def __init__(self, request_options):
        super(AdvancedPayment, self).__init__(request_options)


    def find_by_id(self, id, request_options=None):
        return self._get(uri="/v1/advanced_payments/" + str(id), request_options=request_options) 
