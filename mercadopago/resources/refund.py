"""Refund resource for the MercadoPago Payments API.

Wraps ``/v1/payments/{payment_id}/refunds`` endpoints to list existing
refunds and create full or partial refunds on approved payments.

Refunds are available within 180 days of payment approval and require
sufficient account balance.

`API reference <https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api-payments/create-refund/post>`_
"""
from mercadopago.core import MPBase


class Refund(MPBase):
    """Creates and lists refunds for payments.

    Supports full refunds (omit *amount*) and partial refunds
    (pass ``{"amount": <float>}``).  Refunds can only be issued for
    approved payments within 180 days.
    """

    def list_all(self, payment_id, request_options=None):
        """Lists all refunds issued for a payment.

        Args:
            payment_id: Identifier of the parent payment.
            request_options: Per-call configuration overrides.

        Returns:
            dict: List of refund objects.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api-payments/get-refunds/get
        """
        return self._get(uri="/v1/payments/" + str(payment_id) + "/refunds",
                         request_options=request_options)

    def create(self, payment_id, amount=None, request_options=None):
        """Creates a refund for a payment.

        Omit *amount* for a full refund, or pass a float value
        for a partial refund.

        Args:
            payment_id: Identifier of the payment to refund.
            amount: Optional float with partial refund amount.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *amount* is provided but not a valid number.

        Returns:
            dict: Created refund including its ``id`` and ``status``.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api-payments/create-refund/post
        """
        refund_data = None
        if amount is not None:
            if not isinstance(amount, (int, float)):
                raise ValueError("Param amount must be a number")
            refund_data = {"amount": float(amount)}

        return self._post(uri="/v1/payments/" + str(payment_id) + "/refunds",
                          data=refund_data, request_options=request_options)