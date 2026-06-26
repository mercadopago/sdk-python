```python
from mercadopago.core import MPBase


class Phone(MPBase):
    """
    Phone resource for MercadoPago API.
    
    Represents phone information with area code and number.
    """

    def __init__(self, client):
        """
        Initialize Phone resource.
        
        Args:
            client: MercadoPago client instance
        """
        super().__init__(client)
        self._schema = {
            "area_code": str,
            "number": str
        }

    @property
    def schema(self):
        """
        Get the phone schema.
        
        Returns:
            dict: Schema definition with area_code and number as strings
        """
        return self._schema
```