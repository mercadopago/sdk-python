from mercadopago.resources.base import ResourceBase


class Phone(ResourceBase):
    """Phone resource for MercadoPago API."""

    _schema = {
        "area_code": str,
        "number": str,
    }

    def __init__(self, area_code=None, number=None):
        """
        Initialize Phone resource.

        Args:
            area_code (str, optional): Area code of the phone number.
            number (str, optional): Phone number.
        """
        self.area_code = area_code
        self.number = number