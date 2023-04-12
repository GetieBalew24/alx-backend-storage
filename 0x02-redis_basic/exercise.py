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
def call_history(method: Callable) -> Callable:
    """ Call history decorator to store the history of inputs 
    and outputs for a particular function. 
    """
    call_key = method.__qualname__
    i= "".join([call_key, ":inputs"])
    o = "".join([call_key, ":outputs"])
    @wraps(method)
    def caller(self, *args, **kwargs):
        """ caller history"""
        self._redis.rpush(i, str(args))
        result_call = method(self, *args, **kwargs)
        self._redis.rpush(o, str(result_call))
        return result_call
    return caller
def decode_utf8(a: bytes) -> str:
    """ Decoder to store the histroy of Input & output"""
    return a.decode('utf-8') if type(a) == bytes else a
def replay(method: Callable):
    """ a replay function to display the history 
    of calls of a particular function. 
    """
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])
    call_count = method.__self__.get(key)
    i_list = method.__self__._redis.lrange(i, 0, -1)
    o_list = method.__self__._redis.lrange(o, 0, -1)
    queue = list(zip(i_list, o_list))
    print(f"{key} was called {decode_utf8(count)} times:")
    for k, v, in queue:
        k = decode_utf8(k)
        v = decode_utf8(v)
        print(f"{key}(*{k}) -> {v}")
class Cache:
    """ An object for storing data 
    in a Redis data storage.
    """
    def __init__(self) -> None:
        """ Initializes a Cache instance variable."""
        self._redis = redis.Redis()
        self._redis.flushdb(True)
    @count_calls
    @call_history
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