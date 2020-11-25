from mercadopago.core.mp_base import MPBase

class Payment(MPBase):
    def __init__(self, request_options):
        super(Payment, self).__init__(request_options)

    def search(self, filters, request_options=None):
        return self._get(uri="/v1/payments/search", filters=filters, request_options=request_options)

    def find_by_id(self, id, request_options=None):
        return self._get(uri="/v1/payments/" + str(id), request_options=request_options)

    def save(self, payment_object, request_options=None):
        if type(payment_object) is not dict:
            raise Exception("Param payment_object must be a Dictionary")

        return self._post(uri="/v1/payments/", data=payment_object, request_options=request_options)

    def update(self, id, payment_object, request_options=None):
        if type(payment_object) is not dict:
            raise Exception("Param payment_object must be a Dictionary")

        return self._put(uri="/v1/payments/" + str(id), data=payment_object, request_options=request_options)
