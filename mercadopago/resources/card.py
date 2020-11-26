from mercadopago.core.mp_base import MPBase

class Card(MPBase):
    def __init__(self, request_options):
        super(Card, self).__init__(request_options)

    def find_all(self, customer_id):
        return self._get(uri="/v1/customers/" + str(customer_id))

    def find_by_id(self, customer_id, card_id, request_options=None):
        return self._get(uri="/v1/customers/" + str(customer_id) + "/cards/" + str(card_id), request_options=request_options)

    def create(self, customer_id, card_object, request_options=None):
        if type(card_object) is not dict:
            raise Exception("Param card_object must be a Dictionary")

        return self._post(uri="/v1/customers/" + str(customer_id) + "/cards/", data=card_object, request_options=request_options)

    def update(self, customer_id, card_id, card_object, request_options=None):
        if type(card_object) is not dict:
            raise Exception("Param card_object must be a Dictionary")

        return self._put(uri="/v1/customers/" + str(customer_id) + "/cards/" + str(card_id), data=card_object, request_options=request_options)

    def delete(self, customer_id, card_id, request_options=None):
        return self._delete(uri="/v1/customers/" + str(customer_id) + "/cards/" + str(card_id), request_options=request_options)
        
