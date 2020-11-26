from mercadopago.core.mp_base import MPBase

class Preference(MPBase):
    def __init__(self, request_options):
        super(Preference, self).__init__(request_options)
    
    def find_by_id(self, id, request_options=None):
        return self._get(uri="/checkout/preferences/" + str(id), request_options=request_options)

    def update(self, id, preference_object, request_options=None):
        if type(preference_object) is not dict:
            raise Exception("Param preference_object must be a Dictionary")
        return self._put(uri="/checkout/preferences/" + str(id), data=preference_object, request_options=request_options)

    def save(self, request_options=None):
        return self._post(uri="/checkout/preferences", request_options=request_options)
        