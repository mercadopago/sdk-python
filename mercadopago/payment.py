from mercadopagorestclient import MercadoPagoRestClient

class Payment(MercadoPagoRestClient):
    def __init__(self, client_id, client_secret, access_token):
        super(Payment, self).__init__(client_id, client_secret, access_token)

    def get(self, id):
        access_token = self.get_access_token()

        #uri_prefix = "/sandbox" if MercadoPago.__sandbox else ""

        payment_info = self.__rest_client.get("/v1/payments/" + id + "?access_token=" + access_token)
        return payment_info

    def get_authorized(self, id):
        access_token = self.get_access_token()
        authorized_payment_info = self.__rest_client.get("/authorized_payments/" + id + "?access_token=" + access_token)
        return authorized_payment_info

    def get_refund(self, id):
        access_token = self.get_access_token()
        response = self.__rest_client.get("/v1/payments/" + id + "/refunds?access_token=" + access_token)
        return response

    def do_refund(self, id):
        access_token = self.get_access_token()
        refund_status = {}
        response = self.__rest_client.post("/v1/payments/" + id + "/refunds?access_token=" + access_token, refund_status)
        return response

    def cancel(self, id):
        access_token = self.get_access_token()
        cancel_status = {"status":"cancelled"}
        response = self.__rest_client.put("/v1/payments/" + id + "?access_token=" + access_token, cancel_status)
        return response

    def search(self, filters, offset=0, limit=0):
        access_token = self.get_access_token()
        filters["access_token"] = access_token
        filters["offset"] = offset
        filters["limit"] = limit

        #uri_prefix = "/sandbox" if MercadoPago.__sandbox else ""

        payment_result = self.__rest_client.get("/v1/payments/search", filters)
        return payment_result
