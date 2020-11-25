from mercadopago.core.request_options import RequestOptions
from mercadopago.http.http_client import HttpClient
from mercadopago.config import Config
from json.encoder import JSONEncoder

class MPBase(object):
    def __init__(self, request_options):
        if type(request_options) is not RequestOptions:
            raise Exception('A valid request_options must be informed')

        self.request_options = request_options
        self.http_client = HttpClient()
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
        headers = request_options.default_headers()

        if extra_headers is not None:
            headers.update(extra_headers)

        if request_options.custom_headers is not None:
            headers.update(request_options.custom_headers)

        return headers

    def _get(self, uri, filters=None, request_options=None):
        if filters is not None and type(filters) is not dict:
            raise Exception('Filters must be a Dictionary')

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(request_options, {'Content-type': self.config.MIME_JSON})

        return self.http_client.get(url=self.config.API_BASE_URL + uri, params=filters, headers=headers)

    def _post(self, uri, data=None, params=None, request_options=None):
        if data is not None:
            data = JSONEncoder().encode(data)

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(request_options, {'Content-type': self.config.MIME_JSON})

        return self.http_client.post(url=self.config.API_BASE_URL + uri, data=data, params=params, headers=headers)

    def _put(self, uri, data=None, params=None, request_options=None):
        if data is not None:
            data = JSONEncoder().encode(data)

        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(request_options, {'Content-type': self.config.MIME_JSON})

        return self.http_client.put(url=self.config.API_BASE_URL + uri, data=data, params=params, headers=headers)

    def _delete(self, uri, params=None, request_options=None):
        request_options = self.__check_request_options(request_options)
        headers = self.__check_headers(request_options)

        return self.http_client.delete(url=self.config.API_BASE_URL + uri, params=params, headers=headers)