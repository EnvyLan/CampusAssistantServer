#coding=utf-8
__author__ = 'EnvyLan'
import  requests
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.util import MongodbConnection

class GetUniteAccount():
	def __init__(self, stuId, Pwd):
		self.stuId = stuId
		self.Pwd = Pwd
		self.indexURL = 'http://mlib.zucc.edu.cn'
		self.loginURL = 'http://mc.zucc.edu.cn/irdUser/login/opac/opacLogin.jspx'
		self.recordURL = 'http://mc.zucc.edu.cn/cmpt/opac/opacLink.jspx?stype=1'
		self.token = ''
		self.myDb = MongodbConnection.myConnection('127.0.0.1',27017)
		self.myCollection = self.myDb['UniteAccount']
		self.login_data={
				'backurl':'%2Fuser%2Fuc%2FshowOpacinfo.jspx',
				'schoolid':'5613',
				'userType':0,
				'username':self.stuId,
				'password':self.Pwd
		}
		self.header = {
            "Content-Type":"application/x-www-form-urlencoded",
            'Accept-Language':'zh-CN,zh;q=0.8',
			'Host':	'mc.zucc.edu.cn',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
            'Referer':'http://mc.zucc.edu.cn/user/login/showLogin.jspx?backurl=%2Fuser%2Fuc%2FshowOpacinfo.jspx',
            'Accept-Encoding':'gzip, deflate, sdch'
		}

	def getToken(self):
		return self.token

	def getURL(self):
		self.recordURL = self.getRecord()
		print(self.recordURL)
		if(self.recordURL == False):
			pass
		else:
			self.generateToken()
			self.insertDB()
		return self.recordURL

	def generateToken(self):
		s =  Serializer('SECRET_KEY')
		self.token =s.dumps({'token':self.stuId}).decode('ascii')

	def insertDB(self):
		self.myCollection.update({'stuId':self.stuId}, {'$set':{'stuId':self.stuId, 'Pwd':self.Pwd, 'token':self.token, 'RecordURL':self.recordURL}}, upsert=True)

	def getRecord(self):
		i = 1
		while i==1:
			try:
				mySession = requests.Session()
				myCookies = mySession.send(requests.Request('get', self.indexURL).prepare()).cookies
				i = 2
			except BaseException :
				i = 1
			#try:
			myCookies = mySession.send(requests.Request('post', self.loginURL, cookies=myCookies, data=self.login_data, headers=self.header).prepare()).history[0].cookies
			print('myCookies=')
			print(myCookies)
			record = mySession.send(requests.Request('get', self.recordURL, cookies=myCookies, headers=self.header).prepare())#.history[0].headers['Location']
			print(record)
			#except BaseException :
			#return False
		return record[:-1]+'3'

