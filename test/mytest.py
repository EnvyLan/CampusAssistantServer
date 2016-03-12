#coding=utf-8
__author__ = 'EnvyLan'
import requests
s = "http://ms.zucc.edu.cn:8080/sms/opac/user/lendStatus.action?sn=223B9A1BD48F7D670C57521A003A1BE401D1E0AB0CC6C4C843C442C345F3D32F64718B7D5FB4C4631017B3185E0DC9A56FE4B29FFDC1529003ED58299D88FC50750D74CB32C089EA&xc=0"
print(s[:-1]+'3')

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