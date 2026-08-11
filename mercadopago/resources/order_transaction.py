"""Dataclasses for the transactions payload in Orders API requests.

These dataclasses model the ``transactions.payments[]`` structure of the
``POST /v1/orders`` request body. They complete the typed chain started by
:class:`~mercadopago.resources.order_create.OrderCreateRequest`, allowing
Automatic Payments fields to be built without raw dicts.

The plain dict path continues to work unchanged; these dataclasses are
purely additive.
"""
from dataclasses import dataclass
from typing import (
    List,
    Optional,
)

from mercadopago.resources.order_automatic_payments import OrderAutomaticPayments
from mercadopago.resources.order_stored_credential import OrderStoredCredential
from mercadopago.resources.order_subscription_data import OrderSubscriptionData


@dataclass
class OrderPaymentMethodRequest:
    """Payment method details for a transaction within an order.

    Attributes:
        id: Payment method identifier (e.g. ``"master"``). Type: str.
        type: Payment method type (e.g. ``"credit_card"``). Type: str.
        token: Tokenized card identifier. Type: str.
        installments: Number of installments. Type: int.
        statement_descriptor: Descriptor shown on the cardholder statement.
            Type: str.
        financial_institution: Financial institution code (e.g. PSE). Type: str.
    """

    id: Optional[str] = None
    type: Optional[str] = None
    token: Optional[str] = None
    installments: Optional[int] = None
    statement_descriptor: Optional[str] = None
    financial_institution: Optional[str] = None


@dataclass
class OrderPaymentRequest:
    """A single payment transaction within an order.

    Use this dataclass to build an entry of the ``transactions.payments``
    array. It provides a fully typed path to all Automatic Payments fields
    (``automatic_payments``, ``stored_credential``, ``subscription_data``).

    Attributes:
        amount: Payment amount as a decimal string. Type: str.
        expiration_time: ISO 8601 duration or date-time for expiration.
            Type: str.
        date_of_expiration: ISO 8601 date-time after which the payment
            can no longer be collected. Type: str.
        payment_method: Payment method details.
        automatic_payments: Automatic (recurring) payment configuration.
        stored_credential: Card-on-file metadata for recurring charges.
        subscription_data: Subscription billing data for this payment.
    """

    amount: Optional[str] = None
    expiration_time: Optional[str] = None
    date_of_expiration: Optional[str] = None
    payment_method: Optional[OrderPaymentMethodRequest] = None
    automatic_payments: Optional[OrderAutomaticPayments] = None
    stored_credential: Optional[OrderStoredCredential] = None
    subscription_data: Optional[OrderSubscriptionData] = None


@dataclass
class OrderTransactionRequest:
    """Transactions payload for an order creation request.

    Attributes:
        payments: List of payment transactions for the order.
    """

    payments: Optional[List[OrderPaymentRequest]] = None
