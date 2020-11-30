from mercadopago.core import MPBase

from datetime import datetime

class Disbursement(MPBase):

    """
    Access to Advanced Payments Disbursements
    """
    
    def __init__(self, request_options, http_client):
        super(Disbursement, self).__init__(request_options, http_client)

    def update_release_date(self, advanced_payment_id, disbursement_id, release_date, request_options=None):
        if type(release_date) is not datetime.datetime:
            raise ValueError("Param release_date must be a DateTime")

        #TODO Validar se é esse mesmo o nome do parametro
        #TODO Validar se temos que enviar realmente "date + time"
        disbursement_object = {"money_release_date": release_date.strftime("%m/%d/%Y, %H:%M:%S")}

        return self._post(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/disbursements/" + str(disbursement_id) + "/disburses", data=disbursement_object, request_options=request_options)
