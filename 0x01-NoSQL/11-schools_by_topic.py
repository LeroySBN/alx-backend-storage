#!/usr/bin/env python3
"""
module 11-schools_by_topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic: str):
    """
    returns the list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
