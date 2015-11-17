##fix file structure it is abomination
from lib.quandl.quandl import Q
from config import configprivate as cfgp
q = Q(cfgp.APIKEY) ##apikey is required ##QUANDL_BASE_API is the default URL
##methods: Q.quicky() Q.testRoute() Q.fullquery()
##attributes: Q.APIKEY Q.BASEURL Q.RATELIMITS
print q.APIKEY
