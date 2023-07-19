#!/usr/bin/env python3
"""
module exercise
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Method that defines a decorator and returns the decorated function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Method that increments the count for that key every time the method
        """
        result = method(self, *args, **kwargs)
        self._redis.incr(method.__qualname__)
        return result
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Method that defines a decorator to store the history of inputs and outputs
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Stores the history of inputs and outputs for a particular function
        """
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(method.__qualname__ + ":outputs", str(result))
        return result
    return wrapper


class Cache:
    """
    Class Cache
    """
    def __init__(self):
        """
        Constructor for the class Cache that takes no arguments
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key and stores the input data in Redis using the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """
        Get method for redis database
        Args:
            key (str): string argument
            fn: Callable argument. Defaults to None.
        Returns:
            Union[str, bytes, int, float]: key converted to the desired format
        """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    @count_calls
    def get_str(self, key: str) -> str:
        """
        Method get_str parametrizes get with correct conversion(str)
        """
        return self.get(key, str)

    @count_calls
    def get_int(self, key: str) -> int:
        """
        Method get_str parametrizes get with correct conversion(int)
        """
        return self.get(key, int)


def replay(method: Callable):
    """
    Displays the history of calls of a particular function
    """
    r = redis.Redis()
    method_name = method.__qualname__
    count = r.get(method_name).decode('utf-8')
    inputs = r.lrange(method_name + ":inputs", 0, -1)
    outputs = r.lrange(method_name + ":outputs", 0, -1)
    print("{} was called {} times:".format(method_name, count))
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method_name, i.decode('utf-8'),
                                     o.decode('utf-8')))
