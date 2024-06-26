"""
    Module: test_identification_type
"""
import os
import unittest
import mercadopago


class TestIdentificationType(unittest.TestCase):
    """
    Test Module: Identification Type
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_find_all(self):
        """
        Test Function: Identification Type
        """
        identifications = self.sdk.identification_type().list_all()
        self.assertEqual(identifications["status"], 200)


if __name__ == "__main__":
    unittest.main()
