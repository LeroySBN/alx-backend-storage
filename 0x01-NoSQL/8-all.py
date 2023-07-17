#!/usr/bin/env python3
"""
module 8-all
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection"""
    if mongo_collection is None:
        return []
    with MongoClient() as client:
        db = client.get_database()
        collection = db.mongo_collection
        return collection.find()
