"""Payment Methods resource for the MercadoPago API.

Wraps the ``/v1/payment_methods`` endpoint to list the payment methods
available for the authenticated account (credit cards, debit cards,
bank transfers, cash, etc.).
"""
from mercadopago.core import MPBase


class PaymentMethods(MPBase):
    """Lists payment methods available to the authenticated seller.

    The returned list varies by country and account configuration.  Use
    it to display accepted payment options in your checkout UI.
    """

    def list_all(self, request_options=None):
        """Retrieves all available payment methods.

        Args:
            request_options: Per-call configuration overrides.

        Returns:
            dict: List of payment method objects (id, name, type,
            status, thumbnail, etc.).
        """
        return self._get(uri="/v1/payment_methods", request_options=request_options)

    @property
    def request_options(self):
        """Default :class:`RequestOptions` for this resource instance."""
        return self.__request_options
