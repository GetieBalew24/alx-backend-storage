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


def replay(fnction: Callable) -> None:
    """ a replay function to display the history of calls 
    of a particular function..
    """
    if fnction is None or not hasattr(fnction, '__self__'):
        return
    r_store = getattr(fnction.__self__, '_redis', None)
    if not isinstance(r_store, redis.Redis):
        return
    func_name = fnction.__qualname__
    input_key = '{}:inputs'.format(func_name)
    output_key = '{}:outputs'.format(func_name)
    func_call_count = 0
    if r_store.exists(func_name) != 0:
        func_call_count = int(r_store.get(func_name))
    print('{} was called {} times:'.format(func_name, func_call_count))
    func_inputs = r_store.lrange(input_key, 0, -1)
    func_outputs = r_store.lrange(output_key, 0, -1)
    for func_input, func_output in zip(func_inputs, func_outputs):
        print('{}(*{}) -> {}'.format(
            func_name,
            func_input.decode("utf-8"),
            func_output,
        ))
def decode_utf8(a: bytes) -> str:
    """ Decoder to store the histroy of Input & output"""
    return a.decode('utf-8') if type(a) == bytes else a
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