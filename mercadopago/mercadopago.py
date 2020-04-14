from .mpinvalidcredentials import MPInvalidCredentials

from .card import Card
from .cardtoken import CardToken
from .customer import Customer
from .payment import Payment
from .preference import Preference
from .genericcall import GenericCall
from .discountcampaign import DiscountCampaign
from .identificationtype import IdentificationType
from .merchantorder import MerchantOrder


class MP(object):
    version = "2.0.4"
    __client_id = None
    __client_secret = None
    __ll_access_token = None
    __sandbox = False
    card = None
    cardtoken = None
    customer = None
    payment = None
    preference = None
    genericcall = None
    discountcampaign = None
    identificationtype = None
    merchantorder = None

    def __init__(self, *args):
        """
        Instantiate MP with credentials:
        mp = mercadopago.MP(client_id, client_secret)

        Instantiate MP with Long Live Access Token:
        mp = mercadopago.MP(ll_access_token)
        """
        if len(args) == 2:
            self.__client_id = args[0]
            self.__client_secret = args[1]
        elif len(args) == 1:
            self.__ll_access_token = args[0]
        else:
            raise MPInvalidCredentials(None)

        self.card = Card(self.__client_id, self.__client_secret, self.__ll_access_token, self.version)
        self.cardtoken = CardToken(self.__client_id, self.__client_secret, self.__ll_access_token, self.version)
        self.customer = Customer(self.__client_id, self.__client_secret, self.__ll_access_token, self.version)
        self.payment = Payment(self.__client_id, self.__client_secret, self.__ll_access_token, self.version)
        self.preference = Preference(self.__client_id, self.__client_secret, self.__ll_access_token, self.version)
        self.genericcall = GenericCall(self.__client_id, self.__client_secret, self.__ll_access_token, self.version)
        self.discountcampaign = DiscountCampaign(self.__client_id, self.__client_secret, self.__ll_access_token, self.version)
        self.identificationtype = IdentificationType(self.__client_id, self.__client_secret, self.__ll_access_token, self.version)
        self.merchantorder = MerchantOrder(self.__client_id, self.__client_secret, self.__ll_access_token, self.version)

    def sandbox_mode(self, enable=None):
        if not enable is None:
            self.__sandbox = enable == True

        return self.__sandbox
