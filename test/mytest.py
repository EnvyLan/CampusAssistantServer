#coding=utf-8
__author__ = 'EnvyLan'
import requests
myList = u'操作系统原理!周五第1,2节{第1-17周|单周}!胡隽!理4-226!2015年01月23日(08:10-10:10)!教六406!大学物理(Ⅱ)!周二第3,4节{第1-17周}!凌俐!教五206!2015年01月18日(14:00-16:00)!教五310!操作系统原理!周三第3,4,5节{第1-17周}!胡隽!教六405!2015年01月23日(08:10-10:10)!教六406!计算机网络!周四第3,4,5节{第1-17周}!蔡建平!教五610!2015年01月23日(14:00-16:00)!教五406!数据库系统应用与管理!周五第3,4,5节{第1-17周}!罗荣良!理4-222!2015年01月25日(08:10-10:10)!教五406!计算机信息安全!周一第6,7节{第1-17周}!王云武!理4-217!2015年01月22日(14:00-16:00)!教七206!'
s = u'中文截取'
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
print(s )
s = myList.split('!')
st = s[0]
temp = [u'周一第', u'周二第', u'周三第', u'周四第', u'周五第', u'周六第',u'周日第']
l = []
for h in range(len(s)):
	if s[h].decode('utf-8')[0:3] in temp:
		l.append(s[h-1])
		l.append(s[h])
		l.append(s[h+1])
		l.append(s[h+2])
		h = h+3

s = '!'.join(l)
print(type(s))
print(s)
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