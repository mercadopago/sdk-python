"""
    Module: identification_type
"""
from mercadopago.core import MPBase

class IdentificationType(MPBase):

    """
    Access to Identification Types
    """

    def __init__(self, request_options, http_client):
        MPBase.__init__(self, request_options, http_client)

    def list_all(self, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/identification_types/_identification_types/get/) #pylint: disable=line-too-long

        Args:
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Identification Types find response
        """
        return self._get(uri="/v1/identification_types", request_options=request_options)

    @property
    def request_options(self):
        """
        Returns the attribute value of the function
        """
        return self.__request_options
