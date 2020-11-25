import sys
sys.path.append('../')

from mercadopago.sdk import SDK

sdk = SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")
#print(sdk.payment().search({}))

#print(sdk.payment().find_by_id("67243"))

#print(sdk.payment().save({"payment_method_id": 8734, "transaction_amount": 123.56}))

#print(sdk.payment().update("67243", {"status": "cancelled"}))
