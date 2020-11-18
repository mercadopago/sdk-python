from mercadopago.SDK import SDK


#TODO CORE
#TODO DATASTRUCTURES
#TODO EXCEPETIONS


class Preference(object):
    def __init__(self, SDK):
        self.SDK = SDK

    #appendTrack(self, track)
    #    if(self.track == nil):
    #        self.track = Track[]

    def findById(self, id):
        pass

    def findById(self, useCache):
        pass

    #@GET(path="/checkout/preferences/:id")
    def findById(self, id, useCache, requestOptions):
        pass

    def save(self):
        pass

    #@POST(path="/checkout/preferences")
    def save(self, requestOptions):
        pass

    def update(self):
        pass

    #@PUT(path="/checkout/preferences/:id")
    def update(self, requestOptions):
        pass
