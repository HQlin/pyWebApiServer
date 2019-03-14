#!/usr/bin/python
# -*- coding: UTF-8 -*-

#开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件   
import logging

#用字典保存日志级别
format_dict = {
	10 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
	20 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
	30 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
	40 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
	50 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
}

class Logger():
	def __init__(self, logname, loglevel, logger):
		'''
			指定保存日志的文件路径，日志级别，以及调用文件
			将日志存入到指定的文件中
		'''

		# 创建一个logger
		self.logger = logging.getLogger(logger)
		self.logger.setLevel(logging.DEBUG)

		#NOTSET 0< DEBUG 10< INFO 20< WARNING 30< ERROR 40< CRITICAL 50
		# 创建一个handler，用于写入日志文件
		fh = logging.FileHandler(logname)
		fh.setLevel(loglevel)

		# 再创建一个handler，用于输出到控制台
		ch = logging.StreamHandler()
		ch.setLevel(loglevel)

		# 定义handler的输出格式
		#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		formatter = format_dict[int(loglevel)]
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)

		# 给logger添加handler
		self.logger.addHandler(fh)
		self.logger.addHandler(ch)

	def getlog(self):
		return self.logger

	def getExceptError(self):
		self.logger.error("=== STEP ERROR INFO START")
		import traceback         
		self.logger.error(traceback.print_exc())
		import sys
		s=sys.exc_info()
		self.logger.error("Error '%s' happened on line %d" % (s[1],s[2].tb_lineno))
		self.logger.error("=== STEP ERROR INFO END")
