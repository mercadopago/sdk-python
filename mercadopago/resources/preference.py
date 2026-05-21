"""Checkout Preference resource for the MercadoPago API.

Wraps ``/checkout/preferences`` endpoints to create, retrieve, update,
and search payment preferences used by Checkout Pro.

`API reference <https://www.mercadopago.com/developers/en/reference/online-payments/checkout-pro/preferences/create-preference/post>`_
"""
from mercadopago.core import MPBase


class Preference(MPBase):
    """Manages Checkout Pro payment preferences.

    A preference defines the items, payer information, payment methods,
    and redirect URLs for a Checkout Pro session.  The ``init_point``
    returned by :meth:`create` is the URL you redirect buyers to.
    """

    def get(self, preference_id, request_options=None):
        """Retrieves a preference by its ID.

        Args:
            preference_id: Unique preference identifier.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Full preference object.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-pro/preferences/get-preference/get
        """
        return self._get(uri="/checkout/preferences/" + str(preference_id),
                         request_options=request_options)

    def update(self, preference_id, preference_object, request_options=None):
        """Updates an existing preference.

        Args:
            preference_id: Identifier of the preference to update.
            preference_object: Dict with the fields to modify.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *preference_object* is not a ``dict``.

        Returns:
            dict: Updated preference object.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-pro/preferences/update-preference/put
        """
        if not isinstance(preference_object, dict):
            raise ValueError("Param preference_object must be a Dictionary")

        return self._put(uri="/checkout/preferences/" + str(preference_id), data=preference_object,
                         request_options=request_options)

    def create(self, preference_object, request_options=None):
        """Creates a new checkout preference.

        The response includes ``init_point`` and ``sandbox_init_point``
        URLs to redirect buyers to the Checkout Pro flow.

        Args:
            preference_object: Dict defining items, payer, back_urls,
                payment_methods, etc.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *preference_object* is not a ``dict``.

        Returns:
            dict: Created preference including ``id`` and ``init_point``.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-pro/preferences/create-preference/post
        """
        if not isinstance(preference_object, dict):
            raise ValueError("Param preference_object must be a Dictionary")

        return self._post(uri="/checkout/preferences", data=preference_object,
                          request_options=request_options)

    def search(self, filters=None, request_options=None):
        """Searches preferences matching the given filters.

        Args:
            filters: Query-string parameters (e.g. ``external_reference``).
            request_options: Per-call configuration overrides.

        Returns:
            dict: Paginated list of matching preferences.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-pro/preferences/search-preferences/get
        """

        return self._get(uri="/checkout/preferences/search", filters=filters,
                         request_options=request_options)
