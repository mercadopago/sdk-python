import sys
sys.path.append('../')


from mercadopago import SDK
from mercadopago.config import RequestOptions


class HttpClientProxy():
    def __init__(self):
        pass

    def get(self, url, headers, params=None):
        print("Using default httpClient")

sdk = SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

