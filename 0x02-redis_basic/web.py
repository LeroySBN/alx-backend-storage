#!/usr/bin/env python3
"""
module web
"""
import requests
import redis
from typing import Callable
import time

cache = redis.Redis()


def cached_and_tracked(url: str) -> Callable:
    """
    Decorator that caches the result of a function with an expiration time of 10 seconds
    and tracks the access count.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> str:
            # Check if the content is cached
            cached_content = cache.get(url)
            if cached_content:
                # Increment the count for the URL
                cache.incr(f"count:{url}")
                return cached_content.decode('utf-8')

            # Call the original function
            response = func(*args, **kwargs)

            # Cache the content with an expiration time of 10 seconds
            cache.setex(url, 10, response)

            # Increment the count for the URL
            cache.incr(f"count:{url}")

            return response
        return wrapper
    return decorator


@cached_and_tracked
def get_page(url: str) -> str:
    """
    Method that takes in a URL and returns the HTML content of the URL
    """
    res = requests.get(url)
    return res.text
