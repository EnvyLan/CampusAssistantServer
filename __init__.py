__author__ = 'EnvyLan'

import action.get_jwxt
from lxml import etree

jwxt_class = action.get_jwxt.myJwxtInfo(31207311,'hello123')

index_read = jwxt_class.jwxt_Login()
jwxt_class.getCurriculum(etree.HTML(index_read.text))

