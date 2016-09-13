#!/usr/bin/python

import unittest
import SimpleRequests

class RequestsTest(unittest.TestCase):

    def setUp(self):
        self.url = 'https://api.saintic.com'
        self.url2= 'http://101.200.125.9:10040/user?name=admin&token=true&num=1'
        self.url3= 'https://auth.saintic.com/registry'
        self.req1= SimpleRequests.Requests()
        self.req2= SimpleRequests.Requests(self.url)

    def test_get(self):
        t1  = self.req1.get(self.url)
        t2  = self.req1.get(self.url2)
        assert dict == type(t1)
        assert dict == type(t2)
        t1  = self.req2.get(self.url)
        t2  = self.req2.get(self.url2)
        self.assertEqual(t1,t2)

    def test_post(self):
        t1 = self.req1.post(self.url3, data='')
        print t1

    def test_put(self):
        t1 = self.req1.put(self.url)
        print t1

    '''
    def test_delete(self):
        t1 = self.req1.delete('http://api.saintic.com/blog')
        print t1
    '''

if __name__ == '__main__':
    unittest.main()
