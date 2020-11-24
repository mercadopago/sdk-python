import sys
sys.path.append('../')

from mercadopago.SDK import Sdk
from mercadopago.resources.Payment import Payment
from mercadopago.core.RequestOptions import RequestOptions

SDK = Sdk('APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966')
requestOptions = RequestOptions(accessToken='APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966')

payment = Payment(SDK)
print(payment.search({}, requestOptions))

