__author__ = 'EnvyLan'


from pymongo import MongoClient
client = MongoClient()
db = client.test
collection = db.foo
print( collection.find().count() )

