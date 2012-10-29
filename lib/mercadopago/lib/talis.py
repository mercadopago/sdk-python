import urllib2

from urllib2 import urlparse

from restful_lib import Connection

from gae_restful_lib import GAE_Connection

from datetime import datetime

from StringIO import StringIO

from xml.etree import ElementTree as ET

SPARQL_ENDPOINT = "/services/sparql"
META_ENDPOINT = "/meta"
CONTENT_ENDPOINT = "/items"
JOB_REQUESTS = "/jobs"
SNAPSHOTS = "/snapshots"
SNAPSHOT_TEMPLATE = "/snapshots/%s"

RESET_STORE_TEMPLATE = u"""<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:bf="http://schemas.talis.com/2006/bigfoot/configuration#" > 
  <bf:JobRequest>
    <rdfs:label>%s</rdfs:label>
    <bf:jobType rdf:resource="http://schemas.talis.com/2006/bigfoot/configuration#ResetDataJob"/>
    <bf:startTime>%sZ</bf:startTime>
  </bf:JobRequest>
 </rdf:RDF>"""

SNAPSHOT_STORE_TEMPLATE = """<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:bf="http://schemas.talis.com/2006/bigfoot/configuration#" > 
  <bf:JobRequest>
    <rdfs:label>%s</rdfs:label>
    <bf:jobType rdf:resource="http://schemas.talis.com/2006/bigfoot/configuration#SnapshotJob"/>
    <bf:startTime>%sZ</bf:startTime>
  </bf:JobRequest>
 </rdf:RDF>"""

SNAPSHOT_RESTORE_TEMPLATE = """<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:bf="http://schemas.talis.com/2006/bigfoot/configuration#" > 
  <bf:JobRequest>
    <rdfs:label>%s</rdfs:label>
    <bf:jobType rdf:resource="http://schemas.talis.com/2006/bigfoot/configuration#RestoreJob"/>
    <bf:snapshotUri rdf:resource="%s" />
    <bf:startTime>%sZ</bf:startTime>
  </bf:JobRequest>
 </rdf:RDF>"""

class RDFFormatException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Store():
    def __init__(self, base_store_url, username=None, password=None):
        """ Base URL for the store should be pretty self-explanatory. E.g. something like
            "http://api.talis.com/stores/store_name"
            Only needs to enter the username/password if this class is going to tinker
            with things."""
        if base_store_url.endswith('/'):
            base_store_url = base_store_url[:-1]

        self.base_store_url = base_store_url
        # Split the given URL
        if base_store_url:
            self.conn = Connection(base_store_url, username=username, password=password)

    def does_snapshot_exist(self, snapshot_filename):
        # Test to see if snapshot exists:
        snapshot_path = SNAPSHOT_TEMPLATE % snapshot_filename
        
        response = self.conn.request(snapshot_path, method = "HEAD")
        
        if response.get('headers') and response.get('headers').get('status'):
            status = response.get('headers').get('status')
        
            if status in ['200', '204']:
                return True
            elif status.startswith('4'):
                return False
            # else: raise Error?

        return False

    def schedule_reset_data(self, label, at_time=None):
        """Will request that the store is emptied, and label the request. 
           If a time is given as an ISO8601 formatted string, this will be 
           the scheduled time for the snapshot. Otherwise, it will use the current time."""
        if not at_time:
            at_time=datetime.utcnow().isoformat().split('.')[0]
        
        snapshot_request = RESET_STORE_TEMPLATE % (label, at_time)
        
        return self.conn.request_post(JOB_REQUESTS, body = snapshot_request, headers={'Content-Type':'application/rdf+xml'})

    def schedule_snapshot_data(self, label, at_time=None):
        """Will request a snapshot be made of the store. 
           If a time is given as an ISO8601 formatted string, this will be 
           the scheduled time for the snapshot. Otherwise, it will use the current time."""
        if not at_time:
            at_time=datetime.utcnow().isoformat().split('.')[0]
        
        snapshot_request = SNAPSHOT_STORE_TEMPLATE % (label, at_time)
        
        return self.conn.request_post(JOB_REQUESTS, body = snapshot_request, headers={'Content-Type':'application/rdf+xml'})
        
    def schedule_snapshot_restore(self, label, snapshot_filename, at_time=None):
        """Will request that the store is restored from a snapshot. If a time is given as
           an ISO8601 formatted string, this will be the scheduled time for
           the recovery. Otherwise, it will use the current time."""
        if not at_time:
            at_time=datetime.utcnow().isoformat().split('.')[0]
        
        # Test to see if snapshot exists:
        snapshot_path = SNAPSHOT_TEMPLATE % snapshot_filename
        
        if self.does_snapshot_exist(snapshot_filename):
            snapshot_uri = "%s%s" % (self.base_store_url, snapshot_path)
            snapshot_request = SNAPSHOT_RESTORE_TEMPLATE % (label, snapshot_uri, at_time)    
            return self.conn.request_post(JOB_REQUESTS, body = snapshot_request, headers={'Content-Type':'application/rdf+xml'})
            
    def submit_rdfxml(self, rdf_text):
        """Puts the given RDF/XML into the Talis Store"""
        return self._put_rdf(rdf_text, mimetype="application/rdf+xml")
        
    def _put_rdf(self, rdf_text, mimetype="application/rdf+xml"):
        """Placeholder for allowing other serialisation types to be put into a
           Talis store, whether the conversion takes place here, or if the Talis
           store starts to accept other formats."""
        if rdf_text:
            request_headers = {}
            if mimetype not in ['application/rdf+xml']:
                raise RDFFormatException("%s is not an allowed RDF serialisation format" % mimetype)
            request_headers['Content-Type'] = mimetype
            return self.conn.request_post(META_ENDPOINT, body=rdf_text, headers=request_headers)        
                 
    def _query_sparql_service(self, query, args={}):
        """Low-level SPARQL query - returns the message and response headers from the server.
           You may be looking for Store.sparql instead of this."""
        passed_args = {'query':query}
        passed_args.update(args)
        return self.conn.request_get(SPARQL_ENDPOINT, args=passed_args, headers={'Content-type':'application/x-www-form-urlencoded'})
        
    def _query_search_service(self, query, args={}):
        """Low-level content box query - returns the message and response headers from the server.
           You may be looking for Store.search instead of this."""
           
        passed_args = {'query':query}
        passed_args.update(args)
        
        return self.conn.request_get(CONTENT_ENDPOINT, args=passed_args, headers={'Content-type':'application/x-www-form-urlencoded'} )
        
    def _list_snapshots(self, passed_args={}):
        return self.conn.request_get(SNAPSHOTS, args=passed_args, headers={}) 
        
##############################################################################
# Convenience Functions
##############################################################################

    def submit_rdfxml_from_url(self, url_to_file, headers={"Accept":"application/rdf+xml"}):
        """Convenience method - downloads the file from a given url, and then pushes that
           into the meta store. Currently, it doesn't put it through a parse-> reserialise
           step, so that it could handle more than rdf/xml on the way it but it is a
           future possibility."""
        import_rdf_connection = Connection(url_to_file)
        response = import_rdf_connection.request_get("", headers=headers)
        
        if response.get('headers') and response.get('headers').get('status') in ['200', '204']:
            request_headers = {}
            
            # Lowercase all response header fields, to make matching easier. 
            # According to HTTP spec, they should be case-insensitive
            response_headers = response['headers']
            for header in response_headers:
                response_headers[header.lower()] = response_headers[header]
                
            # Set the body content
            body = response.get('body').encode('UTF-8')
            
            # Get the response mimetype
            rdf_type = response_headers.get('content-type', None)
            
            return self._put_rdf(body, mimetype=rdf_type)
            
    def sparql(self, query, args={}):
        """Performs a SPARQL query and simply returns the body of the response if successful
           - if there is an issue, such as a code 404 or 500, this method will return False. 
           
           Use the _query_sparql_service method to get hold of
           the complete response in this case."""
        response = self._query_sparql_service(query, args)
        headers = response.get('headers')
        
        status = headers.get('status', headers.get('Status'))
        
        if status in ['200', 200, '204', 204]:
            return response.get('body').encode('UTF-8')
        else:
            return False

    def search(self, query, args={}):
        """Performs a search query and simply returns the body of the response if successful
           - if there is an issue, such as a code 404 or 500, this method will return False. 
           
           Use the _query_search_service method to get hold of
           the complete response in this case."""
        response = self._query_search_service(query, args)
        headers = response.get('headers')
        
        status = headers.get('status', headers.get('Status'))
        
        if status in ['200', 200, '204', 204]:
            parsed_atom = Atom_Search_Results(response.get('body').encode('UTF-8'))
            return parsed_atom.get_item_list()
        else:
            return False
            
class Item():
    def __init__(self):
        self.title = None
        self.link = None

class Atom_Search_Results():
    def __init__(self, atom_text):
        self.load_atom_search(atom_text)
    
    def load_atom_search(self, atom_text):
        self.atom = ET.fromstring(atom_text)
    
    def get_item_list(self):
        if self.atom:
            items = []
            for item in self.atom.findall('{http://purl.org/rss/1.0/}item'):
                item_fields = Item()
                item_fields.title = item.find('{http://purl.org/rss/1.0/}title').text
                item_fields.link = item.find('{http://purl.org/rss/1.0/}link').text
                items.append(item_fields)
                
            return items
            
class GAE_Store(Store):
    def __init__(self, base_store_url, username=None, password=None):
        """ Base URL for the store should be pretty self-explanatory. E.g. something like
            "http://api.talis.com/stores/store_name"
            The username and password will not do anything, until the Google app engine's
            fetch library handles authentication, if ever."""
        if base_store_url.endswith('/'):
            base_store_url = base_store_url[:-1]

        self.base_store_url = base_store_url
        # Split the given URL
        if base_store_url:
            self.conn = GAE_Connection(base_store_url, username, password)

