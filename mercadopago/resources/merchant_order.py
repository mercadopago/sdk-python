from mercadopago.core.mp_base import MPBase

class MerchantOrder(MPBase):
    def __init__(self, request_options):
        super(MerchantOrder, self).__init__(request_options)

    #TODO TESTADO OK!!       
    def find_by_id(self, id, request_options=None):
        if type(id) is not str:
            raise Exception('Param id must be a String')
        
        return self._get(uri='/merchant_orders/' + str(id), request_options=request_options)
