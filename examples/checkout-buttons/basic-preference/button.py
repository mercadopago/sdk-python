# coding: utf-8

from wsgiref import util
from string import Template
import json
import os
import sys

# Import Mercadopago library
sys.path.append(os.path.dirname(__file__)+"../../../lib")
import mercadopago

# Templates
wrapper = Template("""
<!doctype html>
<html>
    <head>
        <title>MercadoPago SDK - Create Preference and Show Checkout Example</title>
    </head>
  <body>
    <a href="$url" name="MP-payButton" class="blue-l-arall-rn">Pagar</a>
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
    <script type="text/javascript" src="http://mp-tools.mlstatic.com/buttons/render.beta.js"></script>
  </body>
</html>
""")

four_oh_four = Template("""
<html><body>
  <h1>404-ed!</h1>
  The requested URL <i>$url</i> was not found.
</body></html>""")

# Template Variables for each page
pages = {
    'index': { 'url':'http://default-url.com'}
    }

def handle_request(environment, start_response):

  try:
    #fn = util.shift_path_info(environment)
    #print "------------------------------"+fn
    #if fn == python:
    fn = 'index'
    response = wrapper.substitute(**pages[fn])
    start_response('200 OK', [('content-type', 'text/html')])

    #MP integration
    preference = {
      "items": [
        {
          "title": "sdk-python",
          "quantity": 1,
          "currency_id": "ARS",
          "unit_price": 10.5
        }
      ]
    }
    mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")

    preferenceResult = mp.create_preference(preference)

    checkoutURL = preferenceResult["response"]["init_point"]

    response = (wrapper.substitute(url=checkoutURL)).encode('utf-8')

    return [response]

  except Exception, err:
    print Exception, err
    start_response('404 Not Found', [('content-type', 'text/html')])
    response = four_oh_four.substitute(url=util.request_url(environ))
    return [response]

if __name__ == '__main__':

  from wsgiref import simple_server

  print("Starting server on port 8081...")

  try:
    simple_server.make_server('', 8081, handle_request).serve_forever()

  except KeyboardInterrupt:
    print("Ctrl-C caught, Server exiting...")
