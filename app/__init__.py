__author__ = 'EnvyLan'

from flask import Flask
from flask import request

app = Flask(__name__)

from api_1_0 import api as api_1_0_blueprint
app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

@app.route("/hello")
def hello():
	return "<h1>helloworld</h1>"
if __name__ == '__main__':
    app.run(debug=True)

