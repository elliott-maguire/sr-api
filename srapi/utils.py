"""
srapi.utils
~~~~~~~~~~~

This module implements all utility methods.
"""

import json
import requests


BASE = "https://api.smartrecruiters.com"


def call(endpoint, method="GET", **kwargs):
    """ Call a given endpoint.

    :param endpoint: a string indicating the target endpoint
    :param method: a string indicating the HTTP method to use
    """
    url = "".join([BASE, endpoint])
    method = method.lower()

    for key in kwargs:
        if key not in ("headers", "data", "params"):
            kwargs.pop(key)
    else:
        response = getattr(requests, method)(url, **kwargs)

    if response.status_code == 200:
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            return response.text
    else:
        raise Exception("Error: {}".format(response.status_code))
