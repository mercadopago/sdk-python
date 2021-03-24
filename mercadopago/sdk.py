"""
Module: sdk
"""
from mercadopago.resources import AdvancedPayment
from mercadopago.resources import CardToken
from mercadopago.resources import Card
from mercadopago.resources import Customer
from mercadopago.resources import DisbursementRefund
from mercadopago.resources import IdentificationType
from mercadopago.resources import MerchantOrder
from mercadopago.resources import PaymentMethods
from mercadopago.resources import Payment
from mercadopago.resources import PreApproval
from mercadopago.resources import Preference
from mercadopago.resources import Refund
from mercadopago.resources import User
from mercadopago.config import RequestOptions
from mercadopago.http import HttpClient

class SDK():

    """Generate access to all API' modules, which are:

        1. Advanced Payment
        2. Card Token
        3. Card
        4. Customer
        5. Disbursement Refund
        6. Identification Type
        7. Merchant Order
        8. Payment Methods
        9. Payment
        10. Preapproval
        11. Preference
        12. Refund
        13. User
    """

    def __init__(self,
                 access_token,
                 http_client=None,
                 request_options=None):

        """Construct ur SDK Object to have access to all APIs modules.
        Args:
            [Click here for more infos](https://www.mercadopago.com/mlb/account/credentials)
            http_client (mercadopago.http.http_client, optional): An implementation of
            HttpClient can be pass to be used to make the REST calls. Defaults to None.
            request_options (mercadopago.config.request_options, optional): An instance
            of RequestOptions can be pass changing or adding custom options to ur REST
            calls. Defaults to None.
        Raises:
            ValueError: Param request_options must be a RequestOptions Object
        """

        self.http_client = http_client
        if http_client is None:
            self.http_client = HttpClient()

        self.request_options = request_options
        if request_options is None:
            self.request_options = RequestOptions()

        self.request_options.access_token = access_token

    def advanced_payment(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return AdvancedPayment(request_options is not None and request_options
        or self.request_options, self.http_client)

    def card_token(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return CardToken(request_options is not None and request_options
        or self.request_options, self.http_client)

    def card(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return Card(request_options is not None and request_options
        or self.request_options, self.http_client)

    def customer(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return Customer(request_options is not None and request_options
        or self.request_options, self.http_client)

    def disbursement_refund(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return DisbursementRefund(request_options is not None and request_options
        or self.request_options, self.http_client)

    def identification_type(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return IdentificationType(request_options is not None and request_options
        or self.request_options, self.http_client)

    def merchant_order(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return MerchantOrder(request_options is not None and request_options
        or self.request_options, self.http_client)

    def payment(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return Payment(request_options is not None and request_options
        or self.request_options, self.http_client)

    def payment_methods(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return PaymentMethods(request_options is not None and request_options
        or self.request_options, self.http_client)

    def preapproval(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return PreApproval(request_options is not None and request_options
        or self.request_options, self.http_client)

    def preference(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return Preference(request_options is not None and request_options
        or self.request_options, self.http_client)

    def refund(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return Refund(request_options is not None and request_options
        or self.request_options, self.http_client)

    def user(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return User(request_options is not None and request_options
        or self.request_options, self.http_client)

    @property
    def request_options(self):
        """
        Sets the attribute value and validates request_options
        """
        return self.__request_options

    @request_options.setter
    def request_options(self, value):
        if value is not None and not isinstance(value, RequestOptions):
            raise ValueError("Param request_options must be a RequestOptions Object")
        self.__request_options = value

    @property
    def http_client(self):
        """
        Sets the attribute value and validates http_client
        """
        return self.__http_client

    @http_client.setter
    def http_client(self, value):
        if value is not None and not isinstance(value, HttpClient):
            raise ValueError("Param http_client must be a HttpClient Object")
        self.__http_client = value
