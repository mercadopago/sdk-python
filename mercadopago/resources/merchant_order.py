from mercadopago.core.mp_base import MPBase

class MerchantOrder(MPBase):
    def __init__(self, request_options):
        super(MerchantOrder, self).__init__(request_options)
     
    def find_by_id(self, id, request_options=None):  
        return self._get(uri="/merchant_orders/" + str(id), request_options=request_options)
