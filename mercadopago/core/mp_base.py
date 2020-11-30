from mercadopago.http import HttpClient
from json.encoder import JSONEncoder
from mercadopago.config import RequestOptions
from mercadopago.config import Config

class MPBase(object):

    """
    All mercadopago.resources extends this one to call the REST services
    """
    
    def __init__(self, request_options, http_client):
        if type(request_options) is not RequestOptions:
            raise Exception('A valid request_options must be informed')

        self.request_options = request_options
        self.http_client = http_client

        self.config = Config()

    def __check_request_options(self, request_options):
        if request_options is not None and type(request_options) is not RequestOptions:
            raise Exception('Param request_options must be a RequestOptions Object')
        elif request_options is None:
            request_options = self.request_options

        if request_options.access_token is None:
            request_options.access_token = self.request_options.access_token

        return request_options

    def __check_headers(self, request_options, extra_headers=None):
        headers = request_options is None and self.request_options.get_headers() or request_options.get_headers()

        if extra_headers is not None:
            headers.update(extra_headers)

        return headers

    def _get(self, uri, filters=None, request_options=None):
        if filters is not None and type(filters) is not dict:
            raise Exception('Filters must be a Dictionary')

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(request_options, {'Content-type': self.config.MIME_JSON})
        print(headers)
        return self.http_client.get(url=self.config.API_BASE_URL + uri, params=filters, headers=headers, timeout=request_options.connection_timeout)

    def _post(self, uri, data=None, params=None, request_options=None):
        if data is not None:
            data = JSONEncoder().encode(data)

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(request_options, {'Content-type': self.config.MIME_JSON})

        return self.http_client.post(url=self.config.API_BASE_URL + uri, data=data, params=params, headers=headers, timeout=request_options.connection_timeout)

    def _put(self, uri, data=None, params=None, request_options=None):
        if data is not None:
            data = JSONEncoder().encode(data)

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(request_options, {'Content-type': self.config.MIME_JSON})

        return self.http_client.put(url=self.config.API_BASE_URL + uri, data=data, params=params, headers=headers, timeout=request_options.connection_timeout)

    def _delete(self, uri, params=None, request_options=None):
        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(request_options)

        return self.http_client.delete(url=self.config.API_BASE_URL + uri, params=params, headers=headers, timeout=request_options.connection_timeout)