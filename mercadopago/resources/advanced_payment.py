from mercadopago.core import MPBase

from datetime import datetime

class AdvancedPayment(MPBase):

    """
    Access to Advanced Payments
    """
    
    def __init__(self, request_options, http_client):
        super(AdvancedPayment, self).__init__(request_options, http_client)

    def search(self, filters, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com/developers/en/reference/advanced_payments/_advanced_payments_id_search/get/)

        Args:
            filters (dict): The search filters parameters 
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Returns:
            dict: Advanced Payment search response
        """
        return self._get(uri="/v1/advanced_payments/search", filters=filters, request_options=request_options)    

    def get(self, id, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/advanced_payments/_advanced_payments_id/get/)

        Args:
            id (str): The Advanced Payment ID 
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Returns:
            dict: Advanced Payment find response
        """
        return self._get(uri="/v1/advanced_payments/" + str(id), request_options=request_options) 

    def create(self, advanced_payment_object, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com/developers/en/reference/advanced_payments/_advanced_payments/post/)

        Args:
            advanced_payment_object (dict): Advanced Payment to be created
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Raises:
            ValueError: Param advanced_payment_object must be a Dictionary

        Returns:
            dict: Advanced Payment creation response
        """
        if type(advanced_payment_object) is not dict:
            raise ValueError("Param advanced_payment_object must be a Dictionary")

        return self._post(uri="/v1/advanced_payments", data=advanced_payment_object, request_options=request_options)

    def capture(self, id, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/advanced_payments/_advanced_payments_id/put/)

        Args:
            id (str): The Advanced Payment ID
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Returns:
            dict: Advanced Payment capture response
        """
        capture_object = {"capture": True}
        return self._put(uri="/v1/advanced_payments/" + str(id), data=capture_object, request_options=request_options) 

    def update(self, id, advanced_payment_object, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/advanced_payments/_advanced_payments_id/put/)

        Args:
            id (str): The Advanced Payment ID 
            advanced_payment_object (dict): Advanced Payment to be updated 
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Raises:
            ValueError: Param advanced_payment_object must be a Dictionary

        Returns:
            dict: Advanced Payment modification response
        """
        if type(advanced_payment_object) is not dict:
            raise ValueError("Param advanced_payment_object must be a Dictionary")

        return self._put(uri="/v1/advanced_payments/" + str(id), data=advanced_payment_object, request_options=request_options) 

    def cancel(self, id, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/advanced_payments/_advanced_payments_id/put/)

        Args:
            id (str): The Advanced Payment ID 
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Returns:
            dict: Advanced Payment cancelation response
        """
        cancel_object = {"status": "cancelled"}
        return self._put(uri="/v1/advanced_payments/" + str(id), data=cancel_object, request_options=request_options) 

    def update_release_date(self, id, release_date, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/advanced_payments/_advanced_payments_id_disbursements_disbursement_id_disburses/post/)

        Args:
            id (str): The Advanced Payment ID
            release_date (dict): Advanced Payment to be canceled 
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Raises: 
            ValueError: Param release_date must be a DateTime
            
        Returns:
            dict: Advanced Payment release date modification response
        """
        if type(release_date) is not datetime.datetime:
            raise ValueError("Param release_date must be a DateTime")

        disbursement_object = {"money_release_date": release_date.strftime("%Y-%m-%d %H:%M:%S.%f")}

        return self._post(uri="/v1/advanced_payments/" + str(id) + "/disburses", data=disbursement_object, request_options=request_options)
