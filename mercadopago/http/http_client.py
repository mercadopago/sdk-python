from json.encoder import JSONEncoder
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class HttpClient():

    """
    Default implementation to call all REST API`s
    """
    
    def __init__(self):
        pass
    
    def __getSession(self, maxRetries):
        retry_strategy = Retry(
            total=maxRetries,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
        )
        http = requests.Session()
        http.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        return http

    def get(self, url, headers, params=None, timeout=None, maxretries=None):
        with self.__getSession(maxretries) as session:
            api_result = session.get(url, params=params, headers=headers, timeout=timeout)
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }
        
        return response

    def post(self, url, headers, data=None, params=None, timeout=None, maxretries=None):
        with self.__getSession(maxretries) as session:
            api_result = session.post(url, params=params, data=data, headers=headers, timeout=timeout)
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

        return response

    def put(self, url, headers, data=None, params=None, timeout=None, maxretries=None):
        with self.__getSession(maxretries) as session:
            api_result = session.put(url, params=params, data=data, headers=headers, timeout=timeout)
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

        return response

    def delete(self, url, headers, params=None, timeout=None, maxretries=None):
        with self.__getSession(maxretries) as session:
            api_result = session.delete(url, params=params, headers=headers, timeout=timeout)
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

        return response
