# Troubleshooting

## `401 Unauthorized`

Confirm that `MP_ACCESS_TOKEN` belongs to the intended account and environment. Do not send a public key as an access token.

## `409` or a reused idempotency key

Use the same key only when retrying the same logical operation. Use a new key for a new order or payment.

## `422 Unprocessable Entity`

Inspect `MPValidationError.causes`. Verify required fields, amounts, currency, payer data, and the selected payment method.

## Requests time out

Set `connection_timeout` explicitly and keep retries bounded. A larger timeout does not fix invalid credentials or payloads.

## Webhook validation fails

Pass `x-signature`, `x-request-id`, and `data.id` exactly as received. Check the application webhook secret and server clock.

## An SDK symbol cannot be imported

Check the installed package version with `python -m pip show mercadopago` and compare it with the repository changelog.

## Escalating an issue

Include the SDK and Python versions, operation, HTTP status, request ID, sanitized exception type/message, and a minimal reproduction. Open a repository issue without credentials, card data, webhook secrets, or exploit details.
