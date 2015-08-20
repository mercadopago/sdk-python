try:
    from BaseHTTPServer import HTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler
except ImportError:
    from http.server import HTTPServer, SimpleHTTPRequestHandler

import ssl
import unittest

import mercadopago
import os
from multiprocessing import Process
from requests.exceptions import SSLError
import socket


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

        self.handler = SimpleHTTPRequestHandler

        self.httpd_port = None
        self.httpd = None
        for port_to_try in range(8000, 8099):
            try:
                self.httpd = HTTPServer(('localhost', port_to_try),
                                                       self.handler)
                self.httpd_port = port_to_try
                break
            except socket.error:
                # print "Couldn't use port {0}".format(port_to_try)
                pass

        assert self.httpd_port, "Couldn't bind to any port"

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
            "https://localhost:{0}".format(self.httpd_port)

        with self.assertRaises(SSLError):
            mp.create_preference(preference)

        print("test_fail_if_https_certificate_check_fails OK!")


if __name__ == '__main__':
    unittest.main()
