#coding=utf-8
__author__ = 'EnvyLan'
import requests
myList = u'周五第1,2节{第1-17周|单周}'
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
s = ''
for index, i in enumerate(myList):
	if i == '{':
		s = myList[0:index]
		print(s)
print(s[1:2])
t = s[3:-1]
print(t)
list = t.split(',')
timeFrom = int(list[0])
timeLen = int(list[1])-int(list[0])
print(timeFrom)
print(timeLen)
#l = requests.post("http://mc.zucc.edu.cn/irdUser/login/opac/opacLogin.jspx", data=login_data, cookies = _cookie, headers=header)
#print(l.text)
#t = s.get("http://mlib.zucc.edu.cn/user/uc/showOpacinfo.jspx", cookies=l.cookies)
# from app.action import get_jwxt
#
# myclass = get_jwxt.myJwxtInfo('31308023', 'wjzwl222')
# myindexreader = myclass.jwxt_Login()
# if not myclass.before_getCurriculum(myindexreader):
# 	print('登录失败')
# 	#t1 = myclass.getCurriculum(myclass.before_getCurriculum(myindexreader))
#
# import requests
#
#
# try:
# 	CheckCode_file = open("D:/Downloads/1.gif", 'w+b')
# 	CheckCode_file.write(requests.get("http://124.160.104.166/(ly4cbj55dzuvnumdthpxgkqw)/CheckCode.aspx", stream = True).content)
# except IOError:
# 	print("IOError\n")
# finally:
# 	CheckCode_file.close()
# 	yzm = raw_input("yzm= ")
# login_postData = {
#             '__VIEWSTATE': 'dDwyODE2NTM0OTg7Oz7r5LOCfUV7vFG62JP9rMYu0xxl0A==',
#             'txtUserName': 31207311,
#             'TextBox2': 'hello123',
#             'txtSecretCode': yzm,
#             'RadioButtonList1': '%D1%A7%C9%FA',
#             'hidPdrs': '',
#             'lbLanguage': '',
#             'Button1': '',
#             'hidsc': ''
#             }
#
# index_read = requests.post("http://124.160.104.166/(ly4cbj55dzuvnumdthpxgkqw)/default2.aspx",data=login_postData)
# print(index_read.text)