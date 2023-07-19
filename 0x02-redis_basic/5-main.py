#!/usr/bin/env python3
"""
Main file
"""
import redis

get_page = __import__('web').get_page

cache = redis.Redis()


get_page('http://slowwly.robertomurray.co.uk/time.php')
get_page('https://www.stackoverflow.com/')
get_page('https://www.stackoverflow.com/')
get_page('https://www.google.com/')
get_page('https://twitter.com/')
get_page('https://www.youtube.com/')
get_page('https://www.instagram.com/')
get_page('https://www.amazon.com/')
get_page('https://www.google.com/')
get_page('https://twitter.com/')
get_page('https://www.reddit.com/')
get_page('https://twitter.com/')
get_page('https://www.stackoverflow.com/')

print(cache.get('https://www.google.com/'))
print(cache.get('https://twitter.com/'))
print(cache.get('https://stackoverflow.com/'))