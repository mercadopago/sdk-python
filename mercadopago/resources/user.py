"""
    Module: user
"""
from mercadopago.core import MPBase

class User(MPBase):

    """
    Access to Users
    """

    def __init__(self, request_options, http_client):
        MPBase.__init__(self, request_options, http_client)

    def get(self, request_options=None):
        """Args:
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: User find response
        """
        return self._get(uri="/users/me", request_options=request_options)

    @property
    def request_options(self):
        """
        Returns the attribute value of the function
        """
        return self.__request_options
