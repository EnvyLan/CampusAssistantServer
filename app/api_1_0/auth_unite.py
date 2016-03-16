#coding=utf-8
__author__ = 'EnvyLan'
from flask import request
from flask import jsonify

from app.api_1_0 import  api
from app.action.GetUniteAccount import GetUniteAccount


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


