"""
    Module: preference
"""
from mercadopago.core import MPBase


class Preference(MPBase):
    """
    This class will allow you to charge your customers through our web form
    from any device in a simple, fast and secure way.

    [Click here for more info](https://www.mercadopago.com.br/developers/en/guides/online-payments/checkout-pro/introduction)  # pylint: disable=line-too-long
    """

    def get(self, preference_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/preferences/_checkout_preferences_id/get/)  # pylint: disable=line-too-long

        Args:
            preference_id (str): The Preference ID
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Preference find response
        """
        return self._get(uri="/checkout/preferences/" + str(preference_id),
                         request_options=request_options)

    def update(self, preference_id, preference_object, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/preferences/_checkout_preferences_id/put/)  # pylint: disable=line-too-long

        Args:
            preference_id (str): The Preference ID
            preference_object (dict): Values to be modified
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param preference_object must be a Dictionary

        Returns:
            dict: Preference modification response
        """
        if not isinstance(preference_object, dict):
            raise ValueError("Param preference_object must be a Dictionary")

        return self._put(uri="/checkout/preferences/" + str(preference_id), data=preference_object,
                         request_options=request_options)

    def create(self, preference_object, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/preferences/_checkout_preferences/post/) # pylint: disable=line-too-long

        Args:
            preference_object (dict): Preference object to be created
            request_options (mercadopago.config.request_options, optional): An instance of
                RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Raises:
            ValueError: Param preference_object must be a Dictionary

        Returns:
            dict: Preference creation response
        """
        if not isinstance(preference_object, dict):
            raise ValueError("Param preference_object must be a Dictionary")

        return self._post(uri="/checkout/preferences", data=preference_object,
                          request_options=request_options)

    def search(self, filters=None, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.br/developers/en/reference/preferences/_checkout_preferences_search/get)  # pylint: disable=line-too-long

        Args:
            filters (dict): The search filters parameters
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Preference find response
        """

        return self._get(uri="/checkout/preferences/search", filters=filters,
                         request_options=request_options)
