from mercadopago.core import MPBase

class Refund(MPBase):

    """
    gdfbdgh
    """
    
    def __init__(self, request_options, http_client):
        super(Refund, self).__init__(request_options, http_client)

    def find_all(self, payment_id, request_options=None):
        return self._get(uri="/v1/payments/" + str(payment_id) + "/refunds", request_options=request_options)

    def save(self, payment_id, refund_object, request_options=None):
        if type(refund_object) is not dict:
            raise Exception("Param refund_object must be a Dictionary")

        return self._post(uri="/v1/payments/" + str(payment_id) + "/refunds", data=refund_object, request_options=request_options)
