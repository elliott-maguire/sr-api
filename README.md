srapi
=====

This library functions as a robust and comprehensive client for the SmartRecrtuiters API.

All official releases (*not* pre-releases) will feature functionality for all endpoints at the time of release.

How does it work?
-----------------

It's functionality is versatile in that the we can use an abstract method of calling a given endpoint, or we can use the hardcoded method.

**To call an endpoint using the abstract `call` method,** we must supply an endpoint, and may also supply request keyword arguments (in the same format as they'd be passed to a `requests.get` method).

    >>> import srapi
    >>> candidates = srapi.call('/candidates', 
            params={'q': 'developer', 'limit': 10})

**To call an endpoint using its hardcoded method,** all we need to supply is keyword arguments according to the endpoint. Check the full documentation to learn more about how 

    >>> import srapi
    >>> api = srapi.Endpoints(<YOUR SMARTTOKEN>)
    >>> candidates = api.get_candidates(q='developer')

In both cases, `candidates` would be a dict object housing the response data.

Contact
-------

Send me an email: `emag.codes@gmail.com`

Collaboration
-------------

All collaboration on this project will be done by SmartRecruiters employees. All are free to submit issues and enhancement proposals, but you must be a verified employee in order to make changes to the source.

