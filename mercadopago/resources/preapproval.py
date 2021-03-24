"""
    Module: preapproval
"""
from mercadopago.core import MPBase

class PreApproval(MPBase):

    """
    This class provides the methods to access the API that will allow you to create
    your own preapproval experience on your website.

    From basic to advanced configurations, you control the whole experience.

    [Click here for more infos](https://www.mercadopago.com.br/developers/en/guides/online-payments/subscriptions/introduction) #pylint: disable=line-too-long
    """

    def __init__(self, request_options, http_client):
        MPBase.__init__(self, request_options, http_client)

    def search(self, filters=None, request_options=None):
        """Args:
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: PreApproval find response
        """
        return self._get(uri="/preapproval/search", filters=filters,
        request_options=request_options)

    def get(self, preapproval_id, request_options=None):
        """Args:
            preapproval_id (str): The PreApproval ID
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: PreApproval find response
        """
        return self._get(uri="/preapproval/" +str(preapproval_id), request_options=request_options)

    def create(self, preapproval_object, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com/developers/en/reference/subscriptions/_preapproval/post/) #pylint: disable=line-too-long

        Args:
            preapproval_object (dict): PreApproval to be created
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param preapproval_object must be a Dictionary

        Returns:
            dict: PreApproval creation response
        """
        if not isinstance(preapproval_object, dict):
            raise ValueError("Param preapproval_object must be a Dictionary")

        return self._post(uri="/preapproval",
        data=preapproval_object, request_options=request_options)

    def update(self, preapproval_id, preapproval_object, request_options=None):
        """Args:
            preapproval_id (str): The PreApproval ID
            preapproval_object (dict): PreApproval to be created
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param preapproval_object must be a Dictionary

        Returns:
            dict: PreApproval modification response
        """
        if not isinstance(preapproval_object, dict):
            raise ValueError("Param preapproval_object must be a Dictionary")

        return self._put(uri="/preapproval" + str(preapproval_id),
        data=preapproval_object, request_options=request_options)
