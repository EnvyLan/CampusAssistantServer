__author__ = 'EnvyLan'

from flask import Flask




print('hahahha')

def create_app():
	app = Flask(__name__)
	from app.api_1_0 import api as api_1_0_blueprint
	from util.MongoTest import api1 as api1
	app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1')
	app.register_blueprint(api1, url_prefix='/t')
	return app



