"""
    Module: subscriptions
"""
from mercadopago.core import MPBase


class Subscription(MPBase):
    """
    This class provides the methods to access the API that will allow you to create, search, get and update
    Subscriptions.

    [Click here for more info](https://www.mercadopago.com.br/developers/en/docs/subscriptions/landing)  # pylint: disable=line-too-long
    """

    def search(self, filters=None, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.co/developers/en/reference/subscriptions/_preapproval_search/get)  # pylint: disable=line-too-long

        Args:
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Subscriptions found
        """
        return self._get(
            uri="/preapproval/search",
            filters=filters,
            request_options=request_options)

    def get(self, subscription_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.co/developers/en/reference/subscriptions/_preapproval_id/get)  # pylint: disable=line-too-long

        Args:
            subscription_id (str): The subscription ID
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Subscription found
        """
        return self._get(
            uri="/preapproval/" + str(subscription_id),
            request_options=request_options)

    def create(self, subscription_object, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.co/developers/en/reference/subscriptions/_preapproval/post)  # pylint: disable=line-too-long

        Args:
            subscription_object (dict): Subscription to be created
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param payment_object must be a Dictionary

        Returns:
            dict: Subscription creation response
        """
        if not isinstance(subscription_object, dict):
            raise ValueError("Param subscription_object must be a Dictionary")

        return self._post(
            uri="/preapproval",
            data=subscription_object,
            request_options=request_options)

    def update(self, subscription_id, subscription_object, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.co/developers/en/reference/subscriptions/_preapproval_id/put)  # pylint: disable=line-too-long

        Args:
            subscription_id (str): The subscription ID to be updated
            subscription_object (dict): Subscription information to be updated
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param subscription_object must be a Dictionary

        Returns:
            dict: Subscription modification response
        """
        if not isinstance(subscription_object, dict):
            raise ValueError("Param subscription_object must be a Dictionary")

        return self._put(
            uri="/preapproval/" + str(subscription_id),
            data=subscription_object,
            request_options=request_options)
