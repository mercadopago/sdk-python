===============================================
MercadoPago SDK module for Payments integration
===============================================

Usage:
======

- Get your **CLIENT_ID** and **CLIENT_SECRET** in the following address:
    - Argentina: `<https://www.mercadopago.com/mla/herramientas/aplicaciones>`_
    - Brazil: `<https://www.mercadopago.com/mlb/ferramentas/aplicacoes>`_
    - México: `<https://www.mercadopago.com/mlm/herramientas/aplicaciones>`_
    - Venezuela: `<https://www.mercadopago.com/mlv/herramientas/aplicaciones>`_

::

    import mercadopago
    import json

    mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")

Get your Access Token:
-----------------------------

::

    def index(req, **kwargs):
        accessToken = mp.get_access_token()

        return accessToken

Using MercadoPago Checkout
==========================

Create a Checkout preference:
-----------------------------

::

    def index(req, **kwargs):
        preference = {
            "items": [
                {
                    "title": "Test",
                    "quantity": 1,
                    "currency_id": "USD",
                    "unit_price": 10.4
                }
            ]
        }

        preferenceResult = mp.create_preference(preference)

        return json.dumps(preferenceResult, indent=4)

`Others items to use
<http://developers.mercadopago.com/documentacion/recibir-pagos#glossary>`_



Get an existent Checkout preference:
------------------------------------

::

    def index(req, **kwargs):
        preferenceResult = mp.get_preference("PREFERENCE_ID")
        
        return json.dumps(preferenceResult, indent=4)


Update an existent Checkout preference:
---------------------------------------

::

    def index(req, **kwargs):
        preference = {
                "items": [
                    {
                        "title": "Test Modified",
                        "quantity": 1,
                        "currency_id": "USD",
                        "unit_price": 20.4
                    }
                ]
            }
        
        preferenceResult = mp.update_preference(id, preference)
        
        return json.dumps(preferenceResult, indent=4)


Using MercadoPago Payment
=========================

Searching:
----------

::

    def index(req, **kwargs):
        filters = {
            "id": None,
            "site_id": None,
            "external_reference": None
        }

        searchResult = mp.search_payment(filters)
        
        return json.dumps(searchResult, indent=4)

`More search examples
<http://developers.mercadopago.com/documentacion/busqueda-de-pagos-recibidos>`_

Receiving IPN notification:
---------------------------

- Go to **Mercadopago IPN configuration**:
    - Argentina: `<https://www.mercadopago.com/mla/herramientas/notificaciones>`_
    - Brazil: `<https://www.mercadopago.com/mlb/ferramentas/notificacoes>`_
    - México: `<https://www.mercadopago.com/mlm/herramientas/notificaciones>`_
    - Venezuela: `<https://www.mercadopago.com/mlv/herramientas/notificaciones>`_

::

    import mercadopago
    import json

    def index(req, **kwargs):
        mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")
        paymentInfo = mp.get_payment_info (kwargs["id"])
        
        if paymentInfo["status"] == 200:
            return json.dumps(paymentInfo, indent=4)
        else:
            return None


Cancel (only for pending payments):
-----------------------------------

::

    def index(req, **kwargs):
        result = mp.cancel_payment("ID")
        
        // Show result
        return json.dumps(result, indent=4)


Refund (only for accredited payments):
--------------------------------------

::

    def index(req, **kwargs):
        result = mp.refund_payment("ID")
        
        // Show result
        return json.dumps(result, indent=4)

`About Cancel & Refund
<http://developers.mercadopago.com/documentacion/devolucion-y-cancelacion>`_
