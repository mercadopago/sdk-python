"""Store resource for the MercadoPago API.

Wraps the ``/users/{user_id}/stores`` endpoint to create physical
stores associated with a MercadoPago account.
"""
from mercadopago.core import MPBase


class Store(MPBase):
    """Manages physical stores for a MercadoPago account.

    Stores are used by in-person payment products (e.g. Point) to
    associate orders and devices with a physical location.
    """

    def create(self, user_id, store_object, request_options=None):
        """Creates a new store for the given user.

        Args:
            user_id: Identifier of the store owner (MercadoPago user).
            store_object: Dict describing the store (name, business_hours,
                location, etc.).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *store_object* is not a ``dict``.

        Returns:
            dict: Created store including its ``id``.

        Reference: https://www.mercadopago.com/developers/en/reference
        """
        if not isinstance(store_object, dict):
            raise ValueError("Param store_object must be a Dictionary")

        return self._post(
            uri="/users/" + self._path_param(user_id) + "/stores",
            data=store_object,
            request_options=request_options,
        )


    def get(self, store_id, request_options=None):
        """Retrieves a store by its ID.

        Args:
            store_id: Unique store identifier.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Full store object.

        Reference: https://www.mercadopago.com/developers/en/reference
        """
        return self._get(
            uri="/stores/" + self._path_param(store_id),
            request_options=request_options,
        )

    def search(self, user_id, filters=None, request_options=None):
        """Searches the stores of a given user.

        Args:
            user_id: Identifier of the store owner (MercadoPago user).
            filters: Query-string parameters (e.g. pagination).
            request_options: Per-call configuration overrides.

        Returns:
            dict: Paginated list of stores.

        Reference: https://www.mercadopago.com/developers/en/reference
        """
        return self._get(
            uri="/users/" + self._path_param(user_id) + "/stores/search",
            filters=filters,
            request_options=request_options,
        )

    def update(self, user_id, store_id, store_object, request_options=None):
        """Updates an existing store.

        Args:
            user_id: Identifier of the store owner (MercadoPago user).
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
            raise ValueError("Param store_object must be a Dictionary")

        return self._put(
            uri="/users/" + self._path_param(user_id) + "/stores/"
            + self._path_param(store_id),
            data=store_object,
            request_options=request_options,
        )

    def delete(self, user_id, store_id, request_options=None):
        """Deletes a store by its ID.

        Args:
            user_id: Identifier of the store owner (MercadoPago user).
            store_id: Identifier of the store to delete.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Empty response on success.

        Reference: https://www.mercadopago.com/developers/en/reference
        """
        return self._delete(
            uri="/users/" + self._path_param(user_id) + "/stores/"
            + self._path_param(store_id),
            request_options=request_options,
        )
