from pymongo import MongoClient

host = 'localhost'
port = 27017
name = 'test'

db = MongoClient(host,port)[name]