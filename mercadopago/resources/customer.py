from mercadopago.core import MPBase

class Customer(MPBase):

    """
    gdfbdgh
    """
    
    def __init__(self, request_options, http_client):
        super(Customer, self).__init__(request_options, http_client)

    def search(self, filters, request_options=None):
        return self._get(uri="/v1/customers/search", filters=filters, request_options=request_options)

    def find_by_id(self, id, request_options=None):
        return self._get(uri="/v1/customers/" + str(id), request_options=request_options)
        
    def save(self, customer_object, request_options=None):
        if type(customer_object) is not dict:
            raise Exception("Param customer_object must be a Dictionary")

        return self._post(uri="/v1/customers", data=customer_object, request_options=request_options)

    def update(self, id, customer_object, request_options=None):
        if type(customer_object) is not dict:
            raise Exception("Param customer_object must be a Dictionary")

        return self._put(uri="/v1/customers/" + str(id), data=customer_object, request_options=request_options)

    def delete(self, id, request_options=None):
        return self._delete(uri="/v1/customers/" + str(id), request_options=request_options)    