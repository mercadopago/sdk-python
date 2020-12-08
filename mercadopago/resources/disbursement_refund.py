from mercadopago.core import MPBase

class DisbursementRefund(MPBase):

    """
    Access to Advanced Payments Refunds
    """
    
    def __init__(self, request_options, http_client):
        super(DisbursementRefund, self).__init__(request_options, http_client)

    def get_list(self, advanced_payment_id, request_options=None):
        """[Args:
            advanced_payment_id (str): The Advanced Payment ID 
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Returns:
            dict: Disbursement Refund find response
        """
        return self._get(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/refunds", request_options=request_options)

    def create_all(self, advanced_payment_id, disbursement_refund_object, request_options=None):
        """[Args:
            advanced_payment_id (str): The Advanced Payment ID 
            disbursement_refund_object (dict): Disbursement Refund to be created
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Raises: 
        ValueError: Param disbursement_refund_object must be a Dictionary

        Returns:
            dict: Disbursement Refund creation all response
        """
        if type(disbursement_refund_object) is not dict:
            raise ValueError('Param disbursement_refund_object must be a Dictionary')

        return self._post(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/refunds", data=disbursement_refund_object, request_options=request_options)
        
    def create(self, advanced_payment_id, disbursement_id, amount, request_options=None):
        """[Args:
            advanced_payment_id (str): The Advanced Payment ID 
            disbursement_id (str): Disbursement ID
            amount: Amount to be refunded
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Raises: 
        ValueError: Param amount must be a Float
        
        Returns:
            dict: Disbursement Refund creation response
        """
        if type(amount) is not float:
            raise ValueError('Param amount must be a Float')

        disbursement_refund_object = {"amount": amount}

        return self._post(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/disbursements/" + str(disbursement_id) + "/refunds", data=disbursement_refund_object, request_options=request_options)
    
    #TODO VERIFICAR O NOME DESTE MÉTODO > .NET CORE ESTÁ COMO REFUND()
    def save(self, advanced_payment_id, disbursement_id, disbursement_refund_object, request_options=None):
        """[Args:
            advanced_payment_id (str): The Advanced Payment ID 
            disbursement_id (str): Disbursement ID
            disbursement_refund_object (dict): Disbursement Refund to be saved
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Raises: 
        ValueError: Param disbursement_refund_object must be a Dictionary
        
        Returns:
            dict: Disbursement Refund save response
        """
        if type(disbursement_refund_object) is not dict:
            raise ValueError('Param disbursement_refund_object must be a Dictionary')

        return self._post(uri="/v1/advanced_payments/" + str(advanced_payment_id) + "/disbursements/" + str(disbursement_id) + "/refunds", data=disbursement_refund_object, request_options=request_options)
