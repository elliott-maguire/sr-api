""" Main API module. """

import json
import requests

    
def call(self, endpoint, method, **kwargs):
    """ Call any given endpoint.

    Takes an endpoint and method as well as any parameters
    that should be passed to the given endpoint. Request is
    conducted, response is handled and returned in dict format.

    Arguments:
        endpoint -- a str indicating the target endpoint.
        method -- 
            a str indicating the HTTP method to use,
            defaualt is GET.
    
    """
    url = ''.join([self.base, endpoint])
    method = method.lower()
    
    for key in kwargs:
        if key not in ('headers', 'data', 'params'):
            kwargs.pop(key)
    else:
        response = getattr(requests, method)(url, **kwargs)

    if response.status_code == 200:
        return json.loads(response)
    else:
        raise Exception('Error: {}'.format(response.status_code))


class Endpoints:
    def __init__(self, token):
        """ Load all API classes, sets up instance.
        
        Arguments:
            token -- a SmartRecruiters API token

        """
        self.base = 'https://api.smartrecruiters.com'
        self.token = token
    
    