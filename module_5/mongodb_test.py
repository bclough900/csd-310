import pymongo

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.kirb2v7.mongodb.net/?retryWrites=true&w=majority")

db = client["pytech"]

print(db.list_collection_names)

