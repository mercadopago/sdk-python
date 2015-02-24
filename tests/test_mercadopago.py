import unittest
import mercadopago
import json

client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"

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

    mp = mercadopago.MP(client_id, client_secret)

    create_preference_result = mp.create_preference(preference)

    #print(create_preference_result)

    self.assertEquals(create_preference_result["status"], 201)

    created_preference_id = create_preference_result["response"]["id"]

    get_preference_result = mp.get_preference(created_preference_id)

    self.assertEquals(get_preference_result["status"], 200)

    obtained_preference = get_preference_result["response"]

    self.assertEquals(obtained_preference["items"][0]["title"], "sdk-python")
    self.assertEquals(obtained_preference["items"][0]["quantity"], 1)
    self.assertEquals(obtained_preference["items"][0]["currency_id"], "ARS")
    self.assertEquals(obtained_preference["items"][0]["unit_price"], 10.5)

    print("test_get_preference OK!")

  def test_create_preference(self):

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

    create_preference_result = mp.create_preference(preference)

    self.assertEquals(create_preference_result["status"], 201)

    created_preference = create_preference_result["response"]

    self.assertEquals(created_preference["items"][0]["title"], "sdk-python")
    self.assertEquals(created_preference["items"][0]["quantity"], 1)
    self.assertEquals(created_preference["items"][0]["currency_id"], "ARS")
    self.assertEquals(created_preference["items"][0]["unit_price"], 10.5)

    print("test_create_preference OK!")

  def test_update_preference(self):

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

    create_preference_result = mp.create_preference(preference)

    self.assertEquals(create_preference_result["status"], 201)

    created_preference_id = create_preference_result["response"]["id"]

    preference_update = {
      "items": [
        {
          "title": "sdk-python rules!",
          "quantity": 2,
          "currency_id": "ARS",
          "unit_price": 19.99
        }
      ]
    }

    update_preference_result = mp.update_preference(created_preference_id, preference_update)

    self.assertEquals(update_preference_result["status"], 200)

    get_preference_result = mp.get_preference(created_preference_id)

    self.assertEquals(get_preference_result["status"], 200)

    obtained_preference = get_preference_result["response"]

    self.assertEquals(obtained_preference["items"][0]["title"], "sdk-python rules!")
    self.assertEquals(obtained_preference["items"][0]["quantity"], 2)
    self.assertEquals(obtained_preference["items"][0]["currency_id"], "ARS")
    self.assertEquals(obtained_preference["items"][0]["unit_price"], 19.99)

    print("test_update_preference OK!")

if __name__ == '__main__':
    unittest.main()
