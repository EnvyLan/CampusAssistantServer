__author__ = 'EnvyLan'
from flask import current_app, request, url_for
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
class User():
	stuId =""
	stuPwd = ""
	stuName = ""
	token = ""
	def __init__(self, stuId, stuPwd):
		self.stuId = stuId
		self.stuPwd = stuPwd

	def get_stuid(self):
		return self.stuId

	def get_pwd(self):
		return self.stuPwd

	def generate_user_token(self):
		s = Serializer('SECRET_KEY')
		self.token =  s.dumps( {'token':self.stuId} ).decode('ascii')
		return self.token

