"""HTTP client implementation backed by the ``requests`` library.

Provides automatic retry with exponential back-off for transient server
errors (429, 500, 502, 503, 504) using ``urllib3.util.Retry``.
"""
# pylint: disable=too-many-arguments
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


class HttpClient:
    """Default HTTP transport for all MercadoPago REST calls.

    Each call creates a fresh ``requests.Session`` with a retry-aware
    HTTPS adapter, executes the request, and returns a normalised
    response dict.

    The response format returned by every method is::

        {"status": <int>, "response": <dict | list | None>}

    where *status* is the HTTP status code and *response* is the parsed
    JSON body (``None`` for 204 No Content or unparseable bodies).
    """

    def request(self, method, url, maxretries=None, **kwargs):
        """Executes an HTTP request with automatic retry.

        A new session with an HTTPS retry adapter is created per call so
        that retry state does not leak between requests.

        Args:
            method: HTTP verb (``GET``, ``POST``, ``PUT``, ``DELETE``).
            url: Fully-qualified URL to call.
            maxretries: Maximum number of retries on transient errors.
            **kwargs: Forwarded to ``requests.Session.request`` (headers,
                data, params, timeout, etc.).

        Returns:
            dict: ``{"status": <http_code>, "response": <parsed_json_or_None>}``.
        """
        retry_strategy = Retry(
            total=maxretries,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        http = requests.Session()
        http.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        with http as session:
            api_result = session.request(method, url, **kwargs)
            response = {"status": api_result.status_code, "response": None}

            if api_result.status_code != 204 and api_result.content:
                try:
                    response["response"] = api_result.json()
                except ValueError as e:
                    print(f"Failed to parse JSON: {str(e)}")
                    response["response"] = None

            return response

    def get(self, url, headers, params=None, timeout=None, maxretries=None):  # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments
        """Sends a GET request to the MercadoPago API.

        Args:
            url: Fully-qualified endpoint URL.
            headers: Request headers including authorisation.
            params: Query-string parameters.
            timeout: Connection/read timeout in seconds.
            maxretries: Retry limit for transient failures.

        Returns:
            dict: Normalised response with *status* and *response* keys.
        """
        return self.request(
            "GET",
            url=url,
            headers=headers,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def post(self, url, headers, data=None, params=None, timeout=None, maxretries=None):  # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments
        """Sends a POST request to the MercadoPago API.

        Args:
            url: Fully-qualified endpoint URL.
            headers: Request headers including authorisation.
            data: JSON-encoded request body.
            params: Query-string parameters.
            timeout: Connection/read timeout in seconds.
            maxretries: Retry limit for transient failures.

        Returns:
            dict: Normalised response with *status* and *response* keys.
        """
        return self.request(
            "POST",
            url=url,
            headers=headers,
            data=data,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def put(self, url, headers, data=None, params=None, timeout=None, maxretries=None):  # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments
        """Sends a PUT request to the MercadoPago API.

        Args:
            url: Fully-qualified endpoint URL.
            headers: Request headers including authorisation.
            data: JSON-encoded request body.
            params: Query-string parameters.
            timeout: Connection/read timeout in seconds.
            maxretries: Retry limit for transient failures.

        Returns:
            dict: Normalised response with *status* and *response* keys.
        """
        return self.request(
            "PUT",
            url=url,
            headers=headers,
            data=data,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )

    def delete(self, url, headers, params=None, timeout=None, maxretries=None):  # pylint: disable=too-many-arguments
    # pylint: disable=too-many-positional-arguments
        """Sends a DELETE request to the MercadoPago API.

        Args:
            url: Fully-qualified endpoint URL.
            headers: Request headers including authorisation.
            params: Query-string parameters.
            timeout: Connection/read timeout in seconds.
            maxretries: Retry limit for transient failures.

        Returns:
            dict: Normalised response with *status* and *response* keys.
        """
        return self.request(
            "DELETE",
            url=url,
            headers=headers,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )
