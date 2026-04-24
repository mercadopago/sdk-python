"""Plan resource for the MercadoPago Subscriptions API.

Wraps ``/preapproval_plan`` endpoints to search, retrieve, create, and
update subscription plans.  Plans serve as reusable templates that
define billing frequency, amount, and duration for subscriptions.

`API reference
<https://www.mercadopago.com/developers/en/reference/subscriptions/>`_
"""
from mercadopago.core import MPBase


class Plan(MPBase):
    """Manages subscription plan templates.

    Create a plan once and then attach multiple
    :class:`~mercadopago.resources.subscription.Subscription` instances
    to it so that all subscribers share the same billing terms.
    """

    def search(self, filters=None, request_options=None):
        """Searches plans matching the given filters.

        Args:
            filters: Query-string parameters.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Paginated list of matching plans.
        """
        return self._get(
            uri="/preapproval_plan/search",
            filters=filters,
            request_options=request_options)

    def get(self, plan_id, request_options=None):
        """Retrieves a plan by its ID.

        Args:
            plan_id: Unique plan identifier.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Full plan object.
        """
        return self._get(
            uri="/preapproval_plan/" + str(plan_id),
            request_options=request_options)

    def create(self, plan_object, request_options=None):
        """Creates a new subscription plan.

        Args:
            plan_object: Dict defining the plan (reason,
                auto_recurring frequency/amount, back_url, etc.).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *plan_object* is not a ``dict``.

        Returns:
            dict: Created plan including its ``id`` and ``init_point``.
        """
        if not isinstance(plan_object, dict):
            raise ValueError("Param plan_object must be a Dictionary")

        return self._post(
            uri="/preapproval_plan",
            data=plan_object,
            request_options=request_options)

    def update(self, plan_id, plan_object, request_options=None):
        """Updates an existing plan.

        Args:
            plan_id: Identifier of the plan to update.
            plan_object: Dict with the fields to modify.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *plan_object* is not a ``dict``.

        Returns:
            dict: Updated plan object.
        """
        if not isinstance(plan_object, dict):
            raise ValueError("Param plan_object must be a Dictionary")

        return self._put(
            uri="/preapproval_plan/" + str(plan_id),
            data=plan_object,
            request_options=request_options)
