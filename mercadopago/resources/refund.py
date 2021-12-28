"""
    Module: refund
"""
from mercadopago.core import MPBase


class Refund(MPBase):
    """
    This class will allow you to refund payments created through the Payments class.

    You can refund a payment within 180 days after it was approved.

    You must have sufficient funds in your account in order to successfully refund
    the payment amount. Otherwise, you will get a 400 Bad Request error.

    [Click here for more info](https://www.mercadopago.com.br/developers/en/guides/manage-account/account/cancellations-and-refunds#bookmark_refunds)  # pylint: disable=line-too-long
    """

    def list_all(self, payment_id, request_options=None):
        """Args:
            payment_id (str): The Payment ID
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Returns:
            dict: List all refunds of a payment
        """
        return self._get(uri="/v1/payments/" + str(payment_id) + "/refunds",
                         request_options=request_options)

    def create(self, payment_id, refund_object=None, request_options=None):
        """Args:
            payment_id (str): The Payment ID
            refund_object (dict): Refund to be created
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param refund_object must be a Dictionary

        Returns:
            dict: Refund creation response
        """
        if refund_object is not None and not isinstance(refund_object, dict):
            raise ValueError("Param refund_object must be a Dictionary")

        return self._post(uri="/v1/payments/" + str(payment_id) + "/refunds",
                          data=refund_object, request_options=request_options)
