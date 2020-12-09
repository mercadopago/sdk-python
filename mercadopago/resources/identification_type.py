from mercadopago.core import MPBase

class IdentificationType(MPBase):

    """
    Access to Identification Types
    """
    
    def __init__(self, request_options, http_client):
        super(IdentificationType, self).__init__(request_options, http_client)

    def search(self, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/identification_types/_identification_types/get/)

        Args:
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Returns:
            dict: Identification Types find response
        """
        return self._get(uri="/v1/identification_types", request_options=request_options)
            