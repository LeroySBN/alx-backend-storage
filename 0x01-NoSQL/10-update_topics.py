#!/usr/bin/env python3
"""
module for update topics
"""
import pymongo


def update_topics(mongo_collection, name: str, topics: <list>):
    """
    changes all topics of a school document based on the name
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
        )

