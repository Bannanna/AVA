import requests

QUANDL_BASE_API = 'https://www.quandl.com/api/v3/'
# QUANDL_WIKI_URL = 'https://www.quandl.com/api/v3/datasets/WIKI/'
# QUANDL_SAMPLE_QUERY = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL.json?' +
#                        'start_date=1985-05-01&end_date=1997-07-01&order=asc&' +
#                        'column_index=4&collapse=quarterly&transformation=rdiff'

class Q(object):
    def __init__(self, b=QUANDL_BASE_API):
        self.BASEURL = b
    def testRoute(self, fullroute, callback):
        return callback(request.get(fullroute)) ##get the full route, and handle the response with callback
    def quicky(self, query):
        return requests.get(self.url + query)
    def fullquery(self, ticker, start_date, end_date=time.strftime("%Y-%m-%d"), json=True,): #inspired by QUANDL_SAMPLE_QUERY
        if (datetime.datetime.strptime(start_date, '%Y-%m-%d') && datetime.datetime.strptime(end_date, '%Y-%m-%d')): #validate date-time arguments
            try:
                request.get()
            except err:
                # handle exception
