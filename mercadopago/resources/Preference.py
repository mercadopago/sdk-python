from mercadopago.core.mp_base import MPBase

class Preference(MPBase):
    def __init__(self, request_options):
        super(Preference, self).__init__(request_options)
    
    #TODO SEM TESTE
    def find_by_id(self, id, request_options=None):
        if type(id) is not str:
            raise Exception('Param id must be a String')
                       
        return self._get(uri="/checkout/preferences/" + str(id), request_options=request_options)
