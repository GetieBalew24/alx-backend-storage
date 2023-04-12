#!/usr/bin/env python3
""" Create a Cache class. In the __init__ method, store an instance of the Redis
client as a private variable named _redis (using redis.Redis()) and 
flush the instance using flushdb."""

import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union
class Cache:
    """ An object for storing data in a Redis data storage."""
    def __init__(self) -> None:
        """ Initializes a Cache instance variable."""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores a value in a Redis data storage and returns the key."""
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key