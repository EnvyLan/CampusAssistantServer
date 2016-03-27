#coding=utf-8
__author__ = 'EnvyLan'
from flask import  g, request
from flask import jsonify, render_template
from app.api_1_0 import  api
from app.models.User import User
from app.action.GetJWXT import myJwxtInfo
from app.util.MongodbConnection import myConnection
from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

#
@api.route('/verify_user', methods=['post'])
@auth.verify_password
def verify_pwd():
	postData = request.get_json(force=True)
	print(postData)
	#这里说明第一次登陆，是没有token的
	if postData['token'] == "":
		print('token == ""')
		g.user = User(postData['stuId'],postData['Pwd'])
		#对账号密码进行验证
		getClass = myJwxtInfo(g.user.get_stuid(), g.user.get_pwd())
		token = g.user.generate_user_token();
		if getClass.before_getCurriculum(getClass.jwxt_Login(postData['yzm']), token):
			return jsonify({'status':'100','token': token, 'stuId':g.user.get_stuid(), 'xnd':getClass.returnXnd()})
		else:
			return jsonify({'status':'101','message':'error'})
	#有token，直接去Mongodb查找数据
	else:
		print('you token')
		if verify_token(postData['stuId'], postData['token']):
			pass
		else:
			return jsonify({'status':'101','message':'error'})

#验证token函数，以后把它改成修饰器函数，目前先调用用着
def verify_token(stuId, token):
	client_db = myConnection()
	collection = client_db['foo']
	result = collection.find_one({'stuId':str(stuId)}, {'token':1})
	if result == None:
		return False
	return token==result['token']

#获取课表，post的内容有stuID，token, xnd, xqd
@api.route('/getCurriculum', methods=['post'])
def getCurriculum():
	postData = request.get_json(force=True)
	#验证token成功
	print(postData)
	if verify_token(postData['stuId'], postData['token']):
		#从MongoDb获取课表
		print("token验证成功")
		temp = postData['xnd']+','+postData['xqd']
		myCurriculum = myConnection()['foo'].find_one({'stuId':str(postData['stuId'])}, {temp:1})
		if myCurriculum == None:
			return jsonify({'statue':'102','message':'没有找到您的课程，请重新选择学年和学期'})
		else:
			import sys
			reload(sys)
			sys.setdefaultencoding( "utf-8")
			te = myCurriculum[temp]
			list = []
			count = 0
			curriculumList = te.split('!')
			for i in range(len(curriculumList)):
				for index, j in enumerate(curriculumList[count+1]):
					if j == '{':
						#截取到周五第1，2节的结构
						temps = curriculumList[count+1][0:index]
						print('temps:'+temps)
						tempList = temps[3:-1].split(',')
						print(tempList)
						fromClassNum = int(tempList[0])
						classNumLen = int(tempList[-1]) - int(tempList[0])+1
						wek = temps[1:2]
						if wek == u'一':
							weekday = 1
						elif wek == u'二':
							weekday = 2
						elif wek == u'三':
							weekday = 3
						elif wek == u'四':
							weekday = 4
						elif wek == u'五':
							weekday = 5
						elif wek == u'六':
							weekday = 6
						elif wek == u'日':
							weekday = 7

				myDict = {
					'className':curriculumList[count],
					'fromClassNum':fromClassNum,
					'classNumLen':classNumLen,
					'weekday':weekday,
					'teacherName':curriculumList[count+2],
					'classRoom':curriculumList[count+3]
				}
				list.append(myDict)
				count = count + 4
				if count == len(curriculumList):
					break

			return jsonify({'status':'100', 'list':list})
	else:
		return jsonify({'status':'101','message':'token验证不通过，请重新登录'})


#获取成绩列表，参数为token，stuId
@api.route('/getGradeList', methods=['post'])
def getGradeList():
	postData = request.get_json(force=True)
	print(postData)
	if verify_token(postData['stuId'], postData['token']):
		s = []
		for i in myConnection()['stu_grade'].find({'stuId':str(31207311)}, {'classId':1,'className':1,'credit':1,'grade':1,'type':1}):
			i.pop('_id')
			s.append(i)
		return render_template('gradeList.html', gradeList=({'list':s}))
	else:
		return jsonify({'status':'104','message':'获取成绩错误，请重新更新您的账号'})
@api.route('/test')
def jquryTest():
	return render_template('gradeList.html', gradeList=({'list':'22'}))

@api.route('/token')
def generate_token():
	user = User(312073111,'')
	return  jsonify({'token':user.generate_user_token()})
