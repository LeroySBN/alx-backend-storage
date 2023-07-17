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

client = MongoClient('mongodb://localhost:27017')
collection = client.my_db.my_collection
top_students_list = top_students(collection)

for student in top_students_list:
    pprint(student["_id"], student["name"], student["scores"])

for student in top_students_list:
    pprint(student["_id"], student["name"], "=>", student["averageScore"])
