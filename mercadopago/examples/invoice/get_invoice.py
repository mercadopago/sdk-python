from mercadopago import SDK


def main():
    # Initialize the SDK with your access token
    access_token = "<YOUR_ACCESS_TOKEN>"
    sdk = SDK(access_token)

    # Search invoices for a specific subscription (preapproval)
    filters = {
        "preapproval_id": "<YOUR_PREAPPROVAL_ID>",
        "limit": 10,
    }

    try:
        invoices = sdk.invoice().search(filters=filters)
        print("Invoices found:", invoices["response"])

        # Retrieve a specific invoice by ID
        if invoices["response"].get("results"):
            invoice_id = invoices["response"]["results"][0]["id"]
            invoice = sdk.invoice().get(invoice_id)
            print("Invoice details:", invoice["response"])
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
