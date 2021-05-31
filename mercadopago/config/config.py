"""
Module: config
"""
import platform

class Config():

    """
    General infos of your SDK
    """

    def __init__(self):
        self.__version = "2.0.7"
        self.__user_agent = "MercadoPago Python SDK v" + self.__version
        self.__product_id = "bc32bpftrpp001u8nhlg"
        self.__tracking_id = "platform:" + platform.python_version()
        self.__tracking_id += ",type:SDK" + self.__version + ",so;"

    __api_base_url = "https://api.mercadopago.com"
    __mime_json = "application/json"
    __mime_form = "application/x-www-form-urlencoded"

    @property
    def version(self):
        """
        Sets the attribute value of version
        """
        return self.__version

    @property
    def user_agent(self):
        """
        Sets the attribute value of user agent
        """
        return self.__user_agent

    @property
    def product_id(self):
        """
        Sets the attribute value of product id
        """
        return self.__product_id

    @property
    def tracking_id(self):
        """
        Sets the attribute value of tracking id
        """
        return self.__tracking_id

    @property
    def api_base_url(self):
        """
        Sets the attribute value of api base url
        """
        return self.__api_base_url

    @property
    def mime_json(self):
        """
        Sets the attribute value of mime json
        """
        return self.__mime_json

    @property
    def mime_form(self):
        """
        Sets the attribute value of mime form
        """
        return self.__mime_form
