# CampusAssistantServer
校园助手APP Server端。提供restful形式的接口调用

/app/static/requirement.txt 是程序所需要的组件，通过 pip install -r requirements.txt安装

1.简介
  本系统使用request+lxml抓取学校的校园服务网站，把抓取到的数据格式化为json格式的文档，存入Mongodb数据库，最后通过flask编写成RESTful的API接口供调用。Android客户端项目在CampusAssistantAndroidClient里
  
