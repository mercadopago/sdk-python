import sys
sys.path.append("../")


from mercadopago.resources.card import Card
from mercadopago.resources.card_token import CardToken
from mercadopago.resources.customer import Customer
from mercadopago.resources.merchant_order import MerchantOrder
from mercadopago.resources.payment import Payment
from mercadopago.resources.preference import Preference
from mercadopago.core.request_options import RequestOptions
from mercadopago.sdk import SDK


sdk = SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")
request_options = RequestOptions(access_token="APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")

id = "0000001"

#PAYMENT
#payment = sdk.payment()
#print(payment.search({}, request_options)) #SEARCH LINHAS 15-24 OK!!
#print(payment.find_by_id(id, request_options)) #SEARCH LINHAS 26-32


#PREFERENCE
#preference = sdk.preference()
#print(preference.search(id)) #SEARCH LINHAS 15-24 OK!!


#CARD
#card = sdk.card()
#print(card.find_by_id(id, request_options))


#CARD TOKEN
#card_token = sdk.card_token()
#print(card_token.find_by_id(id, request_options))


#CUSTOMER
#customer = sdk.customer()
#print(customer.search({}, request_options))


#MERCHANT ORDER
#merchant_order = sdk.merchant_order()
#print(merchant_order.search(id))