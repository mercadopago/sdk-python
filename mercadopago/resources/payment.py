"""Payment resource for the MercadoPago Checkout API.

Wraps ``/v1/payments`` endpoints to search, retrieve, create, and update
payments.

`API reference <https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api-payments/create-payment/post>`_
"""
from mercadopago.core import MPBase


class PaymentPayer:
    """Payer information for a payment.
    
    Attributes:
        email (str): Payer's email address.
        identification (dict): Document type and number.
        first_name (str): Payer's first name.
        last_name (str): Payer's last name.
    """
    pass


class PaymentAdditionalInfo:
    """Additional information for a payment.
    
    Attributes:
        items (list): List of items being purchased.
        payer (dict): Additional payer information.
        shipments (dict): Shipping information.
    """
    pass


class PaymentRequest:
    """Schema for creating a new payment.
    
    Attributes:
        transaction_amount (float, required): Amount to be paid.
        token (str): Card token for payment.
        payment_method_id (str): Payment method identifier.
        installments (int): Number of installments.
        issuer_id (str): Card issuer identifier.
        payer (PaymentPayer, required): Payer information.
        capture (bool): Whether to capture payment immediately (default: True).
        binary_mode (bool): Whether to use binary mode (default: False).
        external_reference (str): External reference for the payment.
        statement_descriptor (str): Text to appear on payer's statement (max 22 chars).
        date_of_expiration (datetime): Payment expiration date.
        additional_info (PaymentAdditionalInfo): Additional payment information.
        application_fee (float): Application fee amount.
        notification_url (str): URL for payment notifications (deprecated).
        callback_url (str): URL for payment callbacks.
        coupon_code (str): Discount coupon code.
        coupon_amount (float): Discount coupon amount.
    """
    pass


class Pagination:
    """Pagination information for search results.
    
    Attributes:
        total (int): Total number of results.
        limit (int): Maximum number of results per page.
        offset (int): Starting position in the result set.
    """
    pass


class Payment(MPBase):
    """Manages payment lifecycle through the MercadoPago Checkout API.

    Supports transparent (server-to-server) payments as well as payments
    originated from Checkout Pro / Checkout Bricks.

    `Integration guide
    <https://www.mercadopago.com.br/developers/en/guides/online-payments/checkout-api/introduction/>`_
    """

    def search(self, filters=None, request_options=None):
        """Searches payments matching the given filters.

        Args:
            filters: Query-string parameters such as ``external_reference``,
                ``status``, ``date_created``, etc.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Paginated list of matching payments.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api-payments/search-payments/get
        """
        return self._get(uri="/v1/payments/search", filters=filters,
                         request_options=request_options)

    def get(self, payment_id, request_options=None):
        """Retrieves a single payment by its ID.

        Args:
            payment_id: Numeric or string payment identifier.
            request_options: Per-call configuration overrides.

        Returns:
            dict: Full payment object.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api-payments/get-payment/get
        """
        return self._get(uri="/v1/payments/" + str(payment_id), request_options=request_options)

    def create(self, payment_object, request_options=None):
        """Creates a new payment.

        Args:
            payment_object: Dict describing the payment (transaction_amount, payer,
                payment_method_id, token, etc.). Must conform to PaymentRequest schema.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *payment_object* is not a ``dict``.

        Returns:
            dict: Created payment including its ``id`` and ``status``.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api-payments/create-payment/post
        """
        if not isinstance(payment_object, dict):
            raise ValueError("Param payment_object must be a Dictionary")

        return self._post(uri="/v1/payments", data=payment_object, request_options=request_options)

    def update(self, payment_id, payment_object, request_options=None):
        """Updates an existing payment.

        Commonly used to change ``status`` (e.g. cancel) or update
        metadata on a payment that has not yet been captured.

        Args:
            payment_id: Identifier of the payment to update.
            payment_object: Dict with the fields to modify.
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *payment_object* is not a ``dict``.

        Returns:
            dict: Updated payment object.

        Reference: https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api-payments/update-payment/put
        """
        if not isinstance(payment_object, dict):
            raise ValueError("Param payment_object must be a Dictionary")

        return self._put(uri="/v1/payments/" + str(payment_id), data=payment_object,
                         request_options=request_options)