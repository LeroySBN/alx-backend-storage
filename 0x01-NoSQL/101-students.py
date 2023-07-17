#!/usr/bin/env python3
"""
module for students
"""
from pymongo import ASCENDING

def top_students(mongo_collection):
    """
    returns all students sorted by average score
    """
    pipeline = [
        {"$unwind": "$scores"},
        {"$group": {"_id": "$_id", "averageScore": {"$avg": "$scores.score"}}},
        {"$sort": {"averageScore": ASCENDING}}
    ]
    result = mongo_collection.aggregate(pipeline)
    return list(result)
