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
    Method count_calls
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Method wrapper
        """
        result = method(self, *args, **kwargs)
        self._redis.incr(method.__qualname__)
        return result
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Method call_history
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Method wrapper
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
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method store
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """
        getter function for key
        """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    @count_calls
    def get_str(self, key: str) -> str:
        """
        Method get_str
        """
        return self.get(key, str)

    @count_calls
    def get_int(self, key: str) -> int:
        """
        Method get_int
        """
        return self.get(key, int)


def replay(method: Callable):
    """
    Method replay
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
