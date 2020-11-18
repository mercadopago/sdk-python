class RequestOptions(object):

    def __init__(self, 
                 accessToken, 
                 connectionTimeout, 
                 connectionRequestTimeout, 
                 socketTimeout, 
                 customHeaders):

    #TODO if type PRA VALIDAR A GALERA

        self.accessToken = accessToken
        self.connectionTimeout = connectionTimeout
        self.connectionRequestTimeout = connectionRequestTimeout
        self.socketTimeout = socketTimeout
        self.customHeaders = customHeaders
 