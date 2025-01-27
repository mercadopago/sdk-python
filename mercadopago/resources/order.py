"""
    Module: order
"""
from mercadopago.core import MPBase


class Order(MPBase):
    """
    This class provides the methods to access the API that will allow you to create
    your own order experience on your website.

    From basic to advanced configurations, you control the whole experience.

    [Click here for more info](https://www.mercadopago.com/developers/en/guides/online-payments/checkout-api/introduction/)  # pylint: disable=line-too-long
    """

    def create(self, order_object, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/order/online-payments/create/post/)  # pylint: disable=line-too-long

        Args:
            order_object (dict): Order to be created
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param order_object must be a Dictionary

        Returns:
            dict: Order creation response
        """
        if not isinstance(order_object, dict):
            raise ValueError("Param order_object must be a Dictionary")

        return self._post(uri="/v1/orders", data=order_object, request_options=request_options)
