from mercadopago.core import MPBase

from datetime import datetime

class AdvancedPayment(MPBase):

    """
    Access to Advanced Payments
    """
    
    def __init__(self, request_options, http_client):
        super(AdvancedPayment, self).__init__(request_options, http_client)

    def find_by_id(self, id, request_options=None):
        return self._get(uri="/v1/advanced_payments/" + str(id), request_options=request_options) 

    def save(self, advanced_payment_object, request_options=None):
        if type(advanced_payment_object) is not dict:
            raise ValueError("Param advanced_payment_object must be a Dictionary")

        return self._post(uri="/v1/advanced_payments", data=advanced_payment_object, request_options=request_options)

    def capture(self, id, request_options=None):
        capture_object = {"capture": True}
        return self._put(uri="/v1/advanced_payments/" + str(id), data=capture_object, request_options=request_options) 

    def update(self, id, advanced_payment_object, request_options=None):
        if type(advanced_payment_object) is not dict:
            raise ValueError("Param advanced_payment_object must be a Dictionary")

        return self._put(uri="/v1/advanced_payments/" + str(id), data=advanced_payment_object, request_options=request_options) 

    def cancel(self, id, request_options=None):
        cancel_object = {"status": "cancelled"}
        return self._put(uri="/v1/advanced_payments/" + str(id), data=cancel_object, request_options=request_options) 

    def update_release_date(self, advanced_payment_id, release_date, request_options=None):
        if type(release_date) is not datetime.datetime:
            raise ValueError("Param release_date must be a DateTime")

        #TODO Validar se é esse mesmo o nome do parametro SIM! VERIFICADO NO PROJETO .NET CORE
        #TODO Validar se temos que enviar realmente "date + time" PAYLOAD 2018-06-27T09:34:20.518-04:00
        disbursement_object = {"money_release_date": release_date.strftime("%Y-%m-%d %H:%M:%S")}

        return self._post(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/disburses", data=disbursement_object, request_options=request_options)