""" Main API module. """

import json
import requests

BASE = 'https://api.smartrecruiters.com'

    
def call(endpoint, method, **kwargs):
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
    url = ''.join([BASE, endpoint])
    method = method.lower()
    
    for key in kwargs:
        if key not in ('headers', 'data', 'params'):
            kwargs.pop(key)
    else:
        response = getattr(requests, method)(url, **kwargs)

    if response.status_code == 200:
        return json.loads(response)
    elif response.status_code in (203, 204):
        return response.text
    else:
        raise Exception('Error: {}'.format(response.status_code))


class CandidateAPI:
    def __init__(self, token):
        """ Hardcoded Candidate API endpoint access.

        These API classes make it easier to call endpoints by hardcoding
        request info like the actual endpoint path, and making
        the passage of arguments much more intuitive.

        All operations on this interface should be executed in
        accordance with the official SmartRecruiters API documentation.
        
        Arguments:
            token -- a SmartRecruiters API token

        """
        self.headers = {'X-SmartToken': token}
    
    def search_candidates(self, **kwargs):
        """ Search for candidates. (GET /candidates) """
        endpoint = '/candidates'
        method = 'get'

        response = call(
            endpoint, method, headers=self.headers, params=kwargs)
        return response
    
    def create_candidate(self, **kwargs):
        """ Create a candidate. (POST /candidates) """
        endpoint = '/candidates'
        method = 'post'
        data = json.dumps(**kwargs)

        response = call(
            endpoint, method, headers=self.headers, data=data)
        return response

    def get_candidate(self, cid):
        """ Get a candidate's details. (GET /candidates/{cid}) """
        endpoint = '/candidates/{cid}'.format(cid=cid)
        method = 'get'

        response = call(
            endpoint, method, headers=self.headers)
        return response
    
    def delete_candidate(self, cid):
        """ Delete a candidate. (DELETE /candidates/{cid}) """
        endpoint = '/candidates/{cid}'.format(cid=cid)
        method = 'delete'

        response = call(endpoint, method)
        return response
        
    