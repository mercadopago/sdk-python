"""
Module: sdk
"""
from mercadopago.resources.advanced_payment import AdvancedPayment
from mercadopago.resources.card_token import CardToken
from mercadopago.resources.card import Card
from mercadopago.resources.customer import Customer
from mercadopago.resources.disbursement_refund import DisbursementRefund
from mercadopago.resources.identification_type import IdentificationType
from mercadopago.resources.merchant_order import MerchantOrder
from mercadopago.resources.payment_methods import PaymentMethods
from mercadopago.resources.payment import Payment
from mercadopago.resources.preference import Preference
from mercadopago.resources.refund import Refund
from mercadopago.resources.user import User
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
                 corporation_id=None,
                 integrator_id=None,
                 platform_id=None,
                 http_client=None,
                 request_options=None):

        """Construct ur SDK Object to have access to all APIs modules.
        Args:
            access_token (str): Your access token to the MercadoPago APIs.
            [Click here for more infos](https://www.mercadopago.com/mlb/account/credentials)
            corporation_id (str, optional): Your Corporation ID if any. Defaults to None.
            integrator_id (str, optional): Your Integrator ID if any. Defaults to None.
            platform_id (str, optional): Your Platform ID if any. Defaults to None.
            http_client (mercadopago.http.http_client, optional): An implementation of
            HttpClient can be pass to be used to make the REST calls. Defaults to None.
            request_options (mercadopago.config.request_options, optional): An instance
            of RequestOptions can be pass changing or adding custom options to ur REST
            calls. Defaults to None.

        Raises:
            ValueError: Param access_token must be a String
            ValueError: Param request_options must be a RequestOptions Object
            ValueError: Param corporation_id must be a String
            ValueError: Param integrator_id must be a String
            ValueError: Param platform_Id must be a String
        """
        self.__access_token = access_token
        self.__corporation_id = corporation_id
        self.__integrator_id = integrator_id
        self.__platform_id = platform_id
        if self.__http_client is None and HttpClient() or http_client is not None:
            self.__http_client = self.http_client
        if self.request_options is None and RequestOptions() or request_options is not None:
            self.request_options = self.request_options

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
    def access_token(self):
        """
        Sets the attribute value and validates access_token
        """
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        if not isinstance(value, str):
            raise ValueError('Param access_token must be a String')
        self.__access_token = value

    @property
    def request_options(self):
        """
        Sets the attribute value and validates request_options
        """
        if self.__request_options.access_token is None:
            self.__request_options.access_token = self.access_token

        if self.__request_options.corporation_id is None and self.corporation_id is not None:
            self.__request_options.corporation_id = self.corporation_id

        if self.__request_options.integrator_id is None and self.integrator_id is not None:
            self.__request_options.integrator_id = self.integrator_id

        if self.__request_options.platform_id is None and self.platform_id is not None:
            self.__request_options.platform_id = self.platform_id

        return self.__request_options

    @request_options.setter
    def request_options(self, value):
        if not isinstance(value, RequestOptions):
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
        self.__http_client = value

    @property
    def corporation_id(self):
        """
        Sets the attribute value and validates corporation_id
        """
        return self.__corporation_id

    @corporation_id.setter
    def corporation_id(self, value):
        if not isinstance(value, str):
            raise ValueError('Param corporation_id must be a String')
        self.__corporation_id = value

    @property
    def integrator_id(self):
        """
        Sets the attribute value and validates integrator_id
        """
        return self.__integrator_id

    @integrator_id.setter
    def integrator_id(self, value):
        if not isinstance(value, str):
            raise ValueError('Param integrator_id must be a String')
        self.__integrator_id = value

    @property
    def platform_id(self):
        """
        Sets the attribute value and validates platform_id
        """
        return self.__platform_id

    @platform_id.setter
    def platform_id(self, value):
        if not isinstance(value, str):
            raise ValueError('Param platform_id must be a String')
        self.__platform_id = value
        