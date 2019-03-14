#!/usr/bin/python
# -*- coding: UTF-8 -*-

import jsonServer
from sqlConn import SqlConn
import json
from logger import Logger

#配置文件主要和执行文件同目录
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open('config.ini'))
ip = config.get("config","ip")
port = config.get("config","port")
logpath = config.get("config","logpath")
loglevel = config.get("config","loglevel")

srcDbtype = config.get("config","srcDbtype")
srcServer = config.get("config","srcServer")
srcUser = config.get("config","srcUser")
srcPassword = config.get("config","srcPassword")
srcDbname = config.get("config","srcDbname")

logger = Logger(logname=logpath, loglevel=int(loglevel), logger="jsonInterface.py")

class JsonInterface(jsonServer.JsonServerThread):
	def __init__(self, host, port):
		jsonServer.JsonServerThread.__init__(self, host, port)

	def addMethods(self):
		self.server.register_function(self.doOneThing)
		self.server.register_function(self.doAnother)
		self.server.register_function(self.selectTable)

	#request
	#{"jsonrpc": "2.0", "params": ["Persons","{\"Id_P\": \"0\",\"FirstName\": \"qinglin\"}",10 ,"CREATEDATE"], "id": "ilniw67c", "method": "selectTable"}
	@staticmethod
	def selectTable(table, distStr, rownum = 20, orderbydesc = ""):
		try:
			#连接数据库
			srcConn = SqlConn(dbtype = srcDbtype, userName = srcUser, password = srcPassword, host = srcServer, instance = srcDbname)
			cursor = srcConn.queryByDict(table, json.loads(distStr), rownum, orderbydesc)
			retlist = [];
			for row in cursor:
				retlist.append(json.dumps(row))
			#self.logger.getlog().info(retlist)
			return retlist
		except:
			logger.getExceptError()

	@staticmethod
	def doOneThing(obj):
		return obj

	@staticmethod
	def doAnother():
		return "why am I doing something else?"
