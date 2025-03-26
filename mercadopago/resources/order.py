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
            RequestOptions can be pass changing or adding custom options to the REST call.
            Defaults to None.

        Raises:
            ValueError: Param order_object must be a Dictionary

        Returns:
            dict: Order creation response
        """
        if not isinstance(order_object, dict):
            raise ValueError("Param order_object must be a Dictionary")

        return self._post(uri="/v1/orders", data=order_object, request_options=request_options)

    def get(self, order_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/order/online-payments/get-order/get ) # pylint: disable=line-too-long

        Args:
            order_id (str): The Order ID
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to the REST call.
            Defaults to None.

        Raises:
        ValueError: Param order_id must be a string

        Returns:
            dict: Order returned in the response to the request made for its creation.
        """

        if not isinstance(order_id, str):
            raise ValueError("Param order_id must be a string")

        return self._get(uri="/v1/orders/" + str(order_id), request_options=request_options)

    def process(self, order_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/order/online/process-order/post) # pylint: disable=line-too-long
        Args:
            order_id (str): ID of the order to be processed. This value is returned in the response to the Create order request.
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to the REST call.
            Defaults to None.

        Raises:
            ValueError: Param order_id must be a string
        Returns:
            dict: Order returned in the response to the request made for its creation.
        """

        if not isinstance(order_id, str):
            raise ValueError("Param order_id must be a string")

        return self._post(uri="/v1/orders/" + str(order_id) + "/process", request_options=request_options) # pylint: disable=line-too-long

    def cancel(self, order_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/order/online-payments/cancel-order/post) # pylint: disable=line-too-long
        Args:
            order_id (str): Order ID
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to the REST call.
            Defaults to None.

        Raises:
            ValueError: Param order_id must be a string

        Returns:
            dict: Order cancellation response
        """
        if not isinstance(order_id, str):
            raise ValueError("Param order_id must be a string")

        return self._post(uri="/v1/orders/" + str(order_id) + "/cancel", request_options=request_options) # pylint: disable=line-too-long

    def capture(self, order_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/order/online-payments/capture/post)  # pylint: disable=line-too-long
        Args:
            order_id (str): ID of the order to be captured. This value is returned in the response to the Create order request.
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to the REST call.
            Defaults to None.
        Raises:
            ValueError: Param order_id must be a string
        Returns:
            dict: Order returned in the response to the request made for its creation.
        """

        if not isinstance(order_id, str):
            raise ValueError("Param order_id must be a string")

        return self._post(uri="/v1/orders/" + str(order_id) + "/capture", request_options=request_options) # pylint: disable=line-too-long

    def create_transaction(self, order_id, transaction_object, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/order/online-payments/add-transaction/post)  # pylint: disable=line-too-long

        Args:
            order_id (str): The ID of the order to which the transaction will be added
            transaction_object (dict): Transaction to be added
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to the REST call.
            Defaults to None.

        Raises:
            ValueError: Param transaction_object must be a Dictionary

        Returns:
            dict: Transaction created response
        """
        if not isinstance(transaction_object, dict):
            raise ValueError("Param transaction_object must be a Dictionary")

        response = self._post(uri=f"/v1/orders/{order_id}/transactions", data=transaction_object,
                              request_options=request_options)
        if response.get("status") != 201:
            raise Exception(f"Failed to add transaction: {response}")  # pylint: disable=broad-exception-raised
        return response

    def update_transaction(self, order_id, transaction_id, transaction_object, request_options=None): # pylint: disable=line-too-long
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/order/online-payments/update-transaction/put)  # pylint: disable=line-too-long

        Args:
            order_id (str): The ID of the order to which the transaction belongs
            transaction_id (str): The ID of the transaction to be updated
            transaction_object (dict): Transaction details to be updated
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to the REST call.
            Defaults to None.

        Raises:
            ValueError: Param transaction_object must be a Dictionary

        Returns:
            dict: Transaction update response
        """
        if not isinstance(transaction_object, dict):
            raise ValueError("Param transaction_object must be a Dictionary")

        response = self._put(uri=f"/v1/orders/{order_id}/transactions/{transaction_id}",
                             data=transaction_object, request_options=request_options)
        if response.get("status") != 200:
            raise Exception(f"Failed to update transaction: {response}")  # pylint: disable=broad-exception-raised
        return response

    def refund_transaction(self, order_id, transaction_object=None, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/order/online-payments/refund/post)  # pylint: disable=line-too-long
        Args:
            order_id (str): The ID of the order to which the transaction belongs
            transaction_object (dict, optional): Transaction details to be updated
            request_options (mercadopago.config.request_options, optional): An instance of
            RequestOptions can be pass changing or adding custom options to the REST call.
            Defaults to None.
        Raises:
            ValueError: Param transaction_object must be a Dictionary
        Returns:
            dict: Order refunded response
        """
        if transaction_object is not None and not isinstance(transaction_object, dict):
            raise ValueError("Param transaction_object must be a Dictionary")

        response = self._post(uri=f"/v1/orders/{order_id}/refund", data=transaction_object,
                              request_options=request_options)
        if response.get("status") != 201:
            raise Exception(f"Failed to refund transaction: {response}")  # pylint: disable=broad-exception-raised
        return response

    def delete_transaction(self, order_id, transaction_id, request_options=None):
        """[Click here for more info](https://www.mercadopago.com/developers/en/reference/order/online-payments/delete-transaction/delete)  # pylint: disable=line-too-long
                Args:
                    order_id (str): The ID of the order to which the transaction belongs
                    transaction_id (str): The ID of the transaction to be deleted
                    request_options (mercadopago.config.request_options, optional): An instance of
                    RequestOptions can be pass changing or adding custom options to the REST call.
                    Defaults to None.
                Raises:
                    ValueError: Params order_id and transaction_id must be strings
                Returns:
                    Status 204 - No Content - if deleted successfully
                """
        if not isinstance(order_id, str) or not isinstance(transaction_id, str):
            raise ValueError("Params order_id and transaction_id must be strings")

        response = self._delete(uri=f"/v1/orders/{order_id}/transactions/{transaction_id}",
                                request_options=request_options)

        if response.get("status") != 204:
            raise Exception(f"Failed to delete transaction: {response}")  # pylint: disable=broad-exception-raised
        return response
