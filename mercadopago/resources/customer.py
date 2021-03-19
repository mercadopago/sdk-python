"""
    Module: customer
"""
from mercadopago.core import MPBase

class Customer(MPBase):

    """
    This class allows you to store customers data safely to improve the shopping experience.

    This will allow your customer to complete their purchases much faster and easily when
    used in conjunction with the Cards class.

    [Click here for more infos](https://mercadopago.com.br/developers/en/guides/online-payments/web-tokenize-checkout/customers-and-cards) #pylint: disable=line-too-long
    """

    def __init__(self, request_options, http_client):
        MPBase.__init__(self, request_options, http_client)

    def search(self, filters=None, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/customers/_customers_search/get/) #pylint: disable=line-too-long

        Args:
            filters (dict): The search filters parameters
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Customer find response
        """
        return self._get(uri="/v1/customers/search", filters=filters,
        request_options=request_options)

    def get(self, customer_id, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com/developers/en/reference/customers/_customers_id/get/) #pylint: disable=line-too-long

        Args:
            customer_id (str): The Customer ID owner
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Customer find response
        """
        return self._get(uri="/v1/customers/" + str(customer_id), request_options=request_options)

    def create(self, customer_object, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/customers/_customers/post/) #pylint: disable=line-too-long

        Args:
            customer_object (dict): Customer object to be created
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param customer_object must be a Dictionary

        Returns:
            dict: Customer creation response
        """
        if not isinstance(customer_object, dict):
            raise ValueError("Param customer_object must be a Dictionary")

        return self._post(uri="/v1/customers", data=customer_object,
        request_options=request_options)

    def update(self, customer_id, customer_object, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/customers/_customers_id/put/) #pylint: disable=line-too-long

        Args:
            customer_id (str): The Customer ID owner
            customer_object (dict): Customer object to be updated
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValeuError: Param customer_object must be a Dictionary

        Returns:
            dict: Customer modification response
        """
        if not isinstance(customer_object, dict):
            raise ValueError("Param customer_object must be a Dictionary")

        return self._put(uri="/v1/customers/" + str(customer_id), data=customer_object,
        request_options=request_options)

    def delete(self, customer_id, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/cards/_customers_customer_id_cards_id/delete/) #pylint: disable=line-too-long

        Args:
            customer_id (str): The Customer ID owner
            customer_object (dict): Customer object to be updated
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Returns:
            dict: Customer exclusion response
        """
        return self._delete(uri="/v1/customers/" + str(customer_id),
        request_options=request_options)
