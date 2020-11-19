class RequestOptions(object):

    def __init__(self, 
                 accessToken, 
                 connectionTimeout, 
                 connectionRequestTimeout, 
                 socketTimeout, 
                 customHeaders):
        if type(accessToken) is not str:
            raise Exception('Warning: accessToken must be a String')
        if type(connectionTimeout) is not int:
            raise Exception('Warning: connectionTimeout must be a Integer')
        if type(connectionRequestTimeout) is not int:
            raise Exception('Warning: connectionTimeout must be a Integer')
        if type(socketTimeout) is not int:
            raise Exception('Warning: connectionTimeout must be a Integer')
        if type(customHeaders) is not str:
            raise Exception('Warning: connectionTimeout must be a String')    

        self.accessToken = accessToken
        self.connectionTimeout = connectionTimeout
        self.connectionRequestTimeout = connectionRequestTimeout
        self.socketTimeout = socketTimeout
        self.customHeaders = customHeaders

    #TODO VERIFICAR QUAL É A MELHOR ABORDAGEM 
    @staticmethod
    def createDefault(self):
        return self.createDefault.__build_class__createDefault

    @staticmethod
    def __build_class__build(self):
        return self.__build_class__build   

    def addTrackingHeaders(self):
        pass