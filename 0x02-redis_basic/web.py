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
    def caller(url):
        content_key = "cached:" + url
        content_data = store.get(content_key)
        if content_data:
            return content_data.decode("utf-8")
        count_key = "count:" + url
        html = method(url)
        store.incr(count_key)
        store.set(content_key, html)
        store.expire(content_key, 10)
        return html
    return caller


@count_url_access
def get_page(url: str) -> str:
    """ Accesses HTML content of a url """
    result = requests.get(url)
    return result.text