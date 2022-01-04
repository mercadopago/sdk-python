"""
    Module: card_token
"""
from mercadopago.core import MPBase


class CardToken(MPBase):
    """
    This class will allow you to send your customers card data for Mercado Pago
    server and receive a token to complete the payments transactions.
    """

    def get(self, card_token_id, request_options=None):
        """Args:
            card_token_id (str): The Card Token ID
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Card Token find response
        """
        return self._get(uri="/v1/card_tokens/" + str(card_token_id),
                         request_options=request_options)

    def create(self, card_token_object, request_options=None):
        """Args:
            card_token_object (dict): Card Token to be created
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param card_token_object must be a Dictionary

        Returns:
            dict: Card Token creation response
        """
        if not isinstance(card_token_object, dict):
            raise ValueError("Param card_token_object must be a Dictionary")

        return self._post(uri="/v1/card_tokens", data=card_token_object,
                          request_options=request_options)
