from mercadopago.core import MPBase

class Refund(MPBase):

    """
    This class will allow you to refund payments created through the Payments class.

    You can refund a payment within 180 days after it was approved.
    
    You must have sufficient funds in your account in order to successfully refund the payment amount. Otherwise, you will get a 400 Bad Request error.
    
    [Click here for more infos](https://www.mercadopago.com.br/developers/en/guides/manage-account/account/cancellations-and-refunds#bookmark_refunds)
    """
    
    def __init__(self, request_options, http_client):
        super(Refund, self).__init__(request_options, http_client)

    def search(self, payment_id, request_options=None):
        """Args:
            payment_id (str): The Payment ID
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Returns:
            dict: Refund find response
        """
        return self._get(uri="/v1/payments/" + str(payment_id) + "/refunds", request_options=request_options)

    def create(self, payment_id, refund_object, request_options=None):
        """Args:
            payment_id (str): The Payment ID
            refund_object (dict): Refund to be created
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Raises: 
            ValueError: Param refund_object must be a Dictionary    

        Returns:
            dict: Refund creation response
        """
        if type(refund_object) is not dict:
            raise ValueError("Param refund_object must be a Dictionary")

        return self._post(uri="/v1/payments/" + str(payment_id) + "/refunds", data=refund_object, request_options=request_options)
