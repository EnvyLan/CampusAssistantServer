#coding=utf-8
__author__ = 'EnvyLan'
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, g, request
from flask import jsonify
from . import  api
from app.models.User import User
from app.action.get_jwxt import myJwxtInfo
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

#
@api.route('/verify_user', methods=['post'])
@auth.verify_password
def verify_pwd():
	postData = request.get_json(force=True)
	if postData['token'] == "":
		g.user = User(postData['stuId'],postData['Pwd'])
		#哈哈哈
		#getClass = myJwxtInfo(g.user.get_stuid(), g.user.get_pwd())
		if True:

			return jsonify({'statue':'100','token': g.user.generate_user_token()})
		else:
			return jsonify({'statue':'101','message':'error'})

	else:
		pass

def verify_token():
	postData = request.get_json(force=True)


@api.route('/token')
def generate_token():
	user = User(31207311,'')
	return  jsonify({'token':user.generate_user_token()})