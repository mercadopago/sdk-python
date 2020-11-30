from json.encoder import JSONEncoder
import requests

class HttpClient():

    """
    gdfbdgh
    """
    
    def __init__(self):
        pass

    def get_session(self):
        """Creates and returns a ready-to-use requests.
        Session, with all thecustomizations made to access MP
        """
        
        session = requests.Session()
        return session

    def get(self, url, headers, params=None, timeout=None):
        s = self.get_session()

        api_result = s.get(url, params=params, headers=headers, timeout=timeout)

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response

    def post(self, url, headers, data=None, params=None, timeout=None):
        s = self.get_session()

        api_result = s.post(url, params=params, data=data, headers=headers, timeout=timeout)

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response

    def put(self, url, headers, data=None, params=None, timeout=None):
        s = self.get_session()

        api_result = s.put(url, params=params, data=data, headers=headers, timeout=timeout)

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response

    def delete(self, url, headers, params=None, timeout=None):
        s = self.get_session()

        api_result = s.delete(url, params=params, headers=headers, timeout=timeout)

        response = {
            "status": api_result.status_code,
            "response": api_result.json()
        }

        return response
