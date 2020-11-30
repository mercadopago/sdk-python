from mercadopago.core import MPBase

class MerchantOrder(MPBase):

    """
    This class will allow you to create and manage your orders. You can attach one or more payments in your merchant order.
    """
    
    def __init__(self, request_options, http_client):
        super(MerchantOrder, self).__init__(request_options, http_client)
     
    def find_by_id(self, id, request_options=None):  
        return self._get(uri="/merchant_orders/" + str(id), request_options=request_options)

    def update(self, id, merchant_order_object, request_options=None):
        if type(merchant_order_object) is not dict:
            raise ValueError('Param merchant_order_object must be a Dictionary')

        return self._put(uri="/merchant_orders/" + str(id), data=merchant_order_object, request_options=request_options)

    def save(self, merchant_order_object, request_options=None):
        if type(merchant_order_object) is not dict:
            raise ValueError('Param merchant_order_object must be a Dictionary')

        return self._post(uri="/merchant_orders", data=merchant_order_object, request_options=request_options)
