__author__ = 'EnvyLan'

from flask import Flask

def create_app():
	app = Flask(__name__)
	from app.api_1_0 import api as api_1_0_blueprint
	app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1')
	return app



