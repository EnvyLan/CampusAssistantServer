#coding=utf-8
__author__ = 'EnvyLan'
import requests
import json
from lxml import etree

class myJwxtInfo():

	def __init__(self, stuNum, stuPwd):
		self.stuNum = stuNum
		self.stuPwd = stuPwd
		#把一些URL文件预先写到文件里去，以后修改维护方便
		self.jwxt_xml = etree.ElementTree(file='D:/XML/a.xml')
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
		self.myTest()




	def jwxt_Login(self):
		r = requests.get(self.index_URL)
		#krint(r.text)
		dom = etree.HTML(r.text)
		#u'获取网页的登陆值，类似token的一个值
		jwxt_VIEWSTATE = dom.xpath('//input[@name="__VIEWSTATE"]/@value')[0]
		#把验证码图片写进本地文件，手动输入验证码，只是权宜之计
		try:
			CheckCode_file = open("D:/Downloads/1.gif", 'w+b')
			CheckCode_file.write(requests.get(self.CheckCode_URL, stream = True).content)
		except IOError:
			print("IOError\n")
		finally:
			CheckCode_file.close()
		yzm = raw_input("yzm= ")

		login_postData = {
            '__VIEWSTATE': jwxt_VIEWSTATE,
            'txtUserName': self.stuNum,
            'TextBox2': self.stuPwd,
            'txtSecretCode': yzm,
            'RadioButtonList1': '%D1%A7%C9%FA',
            'hidPdrs': '',
            'lbLanguage': '',
            'Button1': '',
            'hidsc': ''
            }

		index_read = requests.post(self.index_URL,data=login_postData)
		#print(index_read.text)
		#把登录之后的html页面的text传给下一个方法。
		self.getCurriculum(etree.HTML(index_read.text))

	def getCurriculum(self, index_read_text):
		postData = {
			'__EVENTTARGET': 'xqd',
			'__EVENTARGUMENT': '',
			'__VIEWSTATE' : index_read_text.xpath('//input[@name="__VIEWSTATE"]/@value')[0],
			'xnd' : '2013-2014',
			'xqd' : '2'
		}
		print(postData)
		self.name = index_read_text.xpath('//span[@id="xhxm"]/text()')[0][0:-2]
		#s = name.encode("gb2312")
		i = 0

		my_params = {'xh': self.stuNum, 'xm': self.name, 'gnmkdm': 'N121603'}
		curriculum_read = requests.get(self.Curriculum_URL, params=my_params, data= postData, headers=self.header)
		#print(curriculum_read.text)
		curriculum_read_text = etree.HTML(curriculum_read.text)

		#这里的xpath表达式中 /text()  莫名其妙的就取到了所有该节点下的全部内容，
		#包括<br>标签分割的内容,经测试发现，text()函数跟在/后面可行，如果不跟，
		#则用item去取，例如 h.text 是不能取得全部内容的，原因不明，继续查官方文档
		#2015-12-12：text()只能取到上一级标签下的全部内容， br可以忽略掉取，但再加一层标签，无法取到内部。
		h_list = curriculum_read_text.xpath("//table[@id='Table1']//tr[position()>3]//td[@align]/text()")

		for h in h_list:
			if h == u'\xa0':
				continue
			else:
				i+=1
				print(str(i)+" : "+h)
		#print(curriculum_read.text)
		#postData['xqd'] = 2
		#postData['__EVENTTARGET'] = 'xqd'
		#s = etree.HTML(curriculum_read.text).xpath('//input[@name="__VIEWSTATE"]/@value')[0]
		#postData['__VIEWSTATE']= s
		#print(postData)
		#curriculum_read2 = requests.post(self.Curriculum_URL, params=my_params, data=postData, headers=header)
		#print(curriculum_read2.text)




	def myTest(self):
		self.index_URL = str(self.jwxt_xml.xpath("/jwxt/index/text()"))[2:-2]
		self.CheckCode_URL = str(self.jwxt_xml.xpath("/jwxt/CheckCode/text()"))[2:-2]
		self.Curriculum_URL = str(self.jwxt_xml.xpath("/jwxt/curriculum/part1/text()"))[2:-2]





	def myTest2(self):
		self.myTest()

s = myJwxtInfo(31207311,'hello123')
s.jwxt_Login()
