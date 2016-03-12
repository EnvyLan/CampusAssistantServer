__author__ = 'EnvyLan'
from flask import request
from flask import jsonify

from app.api_1_0 import  api
from app.action import GetBookLendRecord


#参数有两个，学号stuId和密码Pwd，
@api.route("/virfy_unite_user", methods=['post'])
def virify_unite_user():
	postData = request.get_json(force=True)
	unite = GetBookLendRecord(postData['stuId'], postData['Pwd'])
	url = unite.getRecord()
	if url == False:
		pass
	else:
		return jsonify({'status':200, 'recordURL':url, 'token':unite.returnToken})


