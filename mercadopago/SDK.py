from mercadopago.resources import *
from mercadopago.config import RequestOptions
from mercadopago.http import HttpClient

class SDK():

    """
    Generate access to all API' modules, which are:

    1. Advanced Payment
    2. Card Token
    3. Card
    4. Customer
    5. Disbursement Refund
    6. Identification Type
    7. Merchant Order
    8. PaymentMethods
    9. Payment
    10. Preference
    11. Refund
    12. User
    """

    def __init__(self, 
                    access_token, 
                    corporation_id=None,
                    http_client=None, 
                    request_options=None):
        """Construct ur SDK Object to have access to all APIs modules.

        Args:
            access_token (str): Your access token to the MercadoPago APIs. [Click here for more infos](https://www.mercadopago.com/mlb/account/credentials)
            http_client (mercadopago.http.http_client, optional): An implementation of HttpClient can be pass to be used to make the REST calls. Defaults to None.
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST calls. Defaults to None.
        """
        self.__access_token = access_token
        self.__corporation_id = corporation_id
        self.__http_client = http_client is None and HttpClient() or http_client
        self.request_options = request_options is None and RequestOptions() or request_options

    def advanced_payment(self):
        return AdvancedPayment(self.request_options, self.http_client)

    def card_token(self):
        return CardToken(self.request_options, self.http_client)

    def card(self):
        return Card(self.request_options, self.http_client)

    def customer(self):
        return Customer(self.request_options, self.http_client)

    def disbursement_refund(self):
        return DisbursementRefund(self.request_options, self.http_client)

    def identification_type(self):
        return IdentificationType(self.request_options, self.http_client)

    def merchant_order(self):
        return MerchantOrder(self.request_options, self.http_client)

    def payment(self):
        return Payment(self.request_options, self.http_client)

    def payment_methods(self):
        return PaymentMethods(self.request_options, self.http_client)

    def preference(self):
        return Preference(self.request_options, self.http_client)

    def refund(self):
        return Refund(self.request_options, self.http_client)

    def user(self):
        return User(self.request_options, self.http_client)

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        if type(value) is not str:
            raise ValueError('Param access_token must be a String')
        self.__access_token = value

    @property
    def request_options(self):
        if self.__request_options.access_token is None:
            self.__request_options.access_token = self.access_token

        if self.__request_options.corporation_id is None and self.corporation_id is not None:
            self.__request_options.corporation_id = self.corporation_id
        
        return self.__request_options

    @request_options.setter
    def request_options(self, value):
        if type(value) is not RequestOptions:
            raise ValueError('Param request_options must be a RequestOptions Object')
        self.__request_options = value

    @property
    def http_client(self):
        return self.__http_client

    @http_client.setter
    def http_client(self, value):
        self.__http_client = value

    @property
    def corporation_id(self):
        return self.__corporation_id

    @corporation_id.setter
    def corporation_id(self, value):
        if type(value) is not str:
            raise ValueError('Param corporation_id must be a String')
        self.__corporation_id = value