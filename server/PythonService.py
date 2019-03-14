#! /usr/bin/python
# -*- coding: UTF-8 -*-

import win32serviceutil
import win32service
import win32event
import os
import inspect
import servicemanager
from logger import Logger
from jsonInterface import JsonInterface

#配置文件主要和执行文件同目录
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open('config.ini'))
ip = config.get("config","ip")
port = config.get("config","port")
logpath = config.get("config","logpath")
loglevel = config.get("config","loglevel")

class PythonService(win32serviceutil.ServiceFramework):
	_svc_name_ = config.get("config","_svc_name_")
	_svc_display_name_ = config.get("config","_svc_display_name_")
	_svc_description_ = config.get("config","_svc_description_")

	def __init__(self, args):
		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
		self.run = True
		self.logger = Logger(logname=logpath, loglevel=int(loglevel), logger="PythonService.py")

	def SvcDoRun(self):
		self.logger.getlog().info("service is run....")
		try:
			#1
			#import time
			#while self.run:
			#    self.logger.getlog().info("service is 0....")
			#    time.sleep(2)
			#2
			self.interface = JsonInterface(ip, int(port))
			self.interface.run()
			win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
		except:
			logger.getExceptError()

	def SvcStop(self):
		self.interface.server.shutdown()
		self.logger.getlog().info("service is stop....")
		self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
		win32event.SetEvent(self.hWaitStop)
		self.run = False


if __name__ == '__main__':
	win32serviceutil.HandleCommandLine(PythonService)
