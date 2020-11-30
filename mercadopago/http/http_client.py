from json.encoder import JSONEncoder
import requests

class HttpClient():

    """
    Default implementation to call all REST API`s
    """
    
    def __init__(self):
        pass

    def get(self, url, headers, params=None, timeout=None):
        with requests.get(url, params=params, headers=headers, timeout=timeout) as api_result:
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

        return response

    def post(self, url, headers, data=None, params=None, timeout=None):
        with requests.post(url, params=params, data=data, headers=headers, timeout=timeout) as api_result:
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

        return response

    def put(self, url, headers, data=None, params=None, timeout=None):
        with requests.put(url, params=params, data=data, headers=headers, timeout=timeout) as api_result:
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

        return response

    def delete(self, url, headers, params=None, timeout=None):
        with requests.delete(url, params=params, headers=headers, timeout=timeout) as api_result:
            response = {
                "status": api_result.status_code,
                "response": api_result.json()
            }

        return response
