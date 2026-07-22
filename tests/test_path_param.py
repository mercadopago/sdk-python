import unittest

from mercadopago.config.request_options import RequestOptions
from mercadopago.core import MPBase


class TestPathParam(unittest.TestCase):
    def test_path_param_escapes_path_traversal(self):
        base = MPBase(RequestOptions(access_token="token"), None)

        self.assertEqual(
            "..%2F..%2Fapplications%2F123",
            base._path_param("../../applications/123"),
        )


if __name__ == "__main__":
    unittest.main()
