#from .http.http_client import HttpClient

import requests
headers = {}
url_base = ''

class TestHttpClient:
    session = requests.Session()

    def test_get(self):
        modelo = session.get(url=self.url_base, headers=self.headers)

        assert modelo.status_code == 200
