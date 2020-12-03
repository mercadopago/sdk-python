from mercadopago.core import MPBase

class Card(MPBase):

    """
    The cards class is the way to store card data of your customers safely to improve the shopping experience.

    This will allow your customers to complete their purchases much faster and easily, since they will not have to complete their card data again.
    
    This class must be used in conjunction with the Customer class.

    [Click here for more infos](https://www.mercadopago.com.br/developers/en/guides/online-payments/web-tokenize-checkout/customers-and-cards)
    """
    
    def __init__(self, request_options, http_client):
        super(Card, self).__init__(request_options, http_client)

    def get_list(self, customer_id, request_options=None):
        return self._get(uri="/v1/customers/" + str(customer_id) + "/cards", request_options=request_options)

    def get(self, customer_id, card_id, request_options=None):
        return self._get(uri="/v1/customers/" + str(customer_id) + "/cards/" + str(card_id), request_options=request_options)

    def create(self, customer_id, card_object, request_options=None):
        if type(card_object) is not dict:
            raise ValueError("Param card_object must be a Dictionary")

        return self._post(uri="/v1/customers/" + str(customer_id) + "/cards/", data=card_object, request_options=request_options)

    def update(self, customer_id, card_id, card_object, request_options=None):
        if type(card_object) is not dict:
            raise ValueError("Param card_object must be a Dictionary")

        return self._put(uri="/v1/customers/" + str(customer_id) + "/cards/" + str(card_id), data=card_object, request_options=request_options)

    def delete(self, customer_id, card_id, request_options=None):
        return self._delete(uri="/v1/customers/" + str(customer_id) + "/cards/" + str(card_id), request_options=request_options)
        
