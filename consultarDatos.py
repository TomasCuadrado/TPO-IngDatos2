from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]

for nombre in db.list_collection_names():
    print(f"\nColección: {nombre}")
    for doc in db[nombre].find():
        print(doc)
