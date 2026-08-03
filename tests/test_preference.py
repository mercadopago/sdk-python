"""
    Module: test_preference
"""
import os
import unittest
import time
import mercadopago


class TestPreference(unittest.TestCase):
    """
    Test Module: Preference
    """
    sdk = mercadopago.SDK(os.environ['ACCESS_TOKEN'])

    def test_all(self):
        """
        Test Module: Preference
        """
        preference_object = {
            "items": [
                {
                    "description": "Test Update Success",
                    "id": "456",
                    "picture_url": "http://product1.image.png",
                    "quantity": 1,
                    "title": "Item 1",
                    "currency_id": "BRL",
                    "unit_price": 20.5,
                    "warranty": False,
                    "type": "default",
                    "event_date": "2027-01-15T00:00:00.000-03:00",
                    "category_descriptor": {
                        "passenger": {
                            "first_name": "Nome",
                            "last_name": "Sobrenome",
                            "identification": {
                                "type": "CPF",
                                "number": "19119119100"
                            }
                        },
                        "route": {
                            "departure": "SAO",
                            "destination": "RIO",
                            "departure_date_time": "2027-01-15T08:00:00.000-03:00",
                            "arrival_date_time": "2027-01-15T09:00:00.000-03:00",
                            "company": "TAM"
                        }
                    }
                }
            ],
            "payer": {
                "email": "test_user_123456@testuser.com",
                "date_created": "2020-01-15T00:00:00.000-03:00",
                "authentication_type": "WEB",
                "is_prime_user": False,
                "is_first_purchase_online": False,
                "last_purchase": "2024-01-01T00:00:00.000-03:00",
                "registration_date": "2020-01-15T00:00:00.000-03:00"
            },
            "shipments": {
                "receiver_address": {
                    "street_name": "Av das Nacoes Unidas",
                    "street_number": 3003,
                    "zip_code": "06233200",
                    "state_name": "Rio de Janeiro",
                    "city_name": "Buzios",
                    "floor": "2",
                    "apartment": "A"
                },
                "express_shipment": False,
                "local_pickup": False
            }
        }
        preference_saved = self.sdk.preference().create(preference_object)
        self.assertEqual(preference_saved["status"], 201)
        time.sleep(3)

        preference_object["items"][0]["title"] = "Testando 1 2 3"

        preference_id = preference_saved["response"]["id"]
        preference_update = self.sdk.preference().update(preference_id, preference_object)
        self.assertEqual(preference_update["status"], 200)

        time.sleep(3)
        preference_saved = self.sdk.preference().get(preference_id)
        self.assertEqual(preference_saved["status"], 200)
        self.assertEqual(preference_saved["response"]["items"][0]["title"],
                         preference_object["items"][0]["title"])

        time.sleep(3)
        preference_search = self.sdk.preference().search()
        self.assertEqual(preference_search["status"], 200)


if __name__ == "__main__":
    unittest.main()
