""" Initialize SmartRecruiters API client. """

import os
import json

from sr_api.exceptions import *

import ergal
import requests


class SmartAPI:
    def __init__(self, token):
        """ Load all API classes, sets up instance.
        
        Arguments:
            str:token -- a certified SmartToken

        """

        self.token = token
        self.instance = self._get_instance()
    
    def _get_instance(self):
        """ Get platform instance. """

        url = 'https://api.smartrecruiters.com/configuration/company'
        headers = {'X-SmartToken': self.token}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return json.loads(response.text)
        elif response.status_code in [401, 403]:
            raise AuthError()
        elif response.status_code == 400:
            raise ProgrammingError()
        elif response.status_code == 429:
            raise ThrottleError()
        else:
            raise APIError()

    def _setup_database(self):
        """ Set up local ERGAL database. """

        

        