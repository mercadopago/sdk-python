#from mercadopago.resources.payment import Payment
#from .resources.preference import Preference

""" class SDK(object):
    
    def __init__(self):
        pass
        
    def setAccessToken(self, accessToken):
        self.accessToken = accessToken    
        self.Payment = Payment(self)
        #self.Preference = Preference(self)
        return self

    def getAcessToken(self):
        return self.accessToken """


class Sdk():
    def __init__(self, accessToken):
        self.accessToken = accessToken

    @property
    def accessToken(self):
        return self.__accessToken

    @accessToken.setter
    def accessToken(self, value):
        self.__accessToken = value

