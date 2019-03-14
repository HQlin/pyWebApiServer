#!/usr/bin/python
# -*- coding: UTF-8 -*-

#����һ����־ϵͳ�� ��Ҫ����־���������̨�� ��Ҫд����־�ļ�   
import logging

#���ֵ䱣����־����
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
			ָ��������־���ļ�·������־�����Լ������ļ�
			����־���뵽ָ�����ļ���
		'''

		# ����һ��logger
		self.logger = logging.getLogger(logger)
		self.logger.setLevel(logging.DEBUG)

		#NOTSET 0< DEBUG 10< INFO 20< WARNING 30< ERROR 40< CRITICAL 50
		# ����һ��handler������д����־�ļ�
		fh = logging.FileHandler(logname)
		fh.setLevel(loglevel)

		# �ٴ���һ��handler���������������̨
		ch = logging.StreamHandler()
		ch.setLevel(loglevel)

		# ����handler�������ʽ
		#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		formatter = format_dict[int(loglevel)]
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)

		# ��logger���handler
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
