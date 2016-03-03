#coding=utf-8
__author__ = 'EnvyLan'
from flask import  g, request
from flask import jsonify
from app.api_1_0 import  api
from app.models.User import User
from app.action.get_jwxt import myJwxtInfo
from app.util.MongodbConnection import myConnection
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

#
@api.route('/verify_user', methods=['post'])
@auth.verify_password
def verify_pwd():
	postData = request.get_json(force=True)
	print(postData)
	#这里说明第一次登陆，是没有token的
	# if postData['token'] == "":
	# 	g.user = User(postData['stuId'],postData['Pwd'])
	# 	#对账号密码进行验证
	# 	getClass = myJwxtInfo(g.user.get_stuid(), g.user.get_pwd())
	# 	token = g.user.generate_user_token();
	# 	if getClass.before_getCurriculum(getClass.jwxt_Login(), token):
	# 		return jsonify({'statue':'100','token': token, 'stuId':g.user.get_stuid(), 'xnd':getClass.returnXnd()})
	# 	else:
	# 		return jsonify({'statue':'101','message':'error'})
	# #有token，直接去Mongodb查找数据
	# else:
	# 	if verify_token(postData['stuId'], postData['token']):
	# 		pass
	# 	else:
	return jsonify({'statue':'101','message':'error'})

#验证token函数，以后把它改成修饰器函数，目前先调用用着
def verify_token(stuId, token):
	client_db = myConnection()
	collection = client_db['foo']
	result = collection.find_one({'stuId':str(stuId)}, {'token':1})
	return token==result['token']

#获取课表，post的内容有stuID，token, xnd, xqd
@api.route('/getCurriculum', methods=['post'])
def getCurriculum():
	postData = request.get_json(force=True)
	#验证token成功
	if verify_token(postData['stuId'], postData['token']):
		#从MongoDb获取课表
		print("token验证成功")
		temp = postData['xnd']+','+postData['xqd']
		myCurriculum = myConnection()['foo'].find_one({'stuId':str(postData['stuId'])}, {temp:1})
		if myCurriculum == None:
			return jsonify({'statue':'102','message':'没有找到您的课程，请重新选择学年和学期'})
		else:
			print(myCurriculum)
			return jsonify({'statue':'100', temp:myCurriculum[temp]})
	else:
		return jsonify({'statue':'101','message':'token验证不通过，请重新登录'})

@api.route('/token')
def generate_token():
	user = User(31207311,'')
	return  jsonify({'token':user.generate_user_token()})

