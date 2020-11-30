from mercadopago.core import MPBase

class DisbursementRefund(MPBase):

    """
    gdfbdgh
    """
    
    def __init__(self, request_options, http_client):
        super(DisbursementRefund, self).__init__(request_options, http_client)

    def find_all(self, advanced_payment_id, request_options=None):
        return self._get(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/refunds", request_options=request_options)

    def create_all(self, advanced_payment_id, disbursement_refund_object, request_options=None):
        if type(disbursement_refund_object) is not dict:
            raise Exception('Param disbursement_refund_object must be a Dictionary')

        return self._post(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/refunds", data=disbursement_refund_object, request_options=request_options)
        
    def create(self, advanced_payment_id, disbursement_id, amount, request_options=None):
        if type(amount) is not float:
            raise Exception('Param amount must be a Float')

        disbursement_refund_object = {"amount": amount}

        return self._post(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/disbursements/" + str(disbursement_id) + "/refunds", data=disbursement_refund_object, request_options=request_options)
    
    def save(self, advanced_payment_id, disbursement_id, disbursement_refund_object, request_options=None):
        if type(disbursement_refund_object) is not dict:
            raise Exception('Param disbursement_refund_object must be a Dictionary')

        return self._post(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/disbursements/" + str(disbursement_id) + "/refunds", data=disbursement_refund_object, request_options=request_options)
