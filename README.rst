MercadoPago SDK module for Payments integration
===============================================

* `Install`_
* `Basic checkout`_
* `Customized checkout`_
* `Generic methods`_

Install
-------

On Python 2.x

``pip install mercadopago``

On Python 3.x

``pip3 install mercadopago``

Basic checkout
--------------

Configure your credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Get your **CLIENT_ID** and **CLIENT_SECRET** in the following address:
    - Argentina: `https://www.mercadopago.com/mla/herramientas/aplicaciones <https://www.mercadopago.com/mla/herramientas/aplicaciones>`_
    - Brazil: `https://www.mercadopago.com/mlb/ferramentas/aplicacoes <https://www.mercadopago.com/mlb/ferramentas/aplicacoes>`_
    - México: `https://www.mercadopago.com/mlm/herramientas/aplicaciones <https://www.mercadopago.com/mlm/herramientas/aplicaciones>`_
    - Venezuela: `https://www.mercadopago.com/mlv/herramientas/aplicaciones <https://www.mercadopago.com/mlv/herramientas/aplicaciones>`_
    - Colombia: `https://www.mercadopago.com/mco/herramientas/aplicaciones <https://www.mercadopago.com/mco/herramientas/aplicaciones>`_
    - Chile: `https://www.mercadopago.com/mlc/herramientas/aplicaciones <https://www.mercadopago.com/mlc/herramientas/aplicaciones>`_

::

    import mercadopago
    import json

    mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")

Preferences
~~~~~~~~~~~

Get an existent Checkout preference
***********************************

::

    def index(req, **kwargs):
        preferenceResult = mp.get_preference("PREFERENCE_ID")
        
        return json.dumps(preferenceResult, indent=4)

Create a Checkout preference
****************************

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

Update an existent Checkout preference
**************************************

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

Payments/Collections
~~~~~~~~~~~~~~~~~~~~

Search for payments
*******************

::

    def index(req, **kwargs):
        filters = {
            "id": None,
            "external_reference": None
        }

        searchResult = mp.search_payment(filters)
        
        return json.dumps(searchResult, indent=4)

Get payment data
****************

::

    import mercadopago
    import json

    def index(req, **kwargs):
        mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")
        paymentInfo = mp.get_payment (kwargs["id"])
        
        if paymentInfo["status"] == 200:
            return json.dumps(paymentInfo, indent=4)
        else:
            return None

Cancel (only for pending payments)
**********************************

::

    def index(req, **kwargs):
        result = mp.cancel_payment("ID")
        
        // Show result
        return json.dumps(result, indent=4)


Refund (only for accredited payments)
*************************************

::

    def index(req, **kwargs):
        result = mp.refund_payment("ID")
        
        // Show result
        return json.dumps(result, indent=4)

Customized checkout
-------------------


Configure your credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Get your **ACCESS_TOKEN** in the following address:
    * Argentina: `https://www.mercadopago.com/mla/account/credentials <https://www.mercadopago.com/mla/account/credentials>`_
    * Brazil: `https://www.mercadopago.com/mlb/account/credentials <https://www.mercadopago.com/mlb/account/credentials>`_
    * Mexico: `https://www.mercadopago.com/mlm/account/credentials <https://www.mercadopago.com/mlm/account/credentials>`_
    * Venezuela: `https://www.mercadopago.com/mlv/account/credentials <https://www.mercadopago.com/mlv/account/credentials>`_
    * Colombia: `https://www.mercadopago.com/mco/account/credentials <https://www.mercadopago.com/mco/account/credentials>`_

::

    import mercadopago
    import json

    mp = mercadopago.MP("ACCESS_TOKEN")

Create payment
~~~~~~~~~~~~~~

::

    mp.post ("/v1/payments", payment_data)

Create customer
~~~~~~~~~~~~~~~

::

    mp.post ("/v1/customers", {"email": "email@test.com"})

Get customer
~~~~~~~~~~~~

::

    mp.get ("/v1/customers/CUSTOMER_ID")

* View more Custom checkout related APIs in Developers Site
    * Argentina: `https://www.mercadopago.com.ar/developers <https://www.mercadopago.com.ar/developers>`_
    * Brazil: `https://www.mercadopago.com.br/developers <https://www.mercadopago.com.br/developers>`_
    * Mexico: `https://www.mercadopago.com.mx/developers <https://www.mercadopago.com.mx/developers>`_
    * Venezuela: `https://www.mercadopago.com.ve/developers <https://www.mercadopago.com.ve/developers>`_
    * Colombia: `https://www.mercadopago.com.co/developers <https://www.mercadopago.com.co/developers>`_

Generic methods
---------------

You can access any other resource from the MercadoPago API using the generic methods:

::

    // Get a resource, with optional URL params. Also you can disable authentication for public APIs
    mp.get ("/resource/uri", [params], [authenticate=true]);

    // Create a resource with "data" and optional URL params.
    mp.post ("/resource/uri", data, [params]);

    // Update a resource with "data" and optional URL params.
    mp.put ("/resource/uri", data, [params]);

    // Delete a resource with optional URL params.
    mp.delete ("/resource/uri", [params]);

For example, if you want to get the Sites list (no params and no authentication):

::

    result = mp.get ("/sites", null, false);

    print (json.dumps(result, indent=4))

Running tests
-------------

On Python 2.x

``python setup.py test``

On Python 3.x

``python3 setup.py test``
