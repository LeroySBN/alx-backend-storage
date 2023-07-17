#!/usr/bin/env python3
"""
module 9-insert_school
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    """
    return mongo_collection.insert(kwargs)
