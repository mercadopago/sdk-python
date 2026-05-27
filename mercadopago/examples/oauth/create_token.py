from mercadopago import SDK


def main():
    # Initialize the SDK with your marketplace access token
    access_token = "<YOUR_ACCESS_TOKEN>"
    sdk = SDK(access_token)

    # Step 1: Build the authorization URL and redirect the seller to it
    auth_url = sdk.oauth().get_authorization_url(
        app_id="<YOUR_APP_ID>",
        redirect_uri="https://yourapp.com/callback",
        random_id="<UNIQUE_CSRF_STATE>",
    )
    print("Redirect seller to:", auth_url)

    # Step 2: After the seller authorizes, exchange the received code for tokens
    oauth_object = {
        "client_secret": access_token,
        "code": "<AUTHORIZATION_CODE_FROM_CALLBACK>",
        "redirect_uri": "https://yourapp.com/callback",
        "grant_type": "authorization_code",
    }

    try:
        response = sdk.oauth().create(oauth_object)
        print("Token created successfully:", response["response"])
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
