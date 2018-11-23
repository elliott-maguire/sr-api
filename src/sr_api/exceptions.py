""" SmartRecruiters API exceptions. """


class APIError(Exception):
    """ Base exception raised for API errors. """
    pass


class AuthError(APIError):
    """ Exception raised on auth failure (401). """


class ProgrammingError(APIError):
    """ Exception raised on bad request (400). """
    pass


class ThrottleError(APIError):
    """ Exception raised on a throttle (429). """
    pass


class ContentError(APIError):
    """ Exception raised on any flawed content response.

    Attributes:
        response -- a Response object

    """
    def __init__(self, response):
        self.response = response
    
    @property
    def content(self):
        return str(self.response.text)

