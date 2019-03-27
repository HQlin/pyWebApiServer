# pyWebApiServer

## 工程简介

### python基于json-rpc的WebApiServer

## 工程详解

- **开发环境**
	
  > Win10 64位 + Python 2.7.14
  
- **下载模块**
  ```
  pip install jsonrpclib
  pip install pywin32
  pip install cx_Oracle
  pip install pymssql
  pip install pymysql
  ```
- **目录结构** 
  ```
  --server    程序
      |-config.ini    配置文件
      |-jsonInterface.py    WebApiServer的具体接口定义
      |-jsonServer.py    jsonrpclib封装
      |-logger.py    日志类
      |-PythonService.py    Windows python程序服务设置
      |-sqlConn.py    不同数据库的数据库操作封装
      |-Test.py    测试启动WebApiServer
  --deamon.py    linux的守护进程
  ```
- **Windows python程序服务设置**
  ```
  将Python27\Lib\site-packages\win32路径下的pythonservice.exe注册一下
  注册命令：pythonservice.exe /register

  安装服务： python PythonService.py install
  启动服务： python PythonService.py start
  关闭服务： python PythonService.py stop
  重启服务： python PythonService.py restart
  卸载服务： python PythonService.py remove
  ```
## 联系信息

> Address：     **广州**  
> Email:        [**SwimYanglin@foxmail.com**][email-addr]  
> Github:       [**github.com/HQlin**][github-site]  

[email-addr]: mailto:SwimYanglin@foxmail.com
[github-site]: https://github.com/HQlin
