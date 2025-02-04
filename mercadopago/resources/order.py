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

    def cancel(self, order_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.br/developers/en/reference/order/in-person-payments/point/cancel-order/post) # pylint: disable=line-too-long
        Args:
            order_id (str): Order ID
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.

        Raises:
            ValueError: Param order_id must be a string

        Returns:
            dict: Order cancellation response
        """
        if not isinstance(order_id, str):
            raise ValueError("Param order_id must be a string")

        return self._post(uri="/v1/orders/" + str(order_id) + "/cancel", request_options=request_options)

    def capture(self, order_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com.br/developers/pt/reference/order/online-payments/capture/post)  # pylint: disable=line-too-long
        Args:
            order_id (str): ID of the order to be captured. This value is returned in the response to the Create order request.
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to ur REST call.
            Defaults to None.
        Raises:
            ValueError: Param order_id must be a string
        Returns:
            dict: Order ID returned in the response to the request made for its creation.
        """

        if not isinstance(order_id, str):
            raise ValueError("Param order_id must be a string")

        return self._post(uri="/v1/orders/" + str(order_id) + "/capture", request_options=request_options)