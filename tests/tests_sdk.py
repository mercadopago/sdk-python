import sys
sys.path.append('../')


from mercadopago.resources.Card import Card
from mercadopago.resources.CardToken import CardToken
from mercadopago.resources.Customer import Customer
from mercadopago.resources.MerchantOrder import MerchantOrder
from mercadopago.resources.Payment import Payment
from mercadopago.resources.Preference import Preference
from mercadopago.core.RequestOptions import RequestOptions
from mercadopago.SDK import Sdk


SDK = Sdk('APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966')
requestOptions = RequestOptions(accessToken='APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966')

id = '0000001'

#PAYMENT
#payment = Payment(SDK)
#print(payment.search({}, requestOptions)) #SEARCH LINHAS 15-24 OK!!
#print(payment.find_by_id(id, requestOptions)) #SEARCH LINHAS 26-32
#print(payment.findById(id, requestOptions)) #SEARCH LINHAS 36-45


#PREFERENCE
#preference = Preference(SDK)
#print(preference.search(id)) #SEARCH LINHAS 15-24 OK!!


#CARD
#card = Card(SDK)
#print(card.find_by_id(id, requestOptions))

#CARD TOKEN
#cardToken = CardToken(SDK)
#print(cardToken.find_by_id(id, requestOptions))

#CUSTOMER
#customer = Customer()
#print(customer.search({}, requestOptions))

#MERCHAN ORDER
#merchanOrder = MerchantOrder()
#print(merchanOrder.search(id))