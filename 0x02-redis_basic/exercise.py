#!/usr/bin/env python3
""" Create a Cache class. In the __init__ method, store an instance of the Redis
client as a private variable named _redis (using redis.Redis()) and 
flush the instance using flushdb."""

import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union
def count_calls(method: Callable) -> Callable:
    """ Count number of calls """
    call_key = method.__qualname__
    @wraps(method)
    def caller(self, *args, **kwargs):
        """ caller """
        self._redis.incr(call_key)
        return method(self, *args, **kwargs)
    return caller
class Cache:
    """ An object for storing data 
    in a Redis data storage.
    """
    def __init__(self) -> None:
        """ Initializes a Cache instance variable."""
        self._redis = redis.Redis()
        self._redis.flushdb(True)
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores a value in a Redis 
        data storage and returns the key.
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """ Retrieves a value from 
        a Redis data storage.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """ Retrieves a string value
        from a Redis data storage.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ Retrieves an integer value 
        from a Redis data storage
        """
        return self.get(key, lambda x: int(x))