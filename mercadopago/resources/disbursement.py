from mercadopago.core.mp_base import MPBase

class Disbursement(MPBase):
    def __init__(self, request_options):
        super(Disbursement, self).__init__(request_options)

    #TODO release_date ??
    def update_release_date(self, advanced_payment_id, disbursement_id, release_date, request_options=None):
        return self._post(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/disbursements/" + str(disbursement_id) + "/disburses", request_options=request_options)

