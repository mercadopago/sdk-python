"""Identification Type resource for the MercadoPago API.

Wraps the ``/v1/identification_types`` endpoint to retrieve the list of
accepted document types (e.g. CPF, CNPJ, DNI) for each country.
"""
from mercadopago.core import MPBase


class IdentificationType(MPBase):
    """Lists accepted identification document types by country.

    Use the returned types to populate document-type selectors in your
    checkout form so buyers can provide a valid identification.
    """

    def list_all(self, request_options=None):
        """Retrieves all available identification types.

        Args:
            request_options: Per-call configuration overrides.

        Returns:
            dict: List of identification type objects (id, name, min/max length).
        """
        return self._get(uri="/v1/identification_types", request_options=request_options)

    @property
    def request_options(self):
        """Default :class:`RequestOptions` for this resource instance."""
        return self.__request_options
