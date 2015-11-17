#TODO make a hash table of stuff from https://www.quandl.com/docs/api
# !!! dont continue developing until this hash table is done, because
# the methods below should concur !!! sleep time now

import requests, time, datetime

QUANDL_BASE_API = 'https://www.quandl.com/api/v3/'
QUANDL_WIKI_URL = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL'
# QUANDL_SAMPLE_QUERY = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL.json?' +
#                        'start_date=1985-05-01&end_date=1997-07-01&order=asc&' +
#                        'column_index=4&collapse=quarterly&transformation=rdiff'

class Q(object):
    def __init__(self, apikey, b=QUANDL_BASE_API):
        self.APIKEY = apikey
        self.BASEURL = b
        self.RATELIMITS = '2,000 calls per 10 minutes, 50,000 calls per day'
    def testRoute(self, fullroute, callback):
        return callback(request.get(fullroute)) ##get the full route, and handle the response with callback

    def quicky(self, query='datasets/WIKI/AAPL'):
        return requests.get(self.url + query)

    def _constructquerystring():
        return 'some quandl route as string to pass to requests.get()'

    def fullquery(self, ticker, start_date, end_date=time.strftime("%Y-%m-%d"), order='asc', format='j', collapse=None, transform=None): #inspired by QUANDL_SAMPLE_QUERY #format = j | c | x
        if (datetime.datetime.strptime(start_date, '%Y-%m-%d') and datetime.datetime.strptime(end_date, '%Y-%m-%d')):
            return
