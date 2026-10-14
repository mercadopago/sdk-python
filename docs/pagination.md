# Paginate search results

Search methods accept filters such as `limit` and `offset`. Resources including payments, customers, preferences, and subscriptions also expose `search_auto_paging_iter`.

```python
for payment in sdk.payment().search_auto_paging_iter({"sort": "date_created"}, limit=100):
    print(payment["id"])
```

The iterator requests additional pages lazily. Stop the loop when you have enough results, and handle `MercadoPagoError` around the iteration because a later page can fail independently.

Use `search()` directly when you need paging metadata or explicit control over `limit` and `offset`.

For long-running jobs, make item processing idempotent and persist a business checkpoint. Automatic pagination removes offset boilerplate, but it is not a transactional snapshot: records can change while pages are being read, and a restarted scan can encounter an item again.
