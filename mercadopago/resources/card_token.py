from mercadopago.core import MPBase

class CardToken(MPBase):

    """
    This class will allow you to send your customers card data for Mercado Pagos server and receive a token to complete the payments transactions.
    """
    
    def __init__(self, request_options, http_client):
        super(CardToken, self).__init__(request_options, http_client)

    def find_by_id(self, id, request_options=None):
        return self._get(uri="/v1/card_tokens/" + str(id), request_options=request_options)

    def save(self, card_token_object, request_options=None):
        if type(card_token_object) is not dict:
            raise Exception("Param card_token_object must be a Dictionary")

        return self._post(uri="/v1/card_tokens", data=card_token_object, request_options=request_options)
