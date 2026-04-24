"""User resource for the MercadoPago API.

Wraps the ``/users/me`` endpoint to retrieve the profile of the
currently authenticated MercadoPago account.
"""
from mercadopago.core import MPBase


class User(MPBase):
    """Retrieves the authenticated user's account information.

    Returns details such as user ID, email, site (country), and account
    status for the access token in use.
    """

    def get(self, request_options=None):
        """Retrieves the authenticated user's profile.

        Args:
            request_options: Per-call configuration overrides.

        Returns:
            dict: User profile (id, email, site_id, etc.).
        """
        return self._get(uri="/users/me", request_options=request_options)

    @property
    def request_options(self):
        """Default :class:`RequestOptions` for this resource instance."""
        return self.__request_options
