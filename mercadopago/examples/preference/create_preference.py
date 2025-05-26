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
                    "unit_price": 10.0
                }
            ],
            "notification_url": "https://webhook.site/test-notification"
        }

        # Call the method to create the preference
        preference = sdk.preference().create(preference_data)
        print(preference)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
