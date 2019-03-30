"""
srapi.jobs
~~~~~~~~~~

This module implements the Job API client.
"""

import json

from srapi.utils import call


class JobAPI:
    """ Partial hardcoded Job API endpoint access. """
    def __init__(self, token):
        """ Initialize the Job API.

        :param token: a SmartRecruiters API token
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