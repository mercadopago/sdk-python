Looking at this change request, I need to update the `payment.py` file to document the new PaymentRequest schema. Since this is a Python SDK wrapper file, the actual schema enforcement happens on the API side, but I should update the documentation to reflect the new fields.

Here's the updated file:

```python
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
            payment_object: Dict describing the payment with the following fields:
                
                **Required fields:**
                - transaction_amount (float): The total amount to charge.
                - payer (dict): PaymentPayer object with payer information.
                
                **Optional fields:**
                - token (string): Card token for card payments.
                - payment_method_id (string): Payment method identifier.
                - installments (integer): Number of installments.
                - issuer_id (string): Card issuer identifier.
                - capture (boolean): Whether to capture immediately (default: True).
                - binary_mode (boolean): Binary payment mode (default: False).
                - external_reference (string): Your internal reference.
                - statement_descriptor (string): Text on card statement (max 22 chars).
                - date_of_expiration (datetime): Payment expiration date.
                - additional_info (dict): PaymentAdditionalInfo object.
                - application_fee (float): Application fee amount.
                - notification_url (uri): IPN notification URL (deprecated).
                - callback_url (uri): Redirect URL after payment.
                - coupon_code (string): Discount coupon code.
                - coupon_amount (float): Coupon discount amount.
                
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
```

**Key changes made:**

1. **Updated `create()` method documentation** to reflect the new PaymentRequest schema:
   - Removed references to old fields (amount, currency, customer_id, merchant_id, payment_method)
   - Added comprehensive documentation for all new fields
   - Clearly marked required fields: `transaction_amount` and `payer`
   - Listed all optional fields with their types and constraints
   - Noted the `notification_url` deprecation
   - Included field constraints (e.g., statement_descriptor max 22 chars, boolean defaults)

2. **Preserved all method signatures** since the SDK is a thin wrapper and validation happens server-side

3. **Maintained backward compatibility** in the code structure while updating documentation to guide developers toward the new API contract