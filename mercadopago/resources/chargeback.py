"""
    Module: chargeback
"""
from mercadopago.core import MPBase


class Chargeback(MPBase):
    """
    Access to Chargebacks

    [Click here for more info](https://www.mercadopago.com.br/developers/pt/guides/manage-account/account/chargebacks)  # pylint: disable=line-too-long
    """

    def search(self, filters=None, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.br/developers/pt/reference/chargebacks/_chargebacks_search/get)  # pylint: disable=line-too-long

        Args:
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Chargeback find response
        """
        return self._get(uri="/v1/chargebacks/search", filters=filters,
                         request_options=request_options)

    def get(self, chargeback_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.br/developers/pt/reference/chargebacks/_chargebacks_id/get)  # pylint: disable=line-too-long

        Args:
            chargeback_id (str): The Chargeback ID
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Chargeback find response
        """
        return self._get(uri="/v1/chargebacks/" + str(chargeback_id),
                         request_options=request_options)
