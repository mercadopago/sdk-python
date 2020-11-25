from mercadopago.core.mp_base import MPBase

class MerchantOrder(MPBase):
    def __init__(self, request_options):
        super(MerchantOrder, self).__init__(request_options)
     
    def find_by_id(self, id, request_options=None):  
        return self._get(uri="/merchant_orders/" + str(id), request_options=request_options)

    def update(self, id, request_options=None):
        return self._put(uri="/merchant_orders/" + str(id), request_options=request_options)

    def save(self, request_options=None):
        return self._post(uri="/merchant_orders", request_options=request_options)
