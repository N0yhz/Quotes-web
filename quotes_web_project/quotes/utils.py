from pymongo import MongoClient

def get_mongodb():
    client = MongoClient('mongodb+srv://n0yhz:module08@qouteset1.13lvt.mongodb.net/')

    db = client.hw10
    return db