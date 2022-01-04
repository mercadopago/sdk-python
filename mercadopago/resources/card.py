"""
    Module: card
"""
from mercadopago.core import MPBase


class Card(MPBase):
    """
    The cards class is the way to store card data of your customers
    safely to improve the shopping experience.

    This will allow your customers to complete their purchases much
    faster and easily, since they will not have to complete their
    card data again.

    This class must be used in conjunction with the Customer class.

    [Click here for more info](https://www.mercadopago.com/developers/en/guides/online-payments/web-tokenize-checkout/customers-and-cards)  # pylint: disable=line-too-long
    """

    def list_all(self, customer_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/cards/_customers_customer_id_cards/get/)  # pylint: disable=line-too-long

        Args:
            customer_id (str): The Customer ID owner
            request_options (mercadopago.config.request_options, optional):
            An instance of RequestOptions can be pass changing or adding
            custom options to ur REST call. Defaults to None.

        Returns:
            dict: Cards find response
        """
        return self._get(
            uri=f"/v1/customers/{str(customer_id)}/cards",
            request_options=request_options,
        )

    def get(self, customer_id, card_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/cards/_customers_customer_id_cards_id/get/)  # pylint: disable=line-too-long

        Args:
            customer_id (str): The Customer ID owner
            card_id (dict): Card ID to be found
            request_options (mercadopago.config.request_options, optional):
            An instance of RequestOptions can be pass changing or adding
            custom options to ur REST call. Defaults to None.

        Returns:
            dict: Card find response
        """
        return self._get(
            uri=f"/v1/customers/{str(customer_id)}/cards/{str(card_id)}",
            request_options=request_options,
        )

    def create(self, customer_id, card_object, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/cards/_customers_customer_id_cards/post/)  # pylint: disable=line-too-long

        Args:
            customer_id (str): The Customer ID owner
            card_object (dict): Card object to be created
            request_options (mercadopago.config.request_options, optional):
            An instance of RequestOptions can be pass changing or adding
            custom options to ur REST call. Defaults to None.

        Raises:
            ValueError: Param card_object must be a Dictionary

        Returns:
            dict: Card creation response
        """
        if not isinstance(card_object, dict):
            raise ValueError("Param card_object must be a Dictionary")

        return self._post(uri="/v1/customers/" + str(customer_id)
                          + "/cards/", data=card_object, request_options=request_options)

    def update(self, customer_id, card_id, card_object, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/cards/_customers_customer_id_cards_id/put/)  # pylint: disable=line-too-long

        Args:
            customer_id (str): Customer ID owner
            card_id (str): Card ID to be modified
            card_object (dict): Values to be modified
            request_options (mercadopago.config.request_options, optional):
            An instance of RequestOptions can be pass changing or adding
            custom options to ur REST call. Defaults to None.

        Raises:
            ValueError: Param card_object must be a Dictionary

        Returns:
            dict: Card modification response
        """
        if not isinstance(card_object, dict):
            raise ValueError("Param card_object must be a Dictionary")

        return self._put(uri="/v1/customers/" + str(customer_id)
                         + "/cards/" + str(card_id), data=card_object,
                         request_options=request_options)

    def delete(self, customer_id, card_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/cards/_customers_customer_id_cards_id/delete/)  # pylint: disable=line-too-long

        Args:
            customer_id (str): Customer ID owner
            card_id (str): Card ID to be deleted
            request_options (mercadopago.config.request_options, optional):
            An instance of RequestOptions can be pass changing or adding
            custom options to ur REST call. Defaults to None.

        Returns:
            dict: Card exclusion response
        """
        return self._delete(uri="/v1/customers/" + str(customer_id)
                            + "/cards/" + str(card_id), request_options=request_options)
