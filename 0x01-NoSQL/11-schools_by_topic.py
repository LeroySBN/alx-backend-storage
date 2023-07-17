#!/usr/bin/env python3
"""
module 11-schools_by_topic
"""
from pymongo.collection import Collection


def schools_by_topic(mongo_collection: Collection, topic: str) -> list:
    """
    returns the list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
