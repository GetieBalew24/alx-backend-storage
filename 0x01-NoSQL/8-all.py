#!/usr/bin/env python3
""" a script that deletes all documents with name="Holberton school 
The database name passed as option of mongo command.
"""


def list_all(mongo_collection):
    """ Lists all documents in a school collection."""
    return [doc for doc in mongo_collection.find()]