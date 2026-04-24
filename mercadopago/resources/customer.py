"""Customer resource for the MercadoPago API.

Wraps ``/v1/customers`` endpoints to search, retrieve, create, update, and
delete customer records.  Use alongside :class:`~mercadopago.resources.card.Card`
to enable one-click payments for returning buyers.

`API reference <https://www.mercadopago.com/developers/en/reference/customers/>`_
"""
from mercadopago.core import MPBase


class Customer(MPBase):
    """Stores and manages buyer profiles for faster checkout experiences.

    Customer records hold identification, email, and address data.
    Attach saved cards via the :class:`Card` resource to let returning
    buyers pay without re-entering card details.
    """

    def search(self, filters=None, request_options=None):
        """Searches customers matching the given filters.

        Args:
            filters: Query-string parameters (e.g. ``email``).
            request_options: Per-call configuration overrides.

        Returns:
            dict: Paginated list of matching customers.
        """
        return self._get(uri="/v1/customers/search", filters=filters,
                         request_options=request_options)

    def get(self, customer_id, request_options=None):
        """Retrieves a customer by their ID.

        Args:
            customer_id: Unique customer identifier.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Full customer object.
        """
        return self._get(uri="/v1/customers/" + str(customer_id), request_options=request_options)

    def create(self, customer_object, request_options=None):
        """Creates a new customer record.

        Args:
            customer_object: Dict with customer data (email, first_name,
                last_name, identification, etc.).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *customer_object* is not a ``dict``.

        Returns:
            dict: Created customer including its ``id``.
        """
        if not isinstance(customer_object, dict):
            raise ValueError("Param customer_object must be a Dictionary")

        return self._post(uri="/v1/customers", data=customer_object,
                          request_options=request_options)

    def update(self, customer_id, customer_object, request_options=None):
        """Updates an existing customer.

        Args:
            customer_id: Identifier of the customer to update.
            customer_object: Dict with the fields to modify.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *customer_object* is not a ``dict``.

        Returns:
            dict: Updated customer object.
        """
        if not isinstance(customer_object, dict):
            raise ValueError("Param customer_object must be a Dictionary")

        return self._put(uri="/v1/customers/" + str(customer_id), data=customer_object,
                         request_options=request_options)

    def delete(self, customer_id, request_options=None):
        """Deletes a customer record.

        Args:
            customer_id: Identifier of the customer to delete.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Deletion confirmation response.
        """
        return self._delete(uri="/v1/customers/" + str(customer_id),
                            request_options=request_options)
