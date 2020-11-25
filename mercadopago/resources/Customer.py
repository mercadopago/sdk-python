from mercadopago.core.mp_base import MPBase

class Customer(MPBase):
    def __init__(self, request_options):
        super(Customer, self).__init__(request_options)

    #TODO TESTADO OK!!
    def search(self, filters, request_options=None):
        if type(filters) is not dict:
            raise Exception('Param filters must be a Dictionary')

        return self._get(uri='/v1/customers/search', filters=filters, request_options=request_options)
