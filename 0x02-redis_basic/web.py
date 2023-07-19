#!/usr/bin/env python3
"""
module web
"""
import redis

redis = redis.Redis()


def get_page(url: str) -> str:
    """
    Method that takes in a URL and returns the HTML content of the URL
    """
    import requests
    res = requests.get(url)
    key = f"count:{url}"
    if redis.get(key):
        redis.incr(key)
    else:
        redis.set(key, 1)
    return res.text
