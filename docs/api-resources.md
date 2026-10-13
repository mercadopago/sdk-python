# Supported API resources

The `SDK` object exposes resource clients through methods such as `sdk.order()` and `sdk.payment()`.

| API area | SDK resource | Common operations |
|---|---|---|
| Orders | `sdk.order()` | create, get, search, capture, process, cancel, refund |
| Payments | `sdk.payment()` | create, get, search, update, capture, cancel |
| Preferences | `sdk.preference()` | create, get, search, update |
| Customers | `sdk.customer()` | create, get, search, update, cards |
| Subscriptions | `sdk.preapproval()` | create, get, search, update |
| OAuth | `sdk.oauth()` | authorization URL, create token, refresh token |

Additional resources cover cards, chargebacks, refunds, invoices, merchant orders, payment methods, identification types, users, and advanced payments. Confirm endpoint fields in the [API reference](https://www.mercadopago.com/developers/en/reference).
