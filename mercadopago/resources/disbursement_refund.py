from mercadopago.core.mp_base import MPBase

class DisbursementRefund(MPBase):
    def __init__(self, request_options):
        super(DisbursementRefund, self).__init__(request_options)

    def find_all(self, advanced_payment_id, request_options=None):
        return self._get(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/refunds/", request_options=request_options)

    def create(self):
        pass

    def create_all(self):
        pass
    
    def save(self, advanced_payment_id, disbursement_id, request_options=None):
        return self._post(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/disbursements/" + str(disbursement_id) + "/refunds", request_options=request_options)
