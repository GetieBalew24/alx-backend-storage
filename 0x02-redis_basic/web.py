#!/usr/bin/env python3
""" a get_page function (prototype: 
def get_page(url: str) -> str:).
The core of the function is very simple. 
It uses the requests module to obtain the HTML 
content of a particular URL and returns it.
"""
import redis
import requests
from functools import wraps
from typing import Callable


r_store = redis.Redis()
""" Redis instance."""


def count_url_access(method: Callable) -> Callable:
    """ output of fetched data."""
    @wraps(method)
    def caller(url) -> str:
        """ The caller function for fetched output."""
        r_store.incr(f'count:{url}')
        call_result = r_store.get(f'result:{url}')
        if call_result:
            return call_result.decode('utf-8')
        call_result = method(url)
        r_store.set(f'count:{url}', 0)
        r_store.setex(f'result:{url}', 10, call_result)
        return call_result
    return caller


@count_url_access
def get_page(url: str) -> str:
    """ Returns the content of a URL.
    and tracking the request.
    """
    return requests.get(url).text

