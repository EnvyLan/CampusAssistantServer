__author__ = 'EnvyLan'

from lxml import etree

from app import action

jwxt_class = app.action.get_jwxt.myJwxtInfo(31207311,'hello123')

index_read = jwxt_class.jwxt_Login()
jwxt_class.getCurriculum(etree.HTML(index_read.text))

