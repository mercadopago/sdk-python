"""
    Module: payment
"""
from mercadopago.core import MPBase

class Payment(MPBase):

    """
    This class provides the methods to access the API that will allow you to create
    your own payment experience on your website.

    From basic to advanced configurations, you control the whole experience.

    [Click here for more infos](https://www.mercadopago.com.br/developers/en/guides/online-payments/checkout-api/introduction/) #pylint: disable=line-too-long
    """

    def __init__(self, request_options, http_client):
        MPBase.__init__(self, request_options, http_client)

    def search(self, filters=None, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com/developers/en/reference/payments/_payments_search/get/) #pylint: disable=line-too-long

        Args:
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Payment find response
        """
        return self._get(uri="/v1/payments/search", filters=filters,
        request_options=request_options)

    def get(self, payment_id, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com/developers/en/reference/payments/_payments_id/get/) #pylint: disable=line-too-long

        Args:
            payment_id (str): The Payment ID
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Payment find response
        """
        return self._get(uri="/v1/payments/" + str(payment_id), request_options=request_options)

    def create(self, payment_object, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com/developers/en/reference/payments/_payments/post/) #pylint: disable=line-too-long

        Args:
            payment_object (dict): Payment to be created
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param payment_object must be a Dictionary

        Returns:
            dict: Payment creation response
        """
        if not isinstance(payment_object, dict):
            raise ValueError("Param payment_object must be a Dictionary")

        return self._post(uri="/v1/payments", data=payment_object, request_options=request_options)

    def update(self, payment_id, payment_object, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/payments/_payments_id/put/) #pylint: disable=line-too-long

        Args:
            payment_id (str): The Payment ID
            payment_object (dict): Payment to be created
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param payment_object must be a Dictionary

        Returns:
            dict: Payment modification response
        """
        if not isinstance(payment_object, dict):
            raise ValueError("Param payment_object must be a Dictionary")

        return self._put(uri="/v1/payments/" + str(payment_id), data=payment_object,
        request_options=request_options)
