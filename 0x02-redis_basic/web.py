#!/usr/bin/env python3
""" a get_page function (prototype: 
def get_page(url: str) -> str:).
The core of the function is very simple. 
It uses the requests module to obtain the HTML 
content of a particular URL and returns it.
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """ counting how many times a Url is accessed """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    return res.text