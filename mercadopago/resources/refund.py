from mercadopago.core import MPBase

class Refund(MPBase):

    """
    This class will allow you to refund payments created through the Payments class.

    You can refund a payment within 180 days after it was approved.
    
    You must have sufficient funds in your account in order to successfully refund the payment amount. Otherwise, you will get a 400 Bad Request error.
    
    [Click here for more infos](https://www.mercadopago.com.br/developers/en/guides/manage-account/account/cancellations-and-refunds#bookmark_refunds)
    """
    
    def __init__(self, request_options, http_client):
        super(Refund, self).__init__(request_options, http_client)

    def find_all(self, payment_id, request_options=None):
        return self._get(uri="/v1/payments/" + str(payment_id) + "/refunds", request_options=request_options)

    def save(self, payment_id, refund_object, request_options=None):
        if isinstance(refund_object, dict):
            raise ValueError("Param refund_object must be a Dictionary")

        return self._post(uri="/v1/payments/" + str(payment_id) + "/refunds", data=refund_object, request_options=request_options)
