# mercadopago/resources/add_address_schema.py

from ..core.resource import Resource


class AddAddressSchema(Resource):
    """
    Address schema resource for MercadoPago API.
    
    Represents address information with optional fields for location details.
    """
    
    _schema = {
        "city": {
            "type": "string",
            "required": False
        },
        "country": {
            "type": "string",
            "required": False
        },
        "state": {
            "type": "string",
            "required": False
        },
        "street_name": {
            "type": "string",
            "required": False
        },
        "street_number": {
            "type": "string",
            "required": False
        },
        "zip_code": {
            "type": "string",
            "required": False
        }
    }