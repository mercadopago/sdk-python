"""Default configuration constants for the MercadoPago Python SDK.

These match the current SDK behaviour so that callers who never set retry
options receive identical results to before.

Attributes:
    DEFAULT_TIMEOUT_SECONDS: Request timeout in seconds (60.0).
    DEFAULT_MAX_RETRIES: Maximum automatic retries on transient errors (3).
    DEFAULT_RETRY_ON: HTTP status codes that trigger a retry.
    DEFAULT_MAX_DELAY: Maximum delay between retries in milliseconds (30 000).
    DEFAULT_INITIAL_DELAY: Initial backoff delay in milliseconds (None = urllib3 default).
"""

DEFAULT_TIMEOUT_SECONDS = 60.0
DEFAULT_MAX_RETRIES = 3
DEFAULT_RETRY_ON = [429, 500, 502, 503, 504]
DEFAULT_MAX_DELAY = 30_000   # milliseconds
DEFAULT_INITIAL_DELAY = None  # None = no extra backoff beyond urllib3 default
