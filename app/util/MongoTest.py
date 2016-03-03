__author__ = 'EnvyLan'
from flask import Blueprint
api1 = Blueprint('api1', __name__)

@api1.route('/test')
def test():
	return "helloworld"
