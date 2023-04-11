#!/usr/bin/env python3
""" A Python function that inserts a new document 
Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
"""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a school collection."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
