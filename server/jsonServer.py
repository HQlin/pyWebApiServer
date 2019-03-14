#! /usr/bin/python
# -*- coding: UTF-8 -*-

import threading

import jsonrpclib
import jsonrpclib.SimpleJSONRPCServer

class JsonServerThread (threading.Thread):
  def __init__(self, host, port):
    threading.Thread.__init__(self)
    self.daemon = True
    self.stopServer = False
    self.host = host
    self.port = port
    self.server = None

  def _ping(self):
    pass

  def stop(self):
    self.stopServer = True
    jsonrpclib.Server("http://" + str(self.host) + ":" + str(self.port))._ping()
    self.join()

  def run(self):
    self.server = jsonrpclib.SimpleJSONRPCServer.SimpleJSONRPCServer((self.host, self.port))
    self.server.logRequests = False
    self.server.register_function(self._ping)

    self.addMethods()

    self.server.serve_forever()
#    while not self.stopServer:
#      self.server.handle_request()
#    self.server = None

  # defined class definitions

  def addMethods(self):
    pass