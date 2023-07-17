#!/usr/bin/env python3
"""
module 8-all
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection"""
    if not mongo_collection:
        return []
    with MongoClient() as client:
        db = client[mongo_collection]
        return db.find()
