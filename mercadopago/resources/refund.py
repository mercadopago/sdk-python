from mercadopago.core.mp_base import MPBase

class Refund(MPBase):
    def __init__(self, request_options):
        super(Refund, self).__init__(request_options)

    