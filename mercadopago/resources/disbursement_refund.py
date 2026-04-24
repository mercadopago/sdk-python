"""Disbursement Refund resource for the MercadoPago Marketplace API.

Wraps ``/v1/advanced_payments/{id}/refunds`` and
``/v1/advanced_payments/{id}/disbursements/{id}/refunds`` endpoints
to refund individual or all disbursements within an advanced payment.
"""
from mercadopago.core import MPBase


class DisbursementRefund(MPBase):
    """Refunds disbursements from advanced (split) payments.

    In marketplace flows each seller receives a disbursement.  This
    resource lets you refund all disbursements at once, a single
    disbursement by amount, or a disbursement with a custom refund body.
    """

    def list_all(self, advanced_payment_id, request_options=None):
        """Lists all refunds for an advanced payment.

        Args:
            advanced_payment_id: Identifier of the advanced payment.
            request_options: Per-call configuration overrides.

        Returns:
            dict: List of disbursement refund objects.
        """
        uri = f"/v1/advanced_payments/{str(advanced_payment_id)}/refunds"
        return self._get(uri=uri, request_options=request_options)

    def create_all(self, advanced_payment_id, disbursement_refund_object, request_options=None):
        """Refunds all disbursements of an advanced payment at once.

        Args:
            advanced_payment_id: Identifier of the advanced payment.
            disbursement_refund_object: Dict with refund details applied
                to every disbursement.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *disbursement_refund_object* is not a ``dict``.

        Returns:
            dict: Bulk refund creation response.
        """
        if not isinstance(disbursement_refund_object, dict):
            raise ValueError(
                "Param disbursement_refund_object must be a Dictionary")

        return self._post(
            uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/refunds",
            data=disbursement_refund_object,
            request_options=request_options,
        )

    def create(self, advanced_payment_id, disbursement_id, amount, request_options=None):
        """Refunds a specific disbursement by amount.

        Args:
            advanced_payment_id: Identifier of the parent advanced payment.
            disbursement_id: Identifier of the disbursement to refund.
            amount: Refund amount as a ``float``.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *amount* is not a ``float``.

        Returns:
            dict: Created disbursement refund.
        """
        if not isinstance(amount, float):
            raise ValueError("Param amount must be a Float")

        disbursement_refund_object = {"amount": amount}

        uri = (
            f"/v1/advanced_payments/{str(advanced_payment_id)}"
            f"/disbursements/{str(disbursement_id)}/refunds"
        )

        return self._post(
            uri=uri,
            data=disbursement_refund_object,
            request_options=request_options,
        )

    def save(self, advanced_payment_id, disbursement_id, disbursement_refund_object,
             request_options=None):
        """Creates a disbursement refund with a custom body.

        Unlike :meth:`create`, which only accepts an amount, this method
        lets you pass an arbitrary refund payload.

        Args:
            advanced_payment_id: Identifier of the parent advanced payment.
            disbursement_id: Identifier of the disbursement to refund.
            disbursement_refund_object: Dict with full refund details.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *disbursement_refund_object* is not a ``dict``.

        Returns:
            dict: Created disbursement refund.
        """
        if not isinstance(disbursement_refund_object, dict):
            raise ValueError(
                "Param disbursement_refund_object must be a Dictionary")

        uri = (
            f"/v1/advanced_payments/{str(advanced_payment_id)}"
            f"/disbursements/{str(disbursement_id)}/refunds"
        )

        return self._post(
            uri=uri,
            data=disbursement_refund_object,
            request_options=request_options,
        )
