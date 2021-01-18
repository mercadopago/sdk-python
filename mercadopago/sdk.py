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
        10. Preference
        11. Refund
        12. User
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

        self.http_client = http_client #ISSO É UMA VERDADE | SE ELE MANDOU É A VERDADE
        if http_client is None:
            self.http_client = HttpClient()

        self.request_options = request_options
        if request_options is None:
            self.request_options = RequestOptions()

        self.request_options.access_token = access_token

    def advanced_payment(self):
        """
        Returns the attribute value of the function
        """
        return AdvancedPayment(self.request_options, self.http_client)

    def card_token(self):
        """
        Returns the attribute value of the function
        """
        return CardToken(self.request_options, self.http_client)

    def card(self):
        """
        Returns the attribute value of the function
        """
        return Card(self.request_options, self.http_client)

    def customer(self):
        """
        Returns the attribute value of the function
        """
        return Customer(self.request_options, self.http_client)

    def disbursement_refund(self):
        """
        Returns the attribute value of the function
        """
        return DisbursementRefund(self.request_options, self.http_client)

    def identification_type(self):
        """
        Returns the attribute value of the function
        """
        return IdentificationType(self.request_options, self.http_client)

    def merchant_order(self):
        """
        Returns the attribute value of the function
        """
        return MerchantOrder(self.request_options, self.http_client)

    def payment(self):
        """
        Returns the attribute value of the function
        """
        return Payment(self.request_options, self.http_client)

    def payment_methods(self):
        """
        Returns the attribute value of the function
        """
        return PaymentMethods(self.request_options, self.http_client)

    def preference(self):
        """
        Returns the attribute value of the function
        """
        return Preference(self.request_options, self.http_client)

    def refund(self):
        """
        Returns the attribute value of the function
        """
        return Refund(self.request_options, self.http_client)

    def user(self):
        """
        Returns the attribute value of the function
        """
        return User(self.request_options, self.http_client)

    @property
    def request_options(self):
        """
        Sets the attribute value and validates request_options
        """
        return self.__request_options

    @request_options.setter
    def request_options(self, value):
        if value is not None and not isinstance(value, RequestOptions):
            raise ValueError('Param request_options must be a RequestOptions Object')
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
            raise ValueError('Param http_client must be a HttpClient Object')
        self.__http_client = value
