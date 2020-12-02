from mercadopago.core import MPBase

class Payment(MPBase):

    """
    This class provides the methods to access the API that will allow you to create your own payment experience on your website.
    
    From basic to advanced configurations, you control the whole experience.
    
    [Click here for more infos](https://www.mercadopago.com.br/developers/en/guides/online-payments/checkout-api/introduction/)
    """
    
    def __init__(self, request_options, http_client):
        super(Payment, self).__init__(request_options, http_client)

    def search(self, filters, request_options=None):
        return self._get(uri="/v1/payments/search", filters=filters, request_options=request_options)

    def find_by_id(self, id, request_options=None):
        return self._get(uri="/v1/payments/" + str(id), request_options=request_options)

    #TODO LÓGICA REQUEST_OPTION IS NOT NONE INSERIR IDEMPOTENCE_KEY
    def create(self, payment_object, request_options=None):
        if type(payment_object) is not dict:
            raise ValueError("Param payment_object must be a Dictionary")

        return self._post(uri="/v1/payments", data=payment_object, request_options=request_options)

    def update(self, id, payment_object, request_options=None):
        if type(payment_object) is not dict:
            raise ValueError("Param payment_object must be a Dictionary")

        return self._put(uri="/v1/payments/" + str(id), data=payment_object, request_options=request_options)
