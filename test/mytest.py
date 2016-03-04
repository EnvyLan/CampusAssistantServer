#coding=utf-8
__author__ = 'EnvyLan'

# from app.action import get_jwxt
#
# myclass = get_jwxt.myJwxtInfo('31308023', 'wjzwl222')
# myindexreader = myclass.jwxt_Login()
# if not myclass.before_getCurriculum(myindexreader):
# 	print('登录失败')
# 	#t1 = myclass.getCurriculum(myclass.before_getCurriculum(myindexreader))
#
import requests

login_postData = {
            '__VIEWSTATE': 'dDwyODE2NTM0OTg7Oz7r5LOCfUV7vFG62JP9rMYu0xxl0A==',
            'txtUserName': 31207311,
            'TextBox2': 'hello123',
            'txtSecretCode': '5bnp',
            'RadioButtonList1': '%D1%A7%C9%FA',
            'hidPdrs': '',
            'lbLanguage': '',
            'Button1': '',
            'hidsc': ''
            }

index_read = requests.post("http://124.160.104.166/(ly4cbj55dzuvnumdthpxgkqw)/default2.aspx",data=login_postData)
print(index_read.text)