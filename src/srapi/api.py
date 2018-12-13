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
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            return response.text
    else:
        raise Exception('Error: {}'.format(response.status_code))


class CandidateAPI:
    """ Partial hardcoded Candidate API endpoint access. """
    def __init__(self, token):
        """ Initialize the Candidate API.
        
        Arguments:
            token -- a SmartRecruiters API token

        """
        self.headers = {'X-SmartToken': token}
    
    def search(self, **kwargs):
        """ Search for candidates. 
        
        GET /candidates
        
        """
        endpoint = '/candidates'
        method = 'get'

        response = call(
            endpoint, method, headers=self.headers, params=kwargs)
        return response
    
    def create(self, **kwargs):
        """ Create a candidate. 
        
        POST /candidates 
        
        """
        endpoint = '/candidates'
        method = 'post'
        data = json.dumps(**kwargs)

        response = call(
            endpoint, method, headers=self.headers, data=data)
        return response

    def get(self, cid):
        """ Get a candidate's details. 
        
        GET /candidates/{cid}
        
        """
        endpoint = '/candidates/{}'.format(cid)
        method = 'get'

        response = call(
            endpoint, method, headers=self.headers)
        return response
    
    def delete(self, cid):
        """ Delete a candidate. 
        
        DELETE /candidates/{cid}
        
        """
        endpoint = '/candidates/{}'.format(cid)
        method = 'delete'

        response = call(
            endpoint, method, headers=self.headers)
        return response
    
    def update(self, cid):
        """ Update a candidate. 
        
        PATCH /candidates/{cid}
        
        """
        endpoint = '/candidates/{}'.format(cid)
        method = 'patch'

        response = call(
            endpoint, method, headers=self.headers)
        return response


class JobAPI:
    """ Partial hardcoded Candidate API endpoint access. """
    def __init__(self, token):
        """ Initialize the Job API.
        
        Arguments:
            token -- a SmartRecruiters API token
        
        """
        self.headers = {'X-SmartToken': token}

    def search(self, **kwargs):
        """ Search for jobs.
        
        GET /jobs
        
        """
        endpoint = '/jobs'
        method = 'get'

        response = call(
            endpoint, method, headers=self.headers)
        return response

    def create(self, **kwargs):
        """ Create a candidate. 
        
        POST /candidates 
        
        """
        endpoint = '/candidates'
        method = 'post'
        data = json.dumps(**kwargs)

        response = call(
            endpoint, method, headers=self.headers, data=data)
        return response