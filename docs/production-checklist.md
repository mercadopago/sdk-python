# Production checklist

Use this checklist after the first successful sandbox request and before sending production traffic.

## Credentials and isolation

- Load access tokens and webhook secrets from a secret manager or environment variables.
- Confirm that production and test credentials cannot be selected by untrusted input.
- Set corporation, integrator, or platform identifiers only when assigned to the integration.

## Reliable writes

- Generate and persist one idempotency key per logical write operation.
- Reuse that key only for retries of the same payload.
- Reconcile an unknown outcome after a timeout or `MPConnectionError` before writing again.
- Keep SDK, framework, and queue retries within one bounded end-to-end deadline.

## Webhooks

- Validate signatures before trusting signed notifications.
- Keep server clocks synchronized and choose an explicit timestamp tolerance.
- Deduplicate deliveries, acknowledge promptly, and process asynchronously.
- Fetch the current API resource and make state transitions idempotent.

## Observability and support

- Record operation name, latency, attempt count, status, SDK error type, request ID, and an application correlation ID.
- Alert on sustained authentication, validation, rate-limit, and server-error changes separately.
- Exclude credentials, card data, full request bodies, webhook secrets, and complete signatures from logs.
- Pin a tested SDK version and review release notes before upgrading.

Keep a minimal sanitized reproduction and the installed SDK/Python versions available for repository issues.
