"""Order resource for the MercadoPago Orders API.

Wraps ``/v1/orders`` endpoints covering the full order lifecycle: creation,
retrieval, search, processing, capture, cancellation, refund, and
transaction management.

`API reference
<https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/create-order/post>`_
"""
from mercadopago.core import MPBase

class Order(MPBase):
    """Manages orders and their associated transactions.

    An order groups one or more payment transactions and supports a
    two-step (authorise then capture) flow as well as direct processing.
    """

    def search(self, filters=None, request_options=None):
        """Searches orders matching the given filters.

        Args:
            filters: Query-string parameters (e.g. ``external_reference``).
            request_options: Per-call configuration overrides.

        Returns:
            dict: Paginated list of matching orders.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/search-order/get
        """
        return self._get(uri="/v1/orders", filters=filters,
                         request_options=request_options)

    def create(self, order_object, request_options=None):
        """Creates a new order.

        Args:
            order_object: Dict describing the order (items, transactions,
                payer, etc.).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *order_object* is not a ``dict``.

        Returns:
            dict: Created order including its ``id``.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/create-order/post
        """
        if not isinstance(order_object, dict):
            raise ValueError("Param order_object must be a Dictionary")

        return self._post(uri="/v1/orders", data=order_object, request_options=request_options)

    def get(self, order_id, request_options=None):
        """Retrieves a single order by its ID.

        Args:
            order_id: String identifier of the order.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *order_id* is not a ``str``.

        Returns:
            dict: Full order object.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/get-order/get
        """

        if not isinstance(order_id, str):
            raise ValueError("Param order_id must be a string")

        return self._get(uri="/v1/orders/" + str(order_id), request_options=request_options)

    def process(self, order_id, request_options=None):
        """Processes (executes payment for) an existing order.

        Triggers the payment flow for all transactions attached to the
        order.  The *order_id* is the value returned by :meth:`create`.

        Args:
            order_id: String identifier of the order to process.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *order_id* is not a ``str``.

        Returns:
            dict: Processed order with updated transaction statuses.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/process-order/post
        """

        if not isinstance(order_id, str):
            raise ValueError("Param order_id must be a string")

        return self._post(
            uri=f"/v1/orders/{order_id}/process",
            request_options=request_options,
        )

    def cancel(self, order_id, request_options=None):
        """Cancels an existing order.

        Only orders that have not yet been fully captured can be cancelled.

        Args:
            order_id: String identifier of the order.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *order_id* is not a ``str``.

        Returns:
            dict: Order cancellation response.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/cancel-order/post
        """
        if not isinstance(order_id, str):
            raise ValueError("Param order_id must be a string")

        return self._post(
            uri=f"/v1/orders/{order_id}/cancel",
            request_options=request_options,
        )

    def capture(self, order_id, request_options=None):
        """Captures a previously authorised order.

        Used in two-step payment flows where the order was created with
        ``capture=false``.

        Args:
            order_id: String identifier of the order to capture.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *order_id* is not a ``str``.

        Returns:
            dict: Captured order with updated transaction statuses.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/capture-order/post
        """

        if not isinstance(order_id, str):
            raise ValueError("Param order_id must be a string")

        return self._post(
            uri=f"/v1/orders/{order_id}/capture",
            request_options=request_options,
        )

    def create_transaction(self, order_id, transaction_object, request_options=None):
        """Adds a payment transaction to an existing order.

        Args:
            order_id: Identifier of the parent order.
            transaction_object: Dict with transaction details (payment
                method, amount, token, etc.).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *transaction_object* is not a ``dict``.
            Exception: If the API does not return HTTP 201.

        Returns:
            dict: Created transaction response.
        """
        if not isinstance(transaction_object, dict):
            raise ValueError("Param transaction_object must be a Dictionary")

        return self._post(uri=f"/v1/orders/{order_id}/transactions", data=transaction_object,
                          request_options=request_options)

    def update_transaction(
        self, order_id, transaction_id, transaction_object, request_options=None
    ):
        """Updates a transaction within an order.

        Args:
            order_id: Identifier of the parent order.
            transaction_id: Identifier of the transaction to update.
            transaction_object: Dict with the fields to modify.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *transaction_object* is not a ``dict``.
            Exception: If the API does not return HTTP 200.

        Returns:
            dict: Updated transaction response.
        """
        if not isinstance(transaction_object, dict):
            raise ValueError("Param transaction_object must be a Dictionary")

        return self._put(uri=f"/v1/orders/{order_id}/transactions/{transaction_id}",
                         data=transaction_object, request_options=request_options)

    def refund_transaction(self, order_id, transaction_object=None, request_options=None):
        """Refunds an order's transactions.

        Pass *transaction_object* with an ``amount`` key for a partial
        refund, or ``None`` for a full refund of every transaction.

        Args:
            order_id: Identifier of the order to refund.
            transaction_object: Optional dict for partial refund details.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *transaction_object* is provided but not a ``dict``.
            Exception: If the API does not return HTTP 201.

        Returns:
            dict: Refund confirmation response.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/refund-order/post
        """
        if transaction_object is not None and not isinstance(transaction_object, dict):
            raise ValueError("Param transaction_object must be a Dictionary")

        return self._post(uri=f"/v1/orders/{order_id}/refund", data=transaction_object,
                          request_options=request_options)

    def delete_transaction(self, order_id, transaction_id, request_options=None):
        """Removes a transaction from an order.

        Only transactions that have not been processed can be deleted.

        Args:
            order_id: Identifier of the parent order.
            transaction_id: Identifier of the transaction to remove.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *order_id* or *transaction_id* is not a ``str``.
            Exception: If the API does not return HTTP 204.

        Returns:
            dict: Empty response with status 204 on success.
        """
        if not isinstance(order_id, str) or not isinstance(transaction_id, str):
            raise ValueError("Params order_id and transaction_id must be strings")

        return self._delete(uri=f"/v1/orders/{order_id}/transactions/{transaction_id}",
                            request_options=request_options)
