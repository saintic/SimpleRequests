# coding:utf8
# taochengwei <staugur@saintic.com> @2016-09-21

__version__ = '0.2'
__doc__     = 'request url for json type'

import json, httplib, urllib, logging
try:
    import urlparse
except ImportError:
    from urllib.parse import urlparse


logging.basicConfig(
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
    )

class RequestsException(httplib.HTTPException):
    pass

class RequestsParamError(RequestsException):
    pass

class Requests:

    '''Request API URL type RESTful, return the dictionary data'''

    def __init__(self, url=None, timeout=5):

        self.url     = url
        self.timeout = timeout
        self.headers = {"User-Agent": "SimpleRequestsAgent"}
        self.jsonde  = json.JSONDecoder()
        self.jsonen  = json.JSONEncoder()

    def _url_split(self, url):
        if isinstance(url, (str, unicode)):
            _url = urlparse.urlparse(url)
            return _url.scheme, _url.netloc, _url.path, _url.query
        else:
            raise RequestsParamError

    def get(self, url=None, headers=None, timeout=None):
        """ http method get function """

        if headers and not isinstance(headers, dict):
            raise RequestsParamError("headers not None or dict")
        if timeout and not isinstance(timeout, int):
            raise RequestsParamError("timeout not None or integer")

        url     = self.url or url
        headers = headers or self.headers
        timeout = timeout or self.timeout
        scheme, netloc, path, query = self._url_split(url)
        if query:
            uri = '%s?%s' %(path, query)
        else:
            uri = path
        netloc  = netloc.split(':')
        if len(netloc) == 2:
            server, port = netloc
        else:
            server = netloc[0]
            port   = 443 if scheme == 'https' else 80

        try:
            if scheme == 'https':
                httpClient = httplib.HTTPSConnection(host=server, port=port, timeout=timeout)
            else:
                httpClient = httplib.HTTPConnection(host=server, port=port, timeout=timeout)
            httpClient.request(method='GET', url=uri, headers=headers)
            response = httpClient.getresponse()
            content  = response.read()  # here is str type
            data     = self.jsonde.decode(content)  # convert str to dict
            httpClient.close()
        except Exception,e:
            logging.error(e, exc_info=True)
            data = {}
        return data

    def post(self, url=None, data=None, headers=None, timeout=None):
        """ http method get function """

        if headers and not isinstance(headers, dict):
            raise RequestsParamError("headers not None or dict")
        if timeout and not isinstance(timeout, int):
            raise RequestsParamError("timeout not None or integer")
        if data and not isinstance(data, dict):
            raise RequestsParamError("data not None or dict")

        url     = self.url or url
        headers = headers or self.headers
        timeout = timeout or self.timeout
        scheme, netloc, path, query = self._url_split(url)
        if query:
            uri = '%s?%s' %(path, query)
        else:
            uri = path
        netloc  = netloc.split(':')
        if len(netloc) == 2:
            server, port = netloc
        else:
            server = netloc[0]
            port   = 443 if scheme == 'https' else 80

        try:
            if scheme == 'https':
                httpClient = httplib.HTTPSConnection(host=server, port=port, timeout=timeout)
            else:
                httpClient = httplib.HTTPConnection(host=server, port=port, timeout=timeout)
            httpClient.request(method='POST', url=uri, body=data, headers=headers)
            response = httpClient.getresponse()
            content  = response.read()  # here is str type
            data     = self.jsonde.decode(content)  # convert str to dict
            httpClient.close()
        except Exception,e:
            logging.error(e, exc_info=True)
            data = {}
        return data

    def put(self, url=None, data=None, headers=None, timeout=None):
        """ http method get function """

        if headers and not isinstance(headers, dict):
            raise RequestsParamError("headers not None or dict")
        if timeout and not isinstance(timeout, int):
            raise RequestsParamError("timeout not None or integer")
        if data and not isinstance(data, dict):
            raise RequestsParamError("data not None or dict")

        url     = self.url or url
        headers = headers or self.headers
        timeout = timeout or self.timeout
        scheme, netloc, path, query = self._url_split(url)
        if query:
            uri = '%s?%s' %(path, query)
        else:
            uri = path
        netloc  = netloc.split(':')
        if len(netloc) == 2:
            server, port = netloc
        else:
            server = netloc[0]
            port   = 443 if scheme == 'https' else 80

        try:
            if scheme == 'https':
                httpClient = httplib.HTTPSConnection(host=server, port=port, timeout=timeout)
            else:
                httpClient = httplib.HTTPConnection(host=server, port=port, timeout=timeout)
            httpClient.request(method='PUT', url=uri, body=data, headers=headers)
            response = httpClient.getresponse()
            content  = response.read()  # here is str type
            data     = self.jsonde.decode(content)  # convert str to dict
            httpClient.close()
        except Exception,e:
            logging.error(e, exc_info=True)
            data = {}
        return data

    def delete(self, url=None, data=None, headers=None, timeout=None):
        """ http method get function """

        if headers and not isinstance(headers, dict):
            raise RequestsParamError("headers not None or dict")
        if timeout and not isinstance(timeout, int):
            raise RequestsParamError("timeout not None or integer")
        if data and not isinstance(data, dict):
            raise RequestsParamError("data not None or dict")

        url     = self.url or url
        headers = headers or self.headers
        timeout = timeout or self.timeout
        scheme, netloc, path, query = self._url_split(url)
        if query:
            uri = '%s?%s' %(path, query)
        else:
            uri = path
        netloc  = netloc.split(':')
        if len(netloc) == 2:
            server, port = netloc
        else:
            server = netloc[0]
            port   = 443 if scheme == 'https' else 80

        try:
            if scheme == 'https':
                httpClient = httplib.HTTPSConnection(host=server, port=port, timeout=timeout)
            else:
                httpClient = httplib.HTTPConnection(host=server, port=port, timeout=timeout)
            httpClient.request(method='DELETE', url=uri, body=data, headers=headers)
            response = httpClient.getresponse()
            content  = response.read()  # here is str type
            data     = self.jsonde.decode(content)  # convert str to dict
            httpClient.close()
        except Exception,e:
            logging.error(e, exc_info=True)
            data = {}
        return data
