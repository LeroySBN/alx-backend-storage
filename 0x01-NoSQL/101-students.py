#!/usr/bin/env python3
"""
module for students
"""
from pymongo import ASCENDING
from pymongo import MongoClient
from pprint import pprint

def top_students(mongo_collection):
    """
    returns all students sorted by average score
    """
