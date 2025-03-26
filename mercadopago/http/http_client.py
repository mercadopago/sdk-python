"""
Module: http_client
"""
# pylint: disable=too-many-arguments
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


class HttpClient:
    """
    Default implementation to call all REST API's
    """

    def request(self, method, url, maxretries=None, **kwargs):
        """Makes a call to the API.

        All **kwargs are passed verbatim to ``requests.request``.
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
        """Makes a GET request to the API"""
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
        """Makes a POST request to the API"""
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
        """Makes a PUT request to the API"""
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
        """Makes a DELETE request to the API"""
        return self.request(
            "DELETE",
            url=url,
            headers=headers,
            params=params,
            timeout=timeout,
            maxretries=maxretries,
        )
