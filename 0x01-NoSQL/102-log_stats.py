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
    """ adding the top 10 of the most present IPs in the collection nginx of the database logs """
    top_10_ip = nginx_document_collection.aggregate([
        {"$group":
            {
                "_id": "$ip", "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {"_id": 0, "ip": "$_id", "count": 1 }}
    ])

    print("IP Adderss:")
    for top_ten_ip in top_10_ip:
        ip = top_ten_ip.get("ip")
        count = top_ten_ip.get("count")
        print(f'\t{ip}: {count}')
