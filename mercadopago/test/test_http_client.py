from mercadopago.http.http_client import HttpClient

import http.client
headers = {}
url_base = ''

class TestHttpClient:
    session = http.client.HTTPConnection.request()

    def test_get(self):
        modelo = session.get(url=self.url_base, headers=self.headers)

        assert modelo.status_code == 200
        