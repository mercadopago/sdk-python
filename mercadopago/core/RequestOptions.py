class RequestOptions(object):

    def __init__(self, 
                 accessToken=None, 
                 connectionTimeout=None, 
                 customHeaders=None):
        if accessToken !=None and type(accessToken) is not str:
            raise Exception('Warning: accessToken must be a String')
        if connectionTimeout !=None and type(connectionTimeout) is not int:
            raise Exception('Warning: connectionTimeout must be a Integer')
        if customHeaders !=None and type(customHeaders) is not dict:
            raise Exception('Warning: customHeaders must be a Dictionary')    

        self.accessToken = accessToken
        self.connectionTimeout = connectionTimeout
        self.customHeaders = customHeaders

