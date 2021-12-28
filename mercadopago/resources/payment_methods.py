"""
    Module: payment_methods
"""
from mercadopago.core import MPBase


class PaymentMethods(MPBase):
    """
    Access to Payment Methods
    """

    def list_all(self, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/payment_methods/_payment_methods/get/)  # pylint: disable=line-too-long

        Args:
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: Payment Methods find response
        """
        return self._get(uri="/v1/payment_methods", request_options=request_options)

    @property
    def request_options(self):
        """
        Returns the attribute value of the function
        """
        return self.__request_options
