"""
MercadoPago PaymentAdditionalInfo Resource Module.

This module provides the PaymentAdditionalInfo schema for fraud scoring.
"""

from marshmallow import Schema, fields, EXCLUDE


class AddressSchema(Schema):
    """Address schema for payer and shipment information."""
    
    class Meta:
        unknown = EXCLUDE
    
    zip_code = fields.Str()
    street_name = fields.Str()
    street_number = fields.Int()
    floor = fields.Str()
    apartment = fields.Str()


class PayerSchema(Schema):
    """Payer information schema."""
    
    class Meta:
        unknown = EXCLUDE
    
    first_name = fields.Str()
    last_name = fields.Str()
    phone = fields.Dict()
    address = fields.Nested(AddressSchema)


class PaymentItemSchema(Schema):
    """Payment item schema."""
    
    class Meta:
        unknown = EXCLUDE
    
    id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    picture_url = fields.Str()
    category_id = fields.Str()
    quantity = fields.Int()
    unit_price = fields.Float()


class ShipmentsSchema(Schema):
    """Shipments information schema."""
    
    class Meta:
        unknown = EXCLUDE
    
    receiver_address = fields.Nested(AddressSchema)


class PaymentAdditionalInfoSchema(Schema):
    """
    PaymentAdditionalInfo schema for fraud scoring.
    
    This schema is used to provide additional information about a payment
    for fraud detection and prevention purposes.
    """
    
    class Meta:
        unknown = EXCLUDE
    
    items = fields.List(fields.Nested(PaymentItemSchema))
    payer = fields.Nested(PayerSchema)
    shipments = fields.Nested(ShipmentsSchema)


# Create schema instance for reuse
payment_additional_info_schema = PaymentAdditionalInfoSchema()