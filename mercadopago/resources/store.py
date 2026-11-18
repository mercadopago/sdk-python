"""Store resource for the MercadoPago API.

Wraps the ``/users/{user_id}/stores`` endpoints to create, retrieve,
search, update, and delete physical stores associated with a seller
account.

`API reference
<https://www.mercadopago.com/developers/en/reference>`_
"""
from mercadopago.core import MPBase


class Store(MPBase):
    """Manages physical stores for in-person (Point) payments.

    A store groups point-of-sale devices under a business location and
    is scoped to a Mercado Pago user account.
    """

    def create(self, user_id, store_object, request_options=None):
        """Creates a new store for the given user.

        Args:
            user_id: Identifier of the store owner.
            store_object: Dict describing the store (name, business_hours,
                location, etc.).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *store_object* is not a ``dict``.

        Returns:
            dict: Created store object including its ``id``.

        Reference: https://www.mercadopago.com/developers/en/reference
        """
        if not isinstance(store_object, dict):
            raise ValueError(
                "Param store_object must be a Dictionary")

        return self._post(uri="/users/" + self._path_param(user_id) + "/stores",
                          data=store_object, request_options=request_options)

    def get(self, store_id, request_options=None):
        """Retrieves a store by its ID.

        Args:
            store_id: Unique store identifier.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Full store object.

        Reference: https://www.mercadopago.com/developers/en/reference
        """
        return self._get(uri="/stores/" + self._path_param(store_id),
                         request_options=request_options)

    def search(self, user_id, filters=None, request_options=None):
        """Searches the stores of the given user.

        Args:
            user_id: Identifier of the store owner.
            filters: Query-string parameters (e.g. ``external_id``).
            request_options: Per-call configuration overrides.

        Returns:
            dict: Paginated list of matching stores.

        Reference: https://www.mercadopago.com/developers/en/reference
        """
        return self._get(uri="/users/" + self._path_param(user_id) + "/stores/search",
                         filters=filters, request_options=request_options)

    def update(self, user_id, store_id, store_object, request_options=None):
        """Updates an existing store.

        Args:
            user_id: Identifier of the store owner.
            store_id: Identifier of the store to update.
            store_object: Dict with the fields to modify.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *store_object* is not a ``dict``.

        Returns:
            dict: Updated store object.

        Reference: https://www.mercadopago.com/developers/en/reference
        """
        if not isinstance(store_object, dict):
            raise ValueError(
                "Param store_object must be a Dictionary")

        return self._put(uri="/users/" + self._path_param(user_id) + "/stores/"
                         + self._path_param(store_id),
                         data=store_object, request_options=request_options)

    def delete(self, user_id, store_id, request_options=None):
        """Deletes a store by its ID.

        Args:
            user_id: Identifier of the store owner.
            store_id: Identifier of the store to delete.
            request_options: Per-call configuration overrides.

        Returns:
            dict: ``{"status": <http_code>, "response": <parsed_json>}``.

        Reference: https://www.mercadopago.com/developers/en/reference
        """
        return self._delete(uri="/users/" + self._path_param(user_id) + "/stores/"
                            + self._path_param(store_id),
                            request_options=request_options)
