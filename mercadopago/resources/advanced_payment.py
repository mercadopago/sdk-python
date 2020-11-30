from mercadopago.core import MPBase

class AdvancedPayment(MPBase):

    """
    gdfbdgh
    """
    
    def __init__(self, request_options, http_client):
        super(AdvancedPayment, self).__init__(request_options, http_client)

    def find_by_id(self, id, request_options=None):
        return self._get(uri="/v1/advanced_payments/" + str(id), request_options=request_options) 

#TODO PROCESS METHOD IN MPBASE
