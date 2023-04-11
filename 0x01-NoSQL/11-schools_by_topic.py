#!/usr/bin/env python3
"""  Python function that returns the list of school having a specific topic. 
Prototype: def schools_by_topic(mongo_collection, topic).
mongo_collection will be the pymongo collection object.
topic (string) topic searched.
"""


def schools_by_topic(mongo_collection, topic):
    """ list of school having a specific topic."""
    collection = mongo_collection.find({"topics": topic})
    return list(collection)
