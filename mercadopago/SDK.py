from mercadopago.resources.card_token import CardToken
from mercadopago.resources.card import Card
from mercadopago.resources.customer import Customer
from mercadopago.resources.merchant_order import MerchantOrder
from mercadopago.resources.payment import Payment
from mercadopago.resources.preference import Preference
from mercadopago.resources.refund import Refund
from mercadopago.core.request_options import RequestOptions

class SDK():
    def __init__(self, access_token):
        self.__access_token = access_token

    def card_token(self):
        self.__validate_access_token()
        return CardToken(RequestOptions(access_token=self.access_token))

    def card(self):
        self.__validate_access_token()
        return Card(RequestOptions(access_token=self.access_token))

    def customer(self):
        self.__validate_access_token()
        return Customer(RequestOptions(access_token=self.access_token))

    def merchant_order(self):
        self.__validate_access_token()
        return MerchantOrder(RequestOptions(access_token=self.access_token))

    def payment(self):
        self.__validate_access_token()
        return Payment(RequestOptions(access_token=self.access_token))

    def preference(self):
        self.__validate_access_token()
        return Preference(RequestOptions(access_token=self.access_token))

    def refund(self):
        self.__validate_access_token()
        return Refund(RequestOptions(access_token=self.access_token))

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        self.__access_token = value

    def __validate_access_token(self):
        if self.access_token is None:
            raise Exception("An access_token must be informed")
        