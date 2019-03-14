#! /usr/bin/python
# -*- coding: UTF-8 -*-

from jsonInterface import JsonInterface


interface = JsonInterface('localhost', 8080)
interface.run()