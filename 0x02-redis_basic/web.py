#!/usr/bin/env python3
"""
module web
"""
import requests
import redis
from typing import Callable
import time

cache = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """
    Method that takes in a function and returns a function
    """
    from functools import wraps

    @wraps(method)
    def wrapper(url):
        """
        Wrapper function
        """
        cache.expire(f"count:{url}", timedelta(seconds=10))
        if cache.get(f"count:{url}"):
            cache.incr(f"count:{url}")
        else:
            cache.set(f"count:{url}", 1)
        return method(url)
    return wrapper


@count_calls
def get_page(url: str) -> str:
    """
    Method that takes in a URL and returns the HTML content of the URL
    """
    res = requests.get(url)
    return res.text
