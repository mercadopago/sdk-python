"""Payment resource for the MercadoPago Checkout API.

Wraps ``/v1/payments`` endpoints to search, retrieve, create, and update
payments.

`API reference <https://www.mercadopago.com/developers/en/reference/online-payments/checkout-api-payments/create-payment/post>`_
"""
from mercadopago.core import MPBase


class Payment(MPBase):
    """Manages payment lifecycle through the MercadoPago Checkout API.

    Supports transparent (server-to-server) payments as well as payments
    originated from Checkout Pro / Checkout Bricks.

    The :meth:`create` method accepts a payment request with the following
    required fields:

    - ``transaction_amount`` (float): The total transaction amount.
    - ``payer`` (dict): Payer information including email and optional
      identification details.

    Optional fields include:

    - ``token`` (str): Tokenized card data obtained from the Card Token API
      or MercadoPago JS SDK.
    - ``payment_method_id`` (str): Payment method identifier (e.g. "visa",
      "master", "pix").
    - ``installments`` (int): Number of installments for card payments.
    - ``description`` (str): Payment description.
    - ``external_reference`` (str): Your internal reference for this payment.

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

        The payment request must include:

        - ``transaction_amount`` (float, required): Total amount to charge.
        - ``payer`` (dict, required): Payer details with at minimum an
          ``email`` field.

        Additional common fields:

        - ``token`` (str): Card token for credit/debit card payments.
        - ``payment_method_id`` (str): Payment method (e.g. "visa", "pix").
        - ``installments`` (int): Number of installments.
        - ``description`` (str): Payment description.
        - ``external_reference`` (str): Merchant's reference identifier.

        Example::

            payment_object = {
                "transaction_amount": 100.50,
                "token": "card_token_id",
                "payment_method_id": "visa",
                "installments": 1,
                "payer": {
                    "email": "buyer@example.com",
                    "identification": {
                        "type": "CPF",
                        "number": "12345678909"
                    }
                },
                "description": "Product purchase"
            }
            result = sdk.payment().create(payment_object)

        Args:
            payment_object: Dict describing the payment. Must contain
                ``transaction_amount`` (float) and ``payer`` (dict).
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