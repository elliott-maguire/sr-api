"""
srapi.candidate
~~~~~~~~~~~~~~~

This module implements the Candidate API client.
"""

import json

from srapi.utils import call


class CandidateAPI:
    """ Partial hardcoded Candidate API endpoint access. """

    def __init__(self, token):
        """ Initialize the Candidate API.

        :param token: a SmartRecruiters API token
        """
        self.headers = {"X-SmartToken": token}

    def search(self, **kwargs):
        """ Search for candidates. """
        endpoint = "/candidates"
        method = "get"

        response = call(endpoint, method, headers=self.headers, params=kwargs)

        return response

    def create(self, **kwargs):
        """ Create a candidate.

        POST /candidates
        """
        endpoint = "/candidates"
        method = "post"
        data = json.dumps(**kwargs)

        response = call(endpoint, method, headers=self.headers, data=data)

        return response

    def get(self, cid):
        """ Get a candidate's details.

        GET /candidates/{cid}
        """
        endpoint = f"/candidates/{cid}"
        method = "get"

        response = call(endpoint, method, headers=self.headers)

        return response

    def delete(self, cid):
        """ Delete a candidate.

        DELETE /candidates/{cid}
        """
        endpoint = f"/candidates/{cid}"
        method = "delete"

        response = call(endpoint, method, headers=self.headers)

        return response

    def update(self, cid):
        """ Update a candidate.

        PATCH /candidates/{cid}
        """
        endpoint = "/candidates/{}".format(cid)
        method = "patch"

        response = call(endpoint, method, headers=self.headers)

        return response
