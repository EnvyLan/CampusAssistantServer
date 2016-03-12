__author__ = 'EnvyLan'
from flask import Blueprint

api = Blueprint('api', __name__)

from .import auth_jwxt, auth_unite