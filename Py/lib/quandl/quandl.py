# TODO make a hash table of stuff from https://www.quandl.com/docs/api
# !!! dont continue developing until this hash table is done, because
# the methods below should concur !!! sleep time now

import sh, time, datetime, math

QUANDL_BASE_API = 'https://www.quandl.com/api/v3/'
QUANDL_WIKI_URL = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL'
# QUANDL_SAMPLE_QUERY = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL.json?' +
#                        'start_date=1985-05-01&end_date=1997-07-01&order=asc&' +
#                        'column_index=4&collapse=quarterly&transformation=rdiff'

# The combination of database_code and dataset_code is called the Quandl code. ie WIKI/AAPL

typetable = {
    'j': '.json',
    'x': '.xml',
    'c': '.csv',
    'json': '.json',
    'xml': '.xml',
    'csv': '.csv'
}

def defaultcallback(a):
    return a
def validate_date(date_string):
    if date_string:
        try:
            datetime.datetime.strptime(date_string, '%Y-%m-%d')
        except (ValueError, TypeError):
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    else: return ''

class Q(object):
    def __init__(self, apikey, b=QUANDL_BASE_API):
        self.APIKEY = apikey
        self.BASEURL = b
        self.RATELIMITS = '2,000 calls per 10 minutes, 50,000 calls per day'

    def testRoute(self, fullroute, callback=defaultcallback):
        return callback(sh.curl(fullroute)) ##get the full route, and handle the response with a user defined callback

    def quicky(self, full_route, callback=defaultcallback):
        return callback(sh.curl(full_route))

    def fullquery(self, database, dataset, data_format='j', limit=None, rows=None, start_date=None, end_date=None, order='asc', column_index=None, collapse=None, transform=None, send=False):
        database = database.upper() + '/'
        dataset = dataset.upper() + typetable[data_format] + '?'
        # validate start and end date arguments and append '&'
        if validate_date(start_date):
            start_date = 'start_date=' + start_date + '&'
        else: start_date = ''
        if validate_date(end_date):
            end_date = 'end_date=' + end_date + '&'
        else: end_date = ''
        # hacky solution to Error('Cannot concatenate str and NoneType objects')
        # just set default args to ''
        # what was u thinkin, musta bn hi or some shit
        column_index = 'column_index=' + str(column_index) + '&' if column_index else ''
        limit = 'limit=' + str(limit) + '&' if limit else ''
        rows = 'rows=' + str(rows) + '&' if rows else ''
        column_index = 'column_index=' + str(column_index) + '&' if column_index else ''
        collapse = 'collapse=' + collapse + '&' if collapse else ''
        transform = 'transformation=' + transform + '&' if transform else ''
        order = 'order=' + order + '&'
        api_key = 'api_key=' + self.APIKEY + '&'
        qstring = self.BASEURL + 'datasets/' + database + dataset + api_key + limit + rows + start_date + end_date + order + column_index + collapse + transform
        if send:
            return sh.curl(qstring)
        else:
            return qstring

    def justdata():
        return None
