"""MercadoPago API resource classes.

Each class maps to a MercadoPago REST API domain (payments, orders,
customers, etc.) and exposes CRUD and action methods.  All resources
extend :class:`~mercadopago.core.mp_base.MPBase`.
"""
from mercadopago.config.request_options import RequestOptions
from mercadopago.http.http_client import HttpClient
from mercadopago.resources.advanced_payment import AdvancedPayment
from mercadopago.resources.card import Card
from mercadopago.resources.card_token import CardToken
from mercadopago.resources.chargeback import Chargeback
from mercadopago.resources.customer import Customer
from mercadopago.resources.disbursement_refund import DisbursementRefund
from mercadopago.resources.identification_type import IdentificationType
from mercadopago.resources.invoice import Invoice
from mercadopago.resources.merchant_order import MerchantOrder
from mercadopago.resources.oauth import OAuth
from mercadopago.resources.order import Order
from mercadopago.resources.order_automatic_payments import OrderAutomaticPayments
from mercadopago.resources.order_checkout_pro import (
    OrderCheckoutProConfig,
    OrderCheckoutProInstallments,
    OrderCheckoutProInterestFree,
    OrderCheckoutProOnlineConfig,
    OrderCheckoutProPaymentMethod,
    OrderCheckoutProTrack,
    OrderCheckoutProDict,
)
from mercadopago.resources.order_create import (
    OrderCreateRequest,
    OrderIdentification,
    OrderPayerRequest,
    order_request_to_dict,
)
from mercadopago.resources.order_integration_data import (
    OrderIntegrationData,
    OrderSponsor,
)
from mercadopago.resources.order_item import OrderItemRequest
from mercadopago.resources.order_payer import (
    OrderPayerAddress,
    OrderPayerPhone,
)
from mercadopago.resources.order_shipment import (
    OrderShipmentAddress,
    OrderShipmentFreeMethod,
    OrderShipmentRequest,
)
from mercadopago.resources.order_stored_credential import OrderStoredCredential
from mercadopago.resources.order_subscription_data import (
    OrderInvoicePeriod,
    OrderSubscriptionData,
    OrderSubscriptionSequence,
)
from mercadopago.resources.order_transaction_security import OrderTransactionSecurity
from mercadopago.resources.payment import Payment
from mercadopago.resources.payment_methods import PaymentMethods
from mercadopago.resources.plan import Plan
from mercadopago.resources.point import Point
from mercadopago.resources.preapproval import PreApproval
from mercadopago.resources.preference import Preference
from mercadopago.resources.refund import Refund
from mercadopago.resources.subscription import Subscription
from mercadopago.resources.user import User


__all__ = (
    'AdvancedPayment',
    'Card',
    'CardToken',
    'Chargeback',
    'Customer',
    'DisbursementRefund',
    'HttpClient',
    'IdentificationType',
    'Invoice',
    'MerchantOrder',
    'OAuth',
    'Order',
    'OrderAutomaticPayments',
    'OrderCheckoutProConfig',
    'OrderCheckoutProInstallments',
    'OrderCheckoutProInterestFree',
    'OrderCheckoutProOnlineConfig',
    'OrderCheckoutProPaymentMethod',
    'OrderCheckoutProTrack',
    'OrderCheckoutProDict',
    'OrderCreateRequest',
    'OrderIdentification',
    'OrderIntegrationData',
    'OrderInvoicePeriod',
    'OrderItemRequest',
    'OrderPayerAddress',
    'OrderPayerPhone',
    'OrderPayerRequest',
    'OrderShipmentAddress',
    'OrderShipmentFreeMethod',
    'OrderShipmentRequest',
    'OrderSponsor',
    'OrderStoredCredential',
    'OrderSubscriptionData',
    'OrderSubscriptionSequence',
    'OrderTransactionSecurity',
    'Payment',
    'PaymentMethods',
    'Plan',
    'Point',
    'PreApproval',
    'Preference',
    'Refund',
    'RequestOptions',
    'Subscription',
    'User',
    'order_request_to_dict',
)
