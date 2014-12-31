import BaseHTTPServer, SimpleHTTPServer
import ssl
import unittest

import mercadopago
import os
from multiprocessing import Process
from requests.exceptions import SSLError


client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"


class TestHttps(unittest.TestCase):

    def get_pem_file(self):
        this_module = os.path.abspath(__file__)
        this_module_dir = os.path.dirname(this_module)
        certfile = os.path.join(this_module_dir, 'server.pem')
        return certfile

    def serve_forever(self):
        self.httpd.serve_forever()

    def unset_proxy_environment_variables(self):
        for var in ('proxy', 'http_proxy', 'https_proxy'):
            try:
                del os.environ[var]
            except KeyError:
                pass

    def setUp(self):
        self.unset_proxy_environment_variables()

        self.handler = SimpleHTTPServer.SimpleHTTPRequestHandler

        self.httpd = BaseHTTPServer.HTTPServer(('localhost', 4443), self.handler)
        self.httpd.socket = ssl.wrap_socket(self.httpd.socket,
                                       certfile=self.get_pem_file(),
                                       server_side=True)
        self.https_server_process = Process(target=self.serve_forever)
        self.https_server_process.start()

    def tearDown(self):
        self.https_server_process.terminate()

    def test_fail_if_https_certificate_check_fails(self):

        preference = {
          "items": [
            {
              "title": "sdk-python",
              "quantity": 1,
              "currency_id": "ARS",
              "unit_price": 10.5
            }
          ]
        }

        mp = mercadopago.MP(client_id, client_secret)
        mp._MP__rest_client._RestClient__API_BASE_URL = \
            'https://localhost:4443'

        with self.assertRaises(SSLError):
            mp.create_preference(preference)


if __name__ == '__main__':
    unittest.main()
