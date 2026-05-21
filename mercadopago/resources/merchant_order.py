"""Merchant Order resource for the MercadoPago API.

Wraps ``/merchant_orders`` endpoints to search, retrieve, create, and
update merchant orders.  A merchant order groups one or more Checkout
Pro payments under a single business reference.

`API reference
<https://www.mercadopago.com/developers/en/reference>`_
"""
from mercadopago.core import MPBase


class MerchantOrder(MPBase):
    """Groups payments into a single merchant-level order.

    Merchant orders are typically created automatically by Checkout Pro
    preferences but can also be managed manually to attach additional
    payments or shipments.
    """

    def search(self, filters=None, request_options=None):
        """Searches merchant orders matching the given filters.

        Args:
            filters: Query-string parameters (e.g. ``external_reference``).
            request_options: Per-call configuration overrides.

        Returns:
            dict: Paginated list of matching merchant orders.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-pro/merchant_orders/search-merchant-order/get
        """
        return self._get(uri="/merchant_orders/search", filters=filters,
                         request_options=request_options)

    def get(self, merchan_order_id, request_options=None):
        """Retrieves a merchant order by its ID.

        Args:
            merchan_order_id: Unique merchant order identifier.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Full merchant order object including attached payments.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-pro/merchant_orders/get-merchant-order/get
        """
        return self._get(uri="/merchant_orders/" + str(merchan_order_id),
                         request_options=request_options)

    def update(self, merchan_order_id, merchant_order_object, request_options=None):
        """Updates an existing merchant order.

        Args:
            merchan_order_id: Identifier of the merchant order to update.
            merchant_order_object: Dict with the fields to modify.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *merchant_order_object* is not a ``dict``.

        Returns:
            dict: Updated merchant order object.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-pro/merchant_orders/update-merchant-order/put
        """
        if not isinstance(merchant_order_object, dict):
            raise ValueError(
                "Param merchant_order_object must be a Dictionary")

        return self._put(uri="/merchant_orders/" + str(merchan_order_id),
                         data=merchant_order_object, request_options=request_options)

    def create(self, merchant_order_object, request_options=None):
        """Creates a new merchant order.

        Args:
            merchant_order_object: Dict describing the order (items,
                preference_id, application_id, etc.).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *merchant_order_object* is not a ``dict``.

        Returns:
            dict: Created merchant order including its ``id``.

        Reference: https://www.mercadopago.com/developers/en/reference
        """
        if not isinstance(merchant_order_object, dict):
            raise ValueError(
                "Param merchant_order_object must be a Dictionary")

        return self._post(uri="/merchant_orders", data=merchant_order_object,
                          request_options=request_options)
