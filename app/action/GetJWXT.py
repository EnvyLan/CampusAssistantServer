#coding=utf-8
from app.util import MongodbConnection

__author__ = 'EnvyLan'
import requests
from lxml import etree

class myJwxtInfo():

	def __init__(self, stuNum, stuPwd):
		self.stuNum = stuNum
		self.stuPwd = stuPwd
		#把一些URL文件预先写到文件里去，以后修改维护方便
		self.jwxt_xml = etree.ElementTree(file='D:/XML/a.xml')
		self.index_URL = str(self.jwxt_xml.xpath("/jwxt/index/text()"))[2:-2]
		self.CheckCode_URL = str(self.jwxt_xml.xpath("/jwxt/CheckCode/text()"))[2:-2]
		self.Curriculum_URL = str(self.jwxt_xml.xpath("/jwxt/curriculum/part1/text()"))[2:-2]
		self.myDb = MongodbConnection.myConnection('127.0.0.1',27017)
		self.myCollection = self.myDb['foo']
		self.header = {
            "Content-Type":"application/x-www-form-urlencoded",
            'Accept-Language':'zh-CN,zh;q=0.8',
			'Host':	'124.160.104.166',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
            'Referer':'http://124.160.104.166/(51ns3k55jcelkk45oepyswnw)',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Connection':'keep-alive',
        }

	# 登录
	def jwxt_Login(self, yzm=""):
		#r = requests.get(self.index_URL)
		#krint(r.text)
		#dom = etree.HTML(r.text)
		#u'获取网页的登陆值，类似token的一个值
		#jwxt_VIEWSTATE = dom.xpath('//input[@name="__VIEWSTATE"]/@value')[0]
		#把验证码图片写进本地文件，手动输入验证码，只是权宜之计
		# try:
		# 	CheckCode_file = open("D:/Downloads/1.gif", 'w+b')
		# 	CheckCode_file.write(requests.get(self.CheckCode_URL, stream = True).content)
		# except IOError:
		# 	print("IOError\n")
		# finally:
		# 	CheckCode_file.close()
		# yzm = raw_input("yzm= ")
		login_postData = {
            '__VIEWSTATE': 'dDwyODE2NTM0OTg7Oz7r5LOCfUV7vFG62JP9rMYu0xxl0A==',
            'txtUserName': 31207311,
            'TextBox2': 'hello123',
            'txtSecretCode': 'f1uw',
            'RadioButtonList1': '%D1%A7%C9%FA',
            'hidPdrs': '',
            'lbLanguage': '',
            'Button1': '',
            'hidsc': ''
            }
		index_read = requests.post(self.index_URL,data=login_postData)
		#print(index_read.text)
		#把登录之后的html页面的text传给下一个方法。

		return (etree.HTML(index_read.text))

	def returnXnd(self):
		temp = ''
		for h in  self.xnqlist:
			temp = temp +','+h
		return temp

	# 获取课表

	def before_getCurriculum(self, urlReader, token=''):
		#此处传过来的网页未登录进去之后的主页
		print("执行获取课表之前的动作")
		try:
			#首页上的网页是有“欢迎您：xxx”的，如果没有xxx，说明没有登录成功
			self.name = urlReader.xpath('//span[@id="xhxm"]/text()')[0][0:-2]
		except BaseException:
			return False
		self.getGrade()
		self.myCollection.update({'stuId':self.stuNum}, {'$set':{'stuId':self.stuNum, 'stuPwd':self.stuPwd, 'token':token, 'stuName':self.name}}, upsert= True)
		self.Curriculum_URL = self.Curriculum_URL+'?xh='+self.stuNum+'&xm='+self.name+'&gnmkdm=N121603'
		print(self.Curriculum_URL)
		curriculum_read = requests.get(self.Curriculum_URL, headers=self.header)
		print(curriculum_read.text)
		findxnd = etree.HTML(curriculum_read.text)
		self.xnqlist = findxnd.xpath('//table[@id="Table2"]//select[@name="xnd"]//option/text()')
		print("执行获取 学年的数据")
		for h in self.xnqlist:
			findxnd = self.getCurriculum(self.getCurriculum(findxnd, h, '1'), h, '2')

		return True

	def getCurriculum(self, index_read_text, xnd, xqd):
		print("执行获取课表的动作")
		postData = {
			'__EVENTTARGET': 'xnd',
			'__EVENTARGUMENT': '',
			'__VIEWSTATE' : index_read_text.xpath('//input[@name="__VIEWSTATE"]/@value')[0],
			'xnd' : xnd,
			'xqd' : xqd
		}
		secondRequest = requests.post(self.Curriculum_URL, data=postData, headers=self.header)
		#print(secondRequest.text)
		#这里的xpath表达式中 /text()  莫名其妙的就取到了所有该节点下的全部内容，
		#包括<br>标签分割的内容,经测试发现，text()函数跟在/后面可行，如果不跟，
		#则用item去取，例如 h.text 是不能取得全部内容的，原因不明，继续查官方文档
		#2015-12-12：text()只能取到上一级标签下的全部内容， br可以忽略掉取，但再加一层标签，无法取到内部。
		h_list = etree.HTML(secondRequest.text).xpath("//table[@id='Table1']//tr[position()>2]//td[@align]/text()")
		i = 0
		print('xnd = '+xnd+'   xqd = '+xqd)
		xnxqd = xnd+','+xqd

		import sys
		reload(sys)
		sys.setdefaultencoding( "utf-8" )
		l = []
		for h in range(len(h_list)):
			if h_list[h].decode('utf-8')[0:3] in [u'周一第', u'周二第', u'周三第', u'周四第', u'周五第', u'周六第',u'周日第']:
				l.append(h_list[h-1])
				l.append(h_list[h])
				l.append(h_list[h+1])
				l.append(h_list[h+2])
				h = h+3
				#print(str(i)+" : "+h)
		s = '!'.join(l)
		self.myCollection.update({'stuId':self.stuNum}, {"$set":{xnxqd:s}}, upsert=True)
		return etree.HTML(secondRequest.text)

	def getGrade(self):
		url = self.index_URL[:-13]+'xscj_gc.aspx?xh='+self.stuNum+'&xm='+self.name+'&gnmkdm=N121605'
		__VIEWSTATE = etree.HTML(requests.get(url, headers=self.header).text).xpath('//input[@name="__VIEWSTATE"]/@value')[0]
		postData = {
			'ddlXN': '',
			'ddlXQ': '',
			'__VIEWSTATE' : __VIEWSTATE,
			'Button6' : u'查询已修课程最高成绩'
		}
		temp = requests.post(url, data=postData, headers=self.header)
		mlist = etree.HTML(temp.text).xpath("//table[@id='Datagrid3']//tr[position()>1]//td[position()<8]/text()")
		tempCollection = self.myDb['stu_grade']
		print(len(mlist)/7)
		t = 0
		for i in range(len(mlist)):
			tempCollection.update({'classId':mlist[t+2]}, {'$set':{'stuId':self.stuNum,
															  'xn':mlist[t],
		                                                      'xq':mlist[t+1],
		                                                      'classId':mlist[t+2],
		                                                      'className':mlist[t+3],
		                                                      'credit':mlist[t+4],
		                                                      'type':mlist[t+5],
		                                                      'grade':mlist[t+6]
		                                                      }},
		                      upsert=True)
			t = t+7
			if t == len(mlist):
				break



getClass = myJwxtInfo('31207311', 'hello123')
getClass.before_getCurriculum(getClass.jwxt_Login('g3mq'), 'token')



