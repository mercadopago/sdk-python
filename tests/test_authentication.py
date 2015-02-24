import unittest
import mercadopago
import json

client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"
ll_access_token = None

class TestAuthentication(unittest.TestCase):

  def test_client_id_and_client_secret(self):

    preference = {
      "items": [
        {
          "title": "sdk-python test_client_id_and_client_secret",
          "quantity": 1,
          "currency_id": "ARS",
          "unit_price": 10.5
        }
      ]
    }

    mp = mercadopago.MP(client_id, client_secret)

    self.assertEquals(mp.create_preference(preference)["status"], 201)

    print("test_client_id_and_client_secret OK!")

  def test_long_live_access_token(self):

    if not ll_access_token is None:

      preference = {
        "items": [
          {
            "title": "sdk-python test_long_live_access_token",
            "quantity": 1,
            "currency_id": "ARS",
            "unit_price": 10.5
          }
        ]
      }

      mp = mercadopago.MP(ll_access_token)

      self.assertEquals(mp.create_preference(preference)["status"], 201)

      print("test_long_live_access_token OK!")

    else:
      print("test_long_live_access_token (NOT EXECUTED)")

if __name__ == '__main__':
    unittest.main()
