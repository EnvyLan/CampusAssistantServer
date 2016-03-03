#coding=utf-8
__author__ = 'EnvyLan'

from pymongo import MongoClient

def myConnection(host='127.0.0.1', port=27017):
		try:
			myClient = MongoClient(host, port)
			db = myClient['test']
			return db
		except BaseException, e:
			print( "unable to connect MongoDb, I don't know why" )

