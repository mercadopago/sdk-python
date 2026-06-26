"""Address schema module."""
from marshmallow import Schema, fields


class AddressSchema(Schema):
    """Address schema for MercadoPago API."""

    city = fields.Str(required=False, allow_none=True)
    country = fields.Str(required=False, allow_none=True)
    state = fields.Str(required=False, allow_none=True)
    street_name = fields.Str(required=False, allow_none=True)
    street_number = fields.Str(required=False, allow_none=True)
    zip_code = fields.Str(required=False, allow_none=True)