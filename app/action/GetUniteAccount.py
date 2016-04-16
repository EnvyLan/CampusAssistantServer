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
		self.uniteURL = 'http://ca.zucc.edu.cn/cas/login'
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
			record = mySession.send(requests.Request('get', self.recordURL, cookies=myCookies, headers=self.header).prepare()).history[0].headers['Location']
			print(record)
			#except BaseException :
			#return False
		return record[:-1]+'3'

	#2016-4-13：进行学校统一账号认证登录仍然有问题，第一次从网页上获取的cookies进行登录会重新跳到登录页面，貌似cookies值错误，目前无法解决这个问题
	def getBalance(self):
		mySession2 = requests.Session()
		url = 'http://ca.zucc.edu.cn/cas/login?service=http://student.zucc.edu.cn'
		login_data={
			'authType':'0',
			'username':self.stuId,
			'password':self.Pwd,
			'lt':'',
			'execution':'e2s1',
			'_eventId':'submit',
			'submit':'',
			'randomStr':''
		}
		header = {
			'Connection':'keep-alive',
			'Cache-Control':'max-age=0',
			'Origin':'http://ca.zucc.edu.cn',
			'Upgtade-Indecure-Requests':'1',
            "Content-Type":"application/x-www-form-urlencoded",
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
            'Referer':'http://ca.zucc.edu.cn/cas/login?service=http://student.zucc.edu.cn/index.portal',
            'Accept-Encoding':'gzip, deflate, sdch'
		}
		#value = mySession2.send(requests.Request('get', 'http://student.zucc.edu.cn').prepare()).history[0].cookies.get("JSESSIONID")
		#myCookies = requests.get('http://student.zucc.edu.cn').cookies
		#myCookies.set('JSESSIONID', value=value, domain='student.zucc.edu.cn', path='/')
		#c = h1.history[0].cookies
		#c2 = h1.history[1].cookies
		#ct = c.get('JSESSIONID')
		# from requests.cookies import RequestsCookieJar
		# myCookies = RequestsCookieJar()

		myCookies = mySession2.get(url).cookies
		print(myCookies)
		myCookies.set(name='CASPRIVACY', value='""', domain='ca.zucc.edu.cn', path='/cas/')
		myCookies.set(name='CASTGC', value='', domain='ca.zucc.edu.cn', path='/cas/')
		myCookies.set(name='JSESSIONID', value='OBXJqJHyyrB8FH07CFOx.41', domain='student.zucc.edu.cn', path='/cas')
		h=mySession2.post(url=url, headers=header, data=login_data, cookies=myCookies)
		print(h.text)
		# h2 = requests.get("http://student.zucc.edu.cn", headers=header)
		# s =h2.history[0].headers['Set-Cookie'].split(';')
		# print(h2.cookies)
		# print(s[0][11:])
		#h2 = mySession2.send(requests.Request('get', url='http://student.zucc.edu.cn',cookies=myCookies).prepare())
		h3 = mySession2.get(url='http://student.zucc.edu.cn/index.portal?.cs=cnxjb20uZWR1LmRrLnN0YXJnYXRlLnBvcnRhbC5zaXRlLmltcGwuRnJhZ21lbnRXaW5kb3d8Y3Npcy5teVN0dWRlbnRJbmZvcm1hdGlvbiFmMTE0N3x2aWV3fG5vcm1hbHxwbV9jc2lzLm15U3R1ZGVudEluZm9ybWF0aW9uIWYxMTQ3X2FjdGlvbj1zaG93fHJtX3xwcm1f', cookies=myCookies)
		return h3.json['balance']




