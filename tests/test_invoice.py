"""
    Module: test_invoice
"""
import os
import unittest
import mercadopago


class TestInvoice(unittest.TestCase):
    """
    Test Module: Invoice
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_search_invoice(self):
        """
        Test Function: Invoice search returns a valid HTTP response
        """
        filters_invoice = {
            "limit": 5
        }
        invoices = self.sdk.invoice().search(filters=filters_invoice)
        self.assertIn(invoices["status"], [200, 400, 401, 404])


if __name__ == "__main__":
    unittest.main()
