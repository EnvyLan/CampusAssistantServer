#coding=utf-8
__author__ = 'EnvyLan'
from flask import request
from flask import jsonify

from app.api_1_0 import  api
from app.action.GetUniteAccount import GetUniteAccount
from app.util.MongodbConnection import myConnection

#参数有两个，学号stuId和密码Pwd，
@api.route("/virfy_unite_user", methods=['post'])
def virify_unite_user():
	postData = request.get_json(force=True)
	print(postData)
	unite = GetUniteAccount(postData['stuId'], postData['Pwd'])
	url = unite.getURL()
	if url == False:
		return jsonify({'status':201,'message':'账号密码错误'})
	else:
		return jsonify({'status':200, 'recordURL':url, 'token':unite.getToken()})


def getRecordURL():
	postData = request.get_json(force=True)
	if verify_token(postData['stuId'], postData['token']):
		client_db = myConnection()
		collection = client_db['UniteAccount']
		result = collection.find_one({'stuId':postData['stuId']}, {'Pwd':1})
		recordURL = GetUniteAccount(postData['stuId'], result['Pwd']).getRecord()
		return jsonify({'status':200, 'recordURL':recordURL})
	else:
		return jsonify({'status':201,'message':'error'})


def verify_token(stuId, token):
	client_db = myConnection()
	collection = client_db['UniteAccount']
	result = collection.find_one({'stuId':str(stuId)}, {'token':1})
	if result == None:
		return False
	return token==result['token']