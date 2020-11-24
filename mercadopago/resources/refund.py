from mercadopago.core.MPBase import MPBase
from mercadopago.core.RequestOptions import RequestOptions

#TODO REFUND (PAYMENT)

class Refund(Base):

    def __init__(self):
        pass

    def setPaymentId(self, paymentId):
        self.paymentId = paymentId
        return self

    def getPaymentId(self):
        return self.paymentId

    def setAmount(self, amount):
        self.amount = amount
        return self

    def getAmount(self):
        return self.amount    

    def save(self, requestOptions):
        return self, RequestOptions.createDefault()


    #TODO INCLUIR OS DEMAIS MÉTODOS
    