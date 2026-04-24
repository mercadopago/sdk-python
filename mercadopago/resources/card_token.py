"""Card Token resource for the MercadoPago API.

Wraps ``/v1/card_tokens`` endpoints to tokenise raw card data
server-side before creating a payment.  The returned token is
single-use and short-lived.
"""
from mercadopago.core import MPBase


class CardToken(MPBase):
    """Tokenises card data for secure payment creation.

    Send raw card details (number, expiry, CVV) to obtain a one-time
    token that can be passed to :meth:`Payment.create` without
    exposing sensitive data in your own backend.
    """

    def get(self, card_token_id, request_options=None):
        """Retrieves a card token by its ID.

        Args:
            card_token_id: Unique token identifier.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Token metadata (last four digits, expiry, etc.).
        """
        return self._get(uri="/v1/card_tokens/" + str(card_token_id),
                         request_options=request_options)

    def create(self, card_token_object, request_options=None):
        """Creates a new card token from raw card data.

        Args:
            card_token_object: Dict with card details (card_number,
                expiration_month, expiration_year, security_code, etc.).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *card_token_object* is not a ``dict``.

        Returns:
            dict: Created token including its ``id``.
        """
        if not isinstance(card_token_object, dict):
            raise ValueError("Param card_token_object must be a Dictionary")

        return self._post(uri="/v1/card_tokens", data=card_token_object,
                          request_options=request_options)
