#!/usr/bin/env python3
""" module 10-update_topics """
import pymongo
from pymongo.collection import Collection
from typing import List


def update_topics(mongo_collection: Collection, name: str, topics: List[str]):
    """ changes all topics of a school document based on the name """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
