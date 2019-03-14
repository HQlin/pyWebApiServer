# pyWebApiServer

## ���̼��

### python����json-rpc��WebApiServer

## �������

- **��������**
	
  > Win10 64λ + Python 2.7.14
  
- **����ģ��**
	
  > pip install jsonrpclib
  > pip install pywin32
  > pip install cx_Oracle
  > pip install pymssql
  > pip install pymysql

- **Ŀ¼�ṹ** 

  >--server    ����

        |-config.ini    �����ļ�
        |-jsonInterface.py    WebApiServer�ľ���ӿڶ���
        |-jsonServer.py    jsonrpclib��װ
        |-logger.py    ��־��
        |-PythonService.py    Windows python�����������
        |-sqlConn.py    ��ͬ���ݿ�����ݿ������װ
        |-Test.py    ��������WebApiServer

- **Windows python�����������**
	
  > ��Python27\Lib\site-packages\win32·���µ�pythonservice.exeע��һ��
  > ע�����pythonservice.exe /register

  > ��װ���� python PythonService.py install
  > �������� python PythonService.py start
  > �رշ��� python PythonService.py stop
  > �������� python PythonService.py restart
  > ж�ط��� python PythonService.py remove

## ��ϵ��Ϣ

> Address��     **����**  
> Email:        [**SwimYanglin@foxmail.com**][email-addr]  
> Github:       [**github.com/HQlin**][github-site]  

[email-addr]: mailto:SwimYanglin@foxmail.com
[github-site]: https://github.com/HQlin
