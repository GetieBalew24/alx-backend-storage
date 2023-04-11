#!/usr/bin/env python3
"""  Python script that provides some stats about Nginx logs stored in MongoDB.
Database: logs.
Collection: nginx.
"""
from pymongo import MongoClient

if __name__ == "__main__":
    """ display the stats of Nginx logs stored in MongoDB 
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"] 
    """
    client_user = MongoClient('mongodb://127.0.0.1:27017')
    nginx_document_collection= client_user.logs.nginx

    number_of_logs = nginx_document_collection.count_documents({})
    print(f'{number_of_logs} logs')


    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for key in methods:
        number_of_method = nginx_document_collection.count_documents({
            "method": key
            })
        print(f'\tmethod {key}: {number_of_method}')


    count_status_check_doc = nginx_document_collection.count_documents(
        {
            "method": "GET", "path": "/status"
            }
    )


    print(f'{count_status_check_doc} status check')