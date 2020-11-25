from mercadopago.core.mp_base import MPBase

class DiscountCampaign(MPBase):
    def __init__(self, request_options):
        super(DiscountCampaign, self).__init__(request_options)

    def find(self, transaction_amount, payer_email, coupon_code, request_options=None):
        if type(transaction_amount) is not float:
            raise("Transaction Amount must be a Float")
        if type(payer_email) is not str:
            raise("Payer Email must be a String")
        if type(coupon_code) is not str:
            raise("Coupon Code must be a String")

        return self._get(uri="/v1/discount_campaigns/", request_options=request_options)

