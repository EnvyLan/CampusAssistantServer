__author__ = 'EnvyLan'

from pymongo import MongoClient

def myConnection(host, port):
		try:
			myClient = MongoClient(host, port)

			return myClient
		except BaseException, e:
			print( "unable to connect MongoDb, I don't know why" )

myConnection("127.0.0.1", 27017)
