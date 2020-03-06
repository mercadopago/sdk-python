import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

class MPSSLAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block)