"""Main entry point for the MercadoPago Python SDK.

Instantiate :class:`SDK` with an access token to obtain factory methods
for every MercadoPago API resource (payments, orders, customers, etc.).

Example::

    import mercadopago

    sdk = mercadopago.SDK("YOUR_ACCESS_TOKEN")
    result = sdk.payment().create({
        "transaction_amount": 100,
        "payment_method_id": "pix",
        "payer": {"email": "buyer@example.com"},
    })
"""
from mercadopago.config import RequestOptions
from mercadopago.http import HttpClient
from mercadopago.resources import (
    AdvancedPayment,
    Card,
    CardToken,
    Chargeback,
    Customer,
    DisbursementRefund,
    IdentificationType,
    Invoice,
    MerchantOrder,
    OAuth,
    Order,
    Payment,
    PaymentMethods,
    Plan,
    Point,
    PreApproval,
    Preference,
    Refund,
    Subscription,
    User,
)


class SDK:
    """Central client providing factory methods for every API resource.

    Each factory method (e.g. :meth:`payment`, :meth:`order`) returns a
    fresh resource instance bound to the SDK's credentials and HTTP
    client.  An optional *request_options* argument lets callers override
    configuration on a per-resource basis.

    Attributes:
        request_options: Default :class:`RequestOptions` applied to all
            resource instances unless overridden.
        http_client: :class:`HttpClient` used for every outgoing request.
    """

    def __init__(
        self,
        access_token,
        http_client=None,
        request_options=None,
    ):
        """Initialises the SDK with authentication credentials.

        Args:
            access_token: OAuth access token obtained from the
                `MercadoPago credentials page
                <https://www.mercadopago.com/mlb/account/credentials>`_.
            http_client: Custom :class:`HttpClient` implementation.
                Defaults to the built-in ``requests``-based client.
            request_options: Default :class:`RequestOptions` (timeout,
                retries, custom headers).  A new instance is created
                if not provided.

        Raises:
            ValueError: If *request_options* is not a
                :class:`RequestOptions` instance.
            ValueError: If *http_client* is not an :class:`HttpClient`
                instance.
        """

        self.http_client = http_client
        if http_client is None:
            self.http_client = HttpClient()

        self.request_options = request_options
        if request_options is None:
            self.request_options = RequestOptions()

        self.request_options.access_token = access_token

    def advanced_payment(self, request_options=None):
        """Creates an :class:`AdvancedPayment` resource for marketplace split payments."""
        return AdvancedPayment(request_options is not None and request_options
                               or self.request_options, self.http_client)

    def card_token(self, request_options=None):
        """Creates a :class:`CardToken` resource for server-side card tokenisation."""
        return CardToken(request_options is not None and request_options
                         or self.request_options, self.http_client)

    def card(self, request_options=None):
        """Creates a :class:`Card` resource to manage saved customer cards."""
        return Card(request_options is not None and request_options
                    or self.request_options, self.http_client)

    def customer(self, request_options=None):
        """Creates a :class:`Customer` resource to manage buyer profiles."""
        return Customer(request_options is not None and request_options
                        or self.request_options, self.http_client)

    def disbursement_refund(self, request_options=None):
        """Creates a :class:`DisbursementRefund` resource for advanced-payment refunds."""
        return DisbursementRefund(request_options is not None and request_options
                                  or self.request_options, self.http_client)

    def identification_type(self, request_options=None):
        """Creates an :class:`IdentificationType` resource to list accepted document types."""
        return IdentificationType(request_options is not None and request_options
                                  or self.request_options, self.http_client)

    def invoice(self, request_options=None):
        """Creates an :class:`Invoice` resource to retrieve subscription billing invoices."""
        return Invoice(request_options is not None and request_options
                       or self.request_options, self.http_client)

    def oauth(self, request_options=None):
        """Creates an :class:`OAuth` resource for the OAuth 2.0 authorization code flow."""
        return OAuth(request_options is not None and request_options
                     or self.request_options, self.http_client)

    def point(self, request_options=None):
        """Creates a :class:`Point` resource for in-person payments via Point devices."""
        return Point(request_options is not None and request_options
                     or self.request_options, self.http_client)

    def merchant_order(self, request_options=None):
        """Creates a :class:`MerchantOrder` resource for Checkout Pro orders."""
        return MerchantOrder(request_options is not None and request_options
                             or self.request_options, self.http_client)

    def order(self, request_options=None):
        """Creates an :class:`Order` resource for the Orders API."""
        return Order(request_options is not None and request_options
                       or self.request_options, self.http_client)

    def payment(self, request_options=None):
        """Creates a :class:`Payment` resource for the Checkout API."""
        return Payment(request_options is not None and request_options
                       or self.request_options, self.http_client)

    def payment_methods(self, request_options=None):
        """Creates a :class:`PaymentMethods` resource to list available payment methods."""
        return PaymentMethods(request_options is not None and request_options
                              or self.request_options, self.http_client)

    def preapproval(self, request_options=None):
        """Creates a :class:`PreApproval` resource for ad-hoc subscriptions."""
        return PreApproval(request_options is not None and request_options
                           or self.request_options, self.http_client)

    def preference(self, request_options=None):
        """Creates a :class:`Preference` resource for Checkout Pro sessions."""
        return Preference(request_options is not None and request_options
                          or self.request_options, self.http_client)

    def refund(self, request_options=None):
        """Creates a :class:`Refund` resource for payment refunds."""
        return Refund(request_options is not None and request_options
                      or self.request_options, self.http_client)

    def user(self, request_options=None):
        """Creates a :class:`User` resource to retrieve the authenticated account."""
        return User(request_options is not None and request_options
                    or self.request_options, self.http_client)

    def chargeback(self, request_options=None):
        """Creates a :class:`Chargeback` resource to monitor disputes."""
        return Chargeback(request_options is not None and request_options
                          or self.request_options, self.http_client)

    def subscription(self, request_options=None):
        """Creates a :class:`Subscription` resource for plan-based recurring billing."""
        return Subscription(request_options is not None and request_options
                            or self.request_options, self.http_client)

    def plan(self, request_options=None):
        """Creates a :class:`Plan` resource for subscription plan templates."""
        return Plan(request_options is not None and request_options
                    or self.request_options, self.http_client)

    @property
    def request_options(self):
        """Default :class:`RequestOptions` applied to all resource instances."""
        return self.__request_options

    @request_options.setter
    def request_options(self, value):
        if value is not None and not isinstance(value, RequestOptions):
            raise ValueError(
                "Param request_options must be a RequestOptions Object")
        self.__request_options = value

    @property
    def http_client(self):
        """HTTP transport used for all outgoing API requests."""
        return self.__http_client

    @http_client.setter
    def http_client(self, value):
        if value is not None and not isinstance(value, HttpClient):
            raise ValueError("Param http_client must be a HttpClient Object")
        self.__http_client = value
