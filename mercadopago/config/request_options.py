"""Per-request configuration for MercadoPago API calls.

Holds authentication credentials, timeout, retry policy, and any custom
or platform-specific headers that should be sent with a request.
"""
import uuid

from .config import Config
from .defaults import (
    DEFAULT_INITIAL_DELAY,
    DEFAULT_MAX_DELAY,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT_SECONDS,
)


class RequestOptions:  # pylint: disable=too-many-instance-attributes

    """Mutable configuration applied to each REST call made by a resource.

    Callers may create a default instance via :class:`~mercadopago.sdk.SDK` and
    override it per-call by passing a different ``RequestOptions`` to any
    resource method.

    Attributes:
        access_token: OAuth access token for the MercadoPago API.
        connection_timeout: Seconds before a request times out.
        custom_headers: Extra headers merged into every request.
        max_retries: Maximum automatic retries on transient failures.
        corporation_id: Optional corporation identifier header.
        integrator_id: Optional integrator identifier header.
        platform_id: Optional platform identifier header.
    """

    __access_token = None
    __connection_timeout = None
    __custom_headers = None
    __max_retries = None
    __corporation_id = None
    __integrator_id = None
    __platform_id = None
    __initial_delay = None
    __max_delay = None
    __jitter = None
    __retry_on = None
    __on_retry = None

    def __init__(  # pylint: disable=too-many-positional-arguments
    # pylint: disable=too-many-arguments
        self,
        access_token=None,
        connection_timeout=DEFAULT_TIMEOUT_SECONDS,
        custom_headers=None,
        corporation_id=None,
        integrator_id=None,
        platform_id=None,
        max_retries=DEFAULT_MAX_RETRIES,
        initial_delay=DEFAULT_INITIAL_DELAY,
        max_delay=DEFAULT_MAX_DELAY,
        jitter=None,
        retry_on=None,
        on_retry=None,
    ):
        """Initialises request options with sensible defaults.

        Every parameter is validated through its property setter.  Pass only
        the values you need to override; the rest keep their defaults.

        Args:
            access_token: OAuth access token. Obtain one from the
                `MercadoPago credentials page
                <https://www.mercadopago.com/mlb/account/credentials>`_.
            connection_timeout: Request timeout in seconds. Defaults to 60.0.
            custom_headers: Additional headers merged into every request.
            corporation_id: Corporation identifier sent as ``x-corporation-id``.
            integrator_id: Integrator identifier sent as ``x-integrator-id``.
            platform_id: Platform identifier sent as ``x-platform-id``.
            max_retries: Retry count on transient HTTP errors. Defaults to 3.

        Raises:
            ValueError: If any parameter fails its type check.
        """

        if access_token is not None:
            self.access_token = access_token
        if connection_timeout is not None:
            self.connection_timeout = connection_timeout
        if custom_headers is not None:
            self.custom_headers = custom_headers
        if max_retries is not None:
            self.max_retries = max_retries
        if corporation_id is not None:
            self.corporation_id = corporation_id
        if integrator_id is not None:
            self.integrator_id = integrator_id
        if platform_id is not None:
            self.platform_id = platform_id
        self.__initial_delay = initial_delay
        self.__max_delay = max_delay
        self.__jitter = jitter
        self.__retry_on = retry_on
        self.__on_retry = on_retry

        self.__config = Config()

    def get_headers(self):
        """Builds the full header dict for an API request.

        Merges authentication, tracking, idempotency, and any optional
        platform/integrator/corporation headers plus user-supplied
        ``custom_headers`` into a single dict ready for ``requests``.

        Returns:
            dict: Header name-value pairs.
        """
        headers = {"Authorization": "Bearer " + self.__access_token,
                   "x-product-id": self.__config.product_id,
                   "x-tracking-id": self.__config.tracking_id,
                   "x-idempotency-key": str(uuid.uuid4().int),
                   "User-Agent": self.__config.user_agent,
                   "Accept": self.__config.mime_json}

        if self.__corporation_id is not None:
            headers["x-corporation-id"] = self.__corporation_id

        if self.__integrator_id is not None:
            headers["x-integrator-id"] = self.__integrator_id

        if self.__platform_id is not None:
            headers["x-platform-id"] = self.__platform_id

        if self.__custom_headers is not None:
            headers.update(self.__custom_headers)

        return headers

    @property
    def access_token(self):
        """OAuth access token used for API authentication."""
        return self.__access_token

    @access_token.setter
    def access_token(self, value):
        if not isinstance(value, str):
            raise ValueError("Param access_token must be a String")
        self.__access_token = value

    @property
    def connection_timeout(self):
        """Request timeout in seconds."""
        return self.__connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, value):
        if not isinstance(value, float):
            raise ValueError("Param connection_timeout must be a Float")
        self.__connection_timeout = value

    @property
    def corporation_id(self):
        """Corporation identifier sent as ``x-corporation-id`` header."""
        return self.__corporation_id

    @corporation_id.setter
    def corporation_id(self, value):
        if not isinstance(value, str):
            raise ValueError("Param corporation_id must be a String")
        self.__corporation_id = value

    @property
    def custom_headers(self):
        """Extra headers merged into every API request."""
        return self.__custom_headers

    @custom_headers.setter
    def custom_headers(self, value):
        if not isinstance(value, dict):
            raise ValueError("Param custom_headers must be a Dictionary")
        idem_key = value.get("x-idempotency-key")
        if idem_key is None:
            idem_key = value.get("X-Idempotency-Key")
        if idem_key is not None and not (1 <= len(str(idem_key)) <= 64):
            raise ValueError(
                "x-idempotency-key must be between 1 and 64 characters "
                f"(got {len(str(idem_key))})"
            )
        self.__custom_headers = value

    @property
    def integrator_id(self):
        """Integrator identifier sent as ``x-integrator-id`` header."""
        return self.__integrator_id

    @integrator_id.setter
    def integrator_id(self, value):
        if not isinstance(value, str):
            raise ValueError("Param integrator_id must be a String")
        self.__integrator_id = value

    @property
    def max_retries(self):
        """Maximum automatic retries on transient HTTP errors."""
        return self.__max_retries

    @max_retries.setter
    def max_retries(self, value):
        if not isinstance(value, int):
            raise ValueError("Param max_retries must be an Integer")
        self.__max_retries = value

    @property
    def platform_id(self):
        """Platform identifier sent as ``x-platform-id`` header."""
        return self.__platform_id

    @platform_id.setter
    def platform_id(self, value):
        if not isinstance(value, str):
            raise ValueError("Param platform_id must be a String")
        self.__platform_id = value

    @property
    def initial_delay(self):
        """Initial backoff delay in ms (None = no extra delay)."""
        return self.__initial_delay

    @initial_delay.setter
    def initial_delay(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("Param initial_delay must be an Integer or None")
        self.__initial_delay = value

    @property
    def max_delay(self):
        """Maximum backoff delay cap in ms."""
        return self.__max_delay

    @max_delay.setter
    def max_delay(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("Param max_delay must be an Integer or None")
        self.__max_delay = value

    @property
    def jitter(self):
        """Whether to add random jitter to retry delay."""
        return self.__jitter

    @jitter.setter
    def jitter(self, value):
        if value is not None and not isinstance(value, bool):
            raise ValueError("Param jitter must be a Boolean or None")
        self.__jitter = value

    @property
    def retry_on(self):
        """List of HTTP status codes that trigger a retry, or None for defaults."""
        return self.__retry_on

    @retry_on.setter
    def retry_on(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise ValueError("Param retry_on must be a List or None")
            for code in value:
                if not isinstance(code, int) or code < 100 or code > 599:
                    raise ValueError(f"retry_on contains invalid HTTP status code: {code}")
        self.__retry_on = value

    @property
    def on_retry(self):
        """Optional callback(attempt, error) invoked before each retry."""
        return self.__on_retry

    @on_retry.setter
    def on_retry(self, value):
        if value is not None and not callable(value):
            raise ValueError("Param on_retry must be callable or None")
        self.__on_retry = value
