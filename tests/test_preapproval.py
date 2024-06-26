"""
    Module: test_preapproval
"""
import os
import unittest
import mercadopago


class TestPreApproval(unittest.TestCase):
    """
    Test Module: PreApproval
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_create(self):
        """
            Function: xoxoxoxo
        """


if __name__ == "__main__":
    unittest.main()
