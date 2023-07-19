#!/usr/bin/env python3
"""
module web
"""
import redis

cache = redis.Redis()


def get_page(url: str) -> str:
    """
    Method that takes in a URL and returns the HTML content of the URL
    """
    import requests
    res = requests.get(url)
    key = f"count:{url}"
    if cache.get(key):
        cache.incr(key)
    else:
        cache.set(key, 1)
    return res.text
