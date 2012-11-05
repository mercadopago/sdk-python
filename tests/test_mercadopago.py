import unittest
import mercadopago

class TestMercadopago(unittest.TestCase):

  def test_get_preference(self):

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

    mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")

    create_preference_result = mp.create_preference(preference)

    self.assertEquals(create_preference_result["status"], "201")

    created_preference_id = create_preference_result["response"]["id"]

    get_preference_result = mp.get_preference(created_preference_id)

    self.assertEquals(get_preference_result["status"], "200")

    obtained_preference = get_preference_result["response"]

    self.assertEquals(obtained_preference["items"][0]["title"], "sdk-python")
    self.assertEquals(obtained_preference["items"][0]["quantity"], 1)
    self.assertEquals(obtained_preference["items"][0]["currency_id"], "ARS")
    self.assertEquals(obtained_preference["items"][0]["unit_price"], 10.5)

    def create_preference(self):

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

      mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")

      create_preference_result = mp.create_preference(preference)

      self.assertEquals(create_preference_result["status"], "201")

      created_preference = create_preference_result["response"]

      self.assertEquals(created_preference["title"], "sdk-python")
      self.assertEquals(created_preference["quantity"], 1)
      self.assertEquals(created_preference["currency_id"], "ARS")
      self.assertEquals(created_preference["unit_price"], 10.5)

    def update_preference(self):

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

      mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")

      create_preference_result = mp.create_preference(preference)

      self.assertEquals(create_preference_result["status"], "201")

      created_preference_id = create_preference_result["response"]["id"]

      update_preference_result = mp.update_preference(created_preference_id)

      self.assertEquals(update_preference_result["status"], "200")

      get_preference_result = mp.get_preference(created_preference_id)

      self.assertEquals(get_preference_result["status"], "200")

      obtained_preference = get_preference_result["response"]

      self.assertEquals(obtained_preference["items"][0]["title"], "sdk-python")
      self.assertEquals(obtained_preference["items"][0]["quantity"], 1)
      self.assertEquals(obtained_preference["items"][0]["currency_id"], "ARS")
      self.assertEquals(obtained_preference["items"][0]["unit_price"], 10.5)

if __name__ == '__main__':
    unittest.main()
