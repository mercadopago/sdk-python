"""OAuth resource for the MercadoPago Authorization API.

Wraps the OAuth 2.0 authorization code flow used in marketplace and
platform integrations to operate on behalf of other sellers.

`API reference
<https://www.mercadopago.com/developers/en/reference/authentication/oauth/_oauth_token/post>`_
"""
from urllib.parse import urlencode

from mercadopago.core import MPBase


_AUTH_URL = "https://auth.mercadopago.com/authorization"


class OAuth(MPBase):
    """Manages the OAuth 2.0 authorization code flow.

    Use this resource when your application needs to operate on behalf
    of other MercadoPago sellers (marketplace or platform scenarios).
    The flow involves redirecting the seller to the authorization URL,
    receiving an authorization code, and exchanging it for access and
    refresh tokens.
    """

    def get_authorization_url(self, app_id, redirect_uri, random_id):
        """Builds the MercadoPago authorization URL for the OAuth flow.

        Redirect the seller to this URL to start the authorization
        process.  After granting permission, MercadoPago redirects back
        to *redirect_uri* with a ``code`` query parameter.

        Args:
            app_id: Your MercadoPago application's client ID.
            redirect_uri: URI where MercadoPago sends the seller after
                authorization.
            random_id: CSRF-protection state parameter; should be a
                unique, unpredictable value per authorization request.

        Returns:
            str: Full authorization URL with query parameters.

        Reference: https://www.mercadopago.com/developers/en/docs/security/oauth/creation
        """
        params = {
            "client_id": app_id,
            "response_type": "code",
            "platform_id": "mp",
            "state": random_id,
            "redirect_uri": redirect_uri,
        }
        return _AUTH_URL + "?" + urlencode(params)

    def create(self, oauth_object, request_options=None):
        """Exchanges an authorization code for an access token.

        Call this after receiving the ``code`` parameter in your
        *redirect_uri* callback.  The returned access token can be used
        to make API requests on behalf of the authorizing seller.

        Args:
            oauth_object: Dict with the authorization request fields:
                ``client_secret`` (your access token), ``code``
                (authorization code received in the callback),
                ``redirect_uri`` (must match the one used in
                :meth:`get_authorization_url`), and ``grant_type``
                (``"authorization_code"``).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *oauth_object* is not a ``dict``.

        Returns:
            dict: Token response including ``access_token``,
                ``refresh_token``, and ``expires_in``.

        Reference: https://www.mercadopago.com/developers/en/reference/authentication/oauth/_oauth_token/post
        """
        if not isinstance(oauth_object, dict):
            raise ValueError("Param oauth_object must be a Dictionary")

        return self._post(
            uri="/oauth/token",
            data=oauth_object,
            request_options=request_options,
        )

    def refresh(self, oauth_object, request_options=None):
        """Refreshes an expired access token.

        Use this to extend the seller's session without requiring them
        to re-authorize.  The *refresh_token* is obtained from the
        initial :meth:`create` response.

        Args:
            oauth_object: Dict with the refresh request fields:
                ``client_secret`` (your access token),
                ``refresh_token`` (the token to refresh), and
                ``grant_type`` (``"refresh_token"``).
            request_options: Per-call configuration overrides.

        Raises:
            ValueError: If *oauth_object* is not a ``dict``.

        Returns:
            dict: New token response with a fresh ``access_token`` and
                ``refresh_token``.

        Reference: https://www.mercadopago.com/developers/en/reference/authentication/oauth/_oauth_token/post
        """
        if not isinstance(oauth_object, dict):
            raise ValueError("Param oauth_object must be a Dictionary")

        return self._post(
            uri="/oauth/token",
            data=oauth_object,
            request_options=request_options,
        )
