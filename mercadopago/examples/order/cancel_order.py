import os
import time

from mercadopago import SDK

def main():
    # Define the authentication token
    access_token = "<YOUR_ACCESS_TOKEN>"

    # Define the authentication token
    sdk = SDK(access_token)

    # Create a test card token
    def create_test_card():
        card_token_object = {
            "card_number": "5031433215406351",
            "security_code": "123",
            "expiration_year": "2030",
            "expiration_month": "11",
            "cardholder": {"name": "APRO"}
        }
        card_token_created = sdk.card_token().create(card_token_object)
        return card_token_created["response"]["id"]

    # Create an order object
    card_token_id = create_test_card()
    order_object = {
        "type": "online",
        "capture_mode": "manual",
        "processing_mode": "automatic",
        "total_amount": "880.00",
        "external_reference": "ext_ref_1234",
        "transactions": {
            "payments": [
                {
                    "amount": "880.00",
                    "payment_method": {
                        "id": "master",
                        "type": "credit_card",
                        "token": card_token_id,
                        "installments": 2
                    }
                }
            ]
        },
        "payer": {
            "email": "<PAYER_EMAIL>"
        }
    }

    try:
        # Call the method to create the order
        response = sdk.order().create(order_object)
        print("Order created successfully")

        # Get the order ID from the response
        order_id = response["response"]["id"]

        time.sleep(5)
        # Call the method to CANCEL
        order_details = sdk.order().cancel(order_id)
        print("Order details:", order_details["response"])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()