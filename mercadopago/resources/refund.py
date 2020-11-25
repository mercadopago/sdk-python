from mercadopago.core.mp_base import MPBase

class Refund(MPBase):
    def __init__(self, request_options):
        super(Refund, self).__init__(request_options)

    def find_all(self, payment_id, request_options=None):
        return self._get(uri="" + str(payment_id) + "/refunds", request_options=request_options)

    def save(self, payment_id, request_options=None):
        return self._post(uri="" + str(payment_id), request_options=request_options)
