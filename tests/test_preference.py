import sys
sys.path.append('../')

from mercadopago import SDK

sdk = SDK("APP_USR-558881221729581-091712-44fdc612e60e3e638775d8b4003edd51-471763966")
#preference_id = "674474959-c947e6d9-a06f-42da-97d9-fdf7f75cd1d4"

print(sdk.preference().save({
        "items": [
            {
                "title": "Test",
                "quantity": 1,
                "currency_id": "R$",
                "unit_price": 10.4
            }
        ]
    }))
