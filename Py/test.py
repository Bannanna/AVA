import unittest

from lib.quandl.quandl import Q
from config import configprivate as cfgp

q = Q(cfgp.APIKEY) ##apikey is required ##QUANDL_BASE_API is the default URL
##methods: Q.quicky() Q.testRoute() Q.fullquery()
##attributes: Q.APIKEY Q.BASEURL Q.RATELIMITS

class Test(unittest.TestCase):
    def setUp(self):
        self.Q = q
    def testEqual(self, a, b):
        self.assertEqual(a, b)
    # finish this unit test
    def testFullQuery(self, a):
        self.assertTrue(a('WIKI', 'AAPL').startsWith())
