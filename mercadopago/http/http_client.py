"""
Module: http_client
"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

class HttpClient():

    """
    Default implementation to call all REST API's
    """

    def __init__(self):
        pass

    @staticmethod
    def __get_session(max_retries):
        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        http = requests.Session()
        http.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        return http

    def get(self, url, headers, params=None, timeout=None, maxretries=None): #pylint: disable=missing-function-docstring, too-many-arguments
        with self.__get_session(maxretries) as session:
            api_result = session.get(url, params=params, headers=headers, timeout=timeout)
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

        return response

    def post(self, url, headers, data=None, params=None, timeout=None, maxretries=None): #pylint: disable=missing-function-docstring, too-many-arguments
        with self.__get_session(maxretries) as session:
            api_result = session.post(url, params=params, data=data,
            headers=headers, timeout=timeout)
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

        return response

    def put(self, url, headers, data=None, params=None, timeout=None, maxretries=None): #pylint: disable=missing-function-docstring, too-many-arguments
        with self.__get_session(maxretries) as session:
            api_result = session.put(url, params=params, data=data,
            headers=headers, timeout=timeout)
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

        return response

    def delete(self, url, headers, params=None, timeout=None, maxretries=None): #pylint: disable=missing-function-docstring, too-many-arguments
        with self.__get_session(maxretries) as session:
            api_result = session.delete(url, params=params, headers=headers, timeout=timeout)
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

        return response
