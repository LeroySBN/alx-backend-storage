#!/usr/bin/env python3
"""
module web
"""
from functools import wraps
from typing import Callable
import redis
import requests
import time

cache = redis.Redis()


def cache_and_track(method: Callable) -> Callable:
    """
    Method that takes in a function and returns a function
    """
    

    @wraps(method)
    def wrapper(url):
        """
        Wrapper function
        """
        if cache.get(f"count:{url}"):
            cache.incr(f"count:{url}")
        else:
            cache.set(f"count:{url}", 1)
        return method(url)
    return wrapper


@cache_and_track
def get_page(url: str) -> str:
    """
    Method that takes in a URL and returns the HTML content of the URL
    """
    res = requests.get(url)
    return res.text
