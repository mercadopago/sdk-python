from mercadopago.sdk import SDK


def main():
    # Define the authentication token
    access_token = "<YOUR_ACCESS_TOKEN>"
    sdk = SDK(access_token)

    try:
        preference_data = {
            "items": [
                {
                    "title": "Dummy Item",
                    "quantity": 1,
                    "unit_price": 10.0,
                    "warranty": False,
                    "type": "default",
                    "event_date": "2027-01-15T00:00:00.000-03:00",
                    "category_descriptor": {
                        "passenger": {
                            "first_name": "<PASSENGER_FIRST_NAME>",
                            "last_name": "<PASSENGER_LAST_NAME>",
                            "identification": {
                                "type": "CPF",
                                "number": "<PASSENGER_DOC_NUMBER>"
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
                "email": "<PAYER_EMAIL>",
                "date_created": "2020-01-15T00:00:00.000-03:00",
                "authentication_type": "MOBILE",
                "is_prime_user": False,
                "is_first_purchase_online": False,
                "last_purchase": "2025-12-01T00:00:00.000-03:00",
                "registration_date": "2020-01-15T00:00:00.000-03:00"
            },
            "shipments": {
                "receiver_address": {
                    "street_name": "Av. Paulista",
                    "street_number": 1000,
                    "zip_code": "01310-100",
                    "state_name": "Sao Paulo",
                    "city_name": "Sao Paulo",
                    "floor": "3",
                    "apartment": "B"
                },
                "express_shipment": False,
                "local_pickup": False
            },
            "notification_url": "https://webhook.site/test-notification"
        }

        # Call the method to create the preference
        preference = sdk.preference().create(preference_data)
        print(preference)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
