from mercadopago import SDK


def main():
    # Initialize the SDK with your access token
    access_token = "<YOUR_ACCESS_TOKEN>"
    sdk = SDK(access_token)

    # List available Point devices to get a device_id
    devices = sdk.point().get_devices()
    print("Available devices:", devices["response"])

    # Create a payment intent on a specific device
    device_id = "<YOUR_DEVICE_ID>"
    payment_intent_object = {
        "amount": 1500,
        "description": "Product purchase",
        "payment": {
            "installments": 1,
            "type": "credit_card",
        },
    }

    try:
        response = sdk.point().create(device_id, payment_intent_object)
        print("Payment intent created:", response["response"])

        # Retrieve the payment intent status
        payment_intent_id = response["response"]["id"]
        status = sdk.point().get(payment_intent_id)
        print("Payment intent status:", status["response"])
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
