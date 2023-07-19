#!/usr/bin/env python3
"""
module exercise
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method store
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
