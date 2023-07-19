#!/usr/bin/env python3
"""
Main file
"""
import redis

get_page = __import__('web').get_page

cache = redis.Redis()
cache.flushdb()

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
    '',
]

for url in urls:
    get_page(url)

print(f"{'http://slowwly.robertomurray.co.uk/time.php'}: {cache.get('count:http://slowwly.robertomurray.co.uk/time.php')} >> expected: 1")
print(f"{'https://twitter.com/'}: {cache.get('count:https://twitter.com/')} >> expected: 3")
print(f"{'https://www.google.com/'}: {cache.get('count:https://www.google.com/')} >> expected: 2")
print(f"{'https://www.reddit.com/'}: {cache.get('count:https://www.reddit.com/')} >> expected: 1")
print(f"{'https://www.youtube.com/'}: {cache.get('count:https://www.youtube.com/')} >> expected: 1")
print(f"{'https://www.stackoverflow.com/'}: {cache.get('count:https://www.stackoverflow.com/')} >> expected: 3")
print(f"{'not a called url'}: {cache.get('count:https://www.threads.com/')} >> expected: 0")
