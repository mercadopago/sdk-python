from mercadopago.core import MPBase

class AdvancedPayment(MPBase):

    """
    Access to Advanced Payments
    """
    
    def __init__(self, request_options, http_client):
        super(AdvancedPayment, self).__init__(request_options, http_client)

    def find_by_id(self, id, request_options=None):
        return self._get(uri="/v1/advanced_payments/" + str(id), request_options=request_options) 

    def save(self, advanced_payment_object, request_options=None):
        if type(advanced_payment_object) is not dict:
            raise ValueError("Param advanced_payment_object must be a Dictionary")

        return self._post(uri="/v1/advanced_payments", data=advanced_payment_object, request_options=request_options)

    def capture(self, id, request_options=None):
        capture_object = {"capture": True}
        return self._put(uri="/v1/advanced_payments/" + str(id), data=capture_object, request_options=request_options) 

    def update(self, id, advanced_payment_object, request_options=None):
        if type(advanced_payment_object) is not dict:
            raise ValueError("Param advanced_payment_object must be a Dictionary")

        return self._put(uri="/v1/advanced_payments/" + str(id), data=advanced_payment_object, request_options=request_options) 

    def cancel(self, id, request_options=None):
        cancel_object = {"status": "cancelled"}
        return self._put(uri="/v1/advanced_payments/" + str(id), data=cancel_object, request_options=request_options) 
