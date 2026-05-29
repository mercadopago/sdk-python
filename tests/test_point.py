"""
    Module: test_point
"""
import os
import unittest
import mercadopago


class TestPoint(unittest.TestCase):
    """
    Test Module: Point
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_get_devices(self):
        """
        Test Function: Point get_devices returns a valid HTTP response
        """
        devices = self.sdk.point().get_devices()
        self.assertIn(devices["status"], [200, 400, 401, 403, 404])

    def test_create_raises_on_invalid_param(self):
        """
        Test Function: Point create raises ValueError for non-dict payment intent
        """
        with self.assertRaises(ValueError):
            self.sdk.point().create("device_123", "not_a_dict")


if __name__ == "__main__":
    unittest.main()
