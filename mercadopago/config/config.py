"""SDK-level configuration constants.

Centralises version information, API base URL, MIME types, and tracking
identifiers used by every HTTP request the SDK makes.  All values are
read-only after initialisation.
"""
import platform


class Config:
    """Read-only container for SDK-wide constants and tracking metadata.

    An instance is created internally by :class:`~mercadopago.core.mp_base.MPBase`
    and should not need to be instantiated by end-users.

    Attributes:
        version: Semantic version string of this SDK release.
        user_agent: User-Agent header value sent with every request.
        product_id: MercadoPago-assigned product identifier for this SDK.
        tracking_id: Composite string with Python version and SDK version
            used by MercadoPago for telemetry.
        api_base_url: Root URL for all MercadoPago REST API calls.
        mime_json: MIME type for JSON payloads.
        mime_form: MIME type for form-encoded payloads.
    """

    def __init__(self):
        """Builds version-dependent values (user_agent, tracking_id)."""
        self.__version = "3.0.2"
        self.__user_agent = "MercadoPago Python SDK v" + self.__version
        self.__product_id = "bc32bpftrpp001u8nhlg"
        self.__tracking_id = "platform:" + platform.python_version()
        self.__tracking_id += ",type:SDK" + self.__version + ",so;"

    __api_base_url = "https://api.mercadopago.com"
    __mime_json = "application/json"
    __mime_form = "application/x-www-form-urlencoded"

    @property
    def version(self):
        """Semantic version of the SDK (e.g. ``'2.4.0'``)."""
        return self.__version

    @property
    def user_agent(self):
        """User-Agent header value identifying this SDK."""
        return self.__user_agent

    @property
    def product_id(self):
        """MercadoPago-assigned product identifier for SDK tracking."""
        return self.__product_id

    @property
    def tracking_id(self):
        """Composite tracking string with Python and SDK versions."""
        return self.__tracking_id

    @property
    def api_base_url(self):
        """Root URL for MercadoPago REST API calls."""
        return self.__api_base_url

    @property
    def mime_json(self):
        """MIME type for JSON request/response bodies."""
        return self.__mime_json

    @property
    def mime_form(self):
        """MIME type for form-encoded request bodies."""
        return self.__mime_form
