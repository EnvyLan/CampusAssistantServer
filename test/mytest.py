#coding=utf-8
__author__ = 'EnvyLan'

from app.action import get_jwxt

myclass = get_jwxt.myJwxtInfo('31308023', 'wjzwl222')
myindexreader = myclass.jwxt_Login()
if not myclass.before_getCurriculum(myindexreader):
	print('登录失败')
	#t1 = myclass.getCurriculum(myclass.before_getCurriculum(myindexreader))

