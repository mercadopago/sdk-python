from mercadopago.core.mp_base import MPBase

class Customer(MPBase):
    def __init__(self, request_options):
        super(Customer, self).__init__(request_options)

    def search(self, filters, request_options=None):
        if type(filters) is not dict:
            raise Exception("Param filters must be a Dictionary")

        return self._get(uri="/v1/customers/search", filters=filters, request_options=request_options)

    def find_by_id(self, id, request_options=None):
        return self._get(uri="/v1/customers/" + str(id), request_options=request_options)
        
    def save(self, request_options=None):
        return self._post(uri="/v1/customers",  request_options=request_options)

    def update(self, id, request_options=None):
        return self._put(uri="/v1/customers/" + str(id), request_options=request_options)

    def delete(self, id, request_options=None):
        return self._delete(uri="/v1/customers/" + str(id), request_options=request_options)    
