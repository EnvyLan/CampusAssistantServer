__author__ = 'EnvyLan'

from pymongo import MongoClient

def myConnection(host, port):
		try:
			myClient = MongoClient(host, port)
			return myClient
		except BaseException, e:
			print( "unable to connect MongoDb, I don't know why" )


