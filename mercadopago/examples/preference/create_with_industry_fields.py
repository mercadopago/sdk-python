# Example: Preference with industry data fields for payment approval improvement
from mercadopago.sdk import SDK


def main():
    # Define the authentication token
    access_token = "<YOUR_ACCESS_TOKEN>"
    sdk = SDK(access_token)

    try:
        preference_data = {
            "items": [
                {
                    "id": "FLIGHT-001",
                    "title": "Flight SAO-RIO",
                    "description": "Round trip, economy class",
                    "picture_url": "https://example.com/flight.jpg",
                    "category_id": "travels",
                    "quantity": 1,
                    "currency_id": "BRL",
                    "unit_price": 450.00,
                    "warranty": False,
                    "type": "travel",
                    "event_date": "2027-01-15T08:00:00.000-03:00",
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
                },
                {
                    "id": "INSURANCE-001",
                    "title": "Travel Insurance",
                    "description": "Basic coverage during trip",
                    "picture_url": "https://example.com/insurance.jpg",
                    "category_id": "travels",
                    "quantity": 1,
                    "currency_id": "BRL",
                    "unit_price": 50.00,
                    "warranty": True,
                    "type": "travel",
                    "event_date": "2027-01-15T08:00:00.000-03:00",
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
                "name": "<PAYER_FIRST_NAME>",
                "surname": "<PAYER_LAST_NAME>",
                "date_created": "2020-01-15T00:00:00.000-03:00",
                "authentication_type": "MOBILE",
                "is_prime_user": True,
                "is_first_purchase_online": False,
                "last_purchase": "2025-12-01T00:00:00.000-03:00",
                "registration_date": "2020-01-15T00:00:00.000-03:00",
                "phone": {
                    "area_code": "11",
                    "number": "999998888"
                },
                "identification": {
                    "type": "CPF",
                    "number": "<PAYER_DOC_NUMBER>"
                },
                "address": {
                    "zip_code": "01310-100",
                    "street_name": "Av. Paulista",
                    "street_number": "1000"
                }
            },
            "shipments": {
                "mode": "custom",
                "receiver_address": {
                    "street_name": "Av. Paulista",
                    "street_number": "1000",
                    "zip_code": "01310-100",
                    "state_name": "Sao Paulo",
                    "city_name": "Sao Paulo",
                    "floor": "3",
                    "apartment": "B"
                },
                "express_shipment": False,
                "local_pickup": False
            },
            "back_urls": {
                "success": "https://example.com/success",
                "failure": "https://example.com/failure",
                "pending": "https://example.com/pending"
            },
            "auto_return": "approved",
            "external_reference": "TRAVEL-BOOKING-001",
            "notification_url": "https://example.com/notifications"
        }

        # Call the method to create the preference
        preference = sdk.preference().create(preference_data)
        print("Preference created successfully:")
        print("id:", preference["response"].get("id"))
        print("init_point:", preference["response"].get("init_point"))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
