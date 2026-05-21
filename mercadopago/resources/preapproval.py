"""PreApproval resource for the MercadoPago Subscriptions API.

Wraps ``/preapproval`` endpoints to search, retrieve, create, and update
preapproval (subscription) records without an associated plan.

`API reference
<https://www.mercadopago.com/developers/en/reference/online-payments/subscriptions/create-preapproval/post>`_
"""
from mercadopago.core import MPBase


class PreApproval(MPBase):
    """Manages plan-less (ad-hoc) subscriptions.

    Use this resource when you need full control over subscription terms
    per subscriber instead of using a shared :class:`Plan` template.
    """

    def __init__(self, request_options, http_client):
        MPBase.__init__(self, request_options, http_client)

    def search(self, filters=None, request_options=None):
        """Searches preapprovals matching the given filters.

        Args:
            filters: Query-string parameters.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Paginated list of matching preapprovals.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/subscriptions/search-preapproval/get
        """
        return self._get(uri="/preapproval/search", filters=filters,
                         request_options=request_options)

    def get(self, preapproval_id, request_options=None):
        """Retrieves a preapproval by its ID.

        Args:
            preapproval_id: Unique preapproval identifier.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Full preapproval object.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/subscriptions/get-preapproval/get
        """
        return self._get(uri="/preapproval/" + str(preapproval_id), request_options=request_options)

    def create(self, preapproval_object, request_options=None):
        """Creates a new preapproval (ad-hoc subscription).

        Args:
            preapproval_object: Dict defining the subscription (reason,
                auto_recurring, payer_email, back_url, etc.).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *preapproval_object* is not a ``dict``.

        Returns:
            dict: Created preapproval including its ``id`` and ``init_point``.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/subscriptions/create-preapproval/post
        """
        if not isinstance(preapproval_object, dict):
            raise ValueError("Param preapproval_object must be a Dictionary")

        return self._post(uri="/preapproval",
                          data=preapproval_object, request_options=request_options)

    def update(self, preapproval_id, preapproval_object, request_options=None):
        """Updates an existing preapproval.

        Args:
            preapproval_id: Identifier of the preapproval to update.
            preapproval_object: Dict with the fields to modify.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *preapproval_object* is not a ``dict``.

        Returns:
            dict: Updated preapproval object.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/subscriptions/update-preapproval/put
        """
        if not isinstance(preapproval_object, dict):
            raise ValueError("Param preapproval_object must be a Dictionary")

        return self._put(uri="/preapproval/" + str(preapproval_id),
                         data=preapproval_object, request_options=request_options)
