"""Saved-card resource for the MercadoPago API.

Wraps ``/v1/customers/{customer_id}/cards`` endpoints to list, retrieve,
create, update, and delete cards stored against a customer profile.

`API reference <https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/cards/save-card/post>`_
"""
from mercadopago.core import MPBase


class Card(MPBase):
    """Manages saved payment cards linked to a :class:`Customer`.

    Storing cards lets returning buyers complete checkout without
    re-entering card details.  Every method requires the owning
    *customer_id*.
    """

    def list_all(self, customer_id, request_options=None):
        """Lists all cards saved for a customer.

        Args:
            customer_id: Owner customer identifier.
            request_options: Per-call configuration overrides.

        Returns:
            dict: List of saved card objects.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/cards/get-customer-cards/get
        """
        return self._get(
            uri=f"/v1/customers/{str(customer_id)}/cards",
            request_options=request_options,
        )

    def get(self, customer_id, card_id, request_options=None):
        """Retrieves a single saved card.

        Args:
            customer_id: Owner customer identifier.
            card_id: Identifier of the card to retrieve.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Full card object.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/cards/get-card/get
        """
        return self._get(
            uri=f"/v1/customers/{str(customer_id)}/cards/{str(card_id)}",
            request_options=request_options,
        )

    def create(self, customer_id, card_object, request_options=None):
        """Saves a new card for a customer.

        The *card_object* typically contains a ``token`` obtained via
        the MercadoPago JS SDK or Card Token API.

        Args:
            customer_id: Owner customer identifier.
            card_object: Dict with card data (``token`` is required).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *card_object* is not a ``dict``.

        Returns:
            dict: Created card including its ``id``.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/cards/save-card/post
        """
        if not isinstance(card_object, dict):
            raise ValueError("Param card_object must be a Dictionary")

        return self._post(uri="/v1/customers/" + str(customer_id)
                          + "/cards/", data=card_object, request_options=request_options)

    def update(self, customer_id, card_id, card_object, request_options=None):
        """Updates a saved card's details.

        Args:
            customer_id: Owner customer identifier.
            card_id: Identifier of the card to update.
            card_object: Dict with the fields to modify.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *card_object* is not a ``dict``.

        Returns:
            dict: Updated card object.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/cards/update-card/put
        """
        if not isinstance(card_object, dict):
            raise ValueError("Param card_object must be a Dictionary")

        return self._put(uri="/v1/customers/" + str(customer_id)
                         + "/cards/" + str(card_id), data=card_object,
                         request_options=request_options)

    def delete(self, customer_id, card_id, request_options=None):
        """Deletes a saved card from a customer profile.

        Args:
            customer_id: Owner customer identifier.
            card_id: Identifier of the card to delete.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Deletion confirmation response.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api/cards/delete-card/delete
        """
        return self._delete(uri="/v1/customers/" + str(customer_id)
                            + "/cards/" + str(card_id), request_options=request_options)
