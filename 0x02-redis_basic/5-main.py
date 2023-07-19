#!/usr/bin/env python3
"""
Main file
"""
import redis

get_page = __import__('web').get_page

cache = redis.Redis()

urls = [
    'http://slowwly.robertomurray.co.uk/time.php',
    'https://www.stackoverflow.com/',
    'https://www.stackoverflow.com/',
    'https://www.google.com/',
    'https://twitter.com/',
    'https://www.youtube.com/',
    'https://www.instagram.com/',
    'https://www.amazon.com/',
    'https://www.google.com/',
    'https://twitter.com/',
    'https://www.reddit.com/',
    'https://twitter.com/',
    'https://www.stackoverflow.com/',
]

for url in urls:
    get_page(url)

for url in urls:
    count = cache.get(f"count:{url}")
    print(f"{url}: {count}")
