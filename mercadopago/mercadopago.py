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
    version = "2.0.0"
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

        self.card = Card(self.__client_id, self.__client_secret, self.__ll_access_token)
        self.cardtoken = CardToken(self.__client_id, self.__client_secret, self.__ll_access_token)
        self.customer = Customer(self.__client_id, self.__client_secret, self.__ll_access_token)
        self.payment = Payment(self.__client_id, self.__client_secret, self.__ll_access_token)
        self.preference = Preference(self.__client_id, self.__client_secret, self.__ll_access_token)
        self.genericcall = GenericCall(self.__client_id, self.__client_secret, self.__ll_access_token)
        self.discountcampaign = DiscountCampaign(self.__client_id, self.__client_secret, self.__ll_access_token)
        self.identificationtype = IdentificationType(self.__client_id, self.__client_secret, self.__ll_access_token)
        self.merchantorder = MerchantOrder(self.__client_id, self.__client_secret, self.__ll_access_token)

    def sandbox_mode(self, enable=None):
        if not enable is None:
            self.__sandbox = enable == True

        return self.__sandbox
