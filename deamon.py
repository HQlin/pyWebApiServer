#!/usr/bin/env python
#coding: utf-8
#pythonlinux���ػ�����

import sys
import os
import time
import string
import ctypes
import datetime
#from logger import *

#logyyx = Logger('tsl.log', logging.ERROR, logging.DEBUG)

class Deamon:
    def __init__(self, pyfilename, runCmd, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.pyfilename = pyfilename
        self.findCmd = 'ps -fe |grep '+self.pyfilename+' | grep -v grep | wc -l'
        self.runCmd = runCmd
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        #self.logger = logging.getLogger()
        self.isRuning = False
    '''
    def LoggerInit(self):
        logfile = '/home/***/log/tsl.log'
        hdlr=logging.FileHandler(logfile)
        formatter = logging.Formatter('\n%(asctime)s   %(filename)s[line:%(lineno)d]   %(levelname)s\n%(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger.setLevel(logging.NOTSET)
        return
    '''
    def daemonize(self):
        try:
            #��һ��fork�������ӽ��̣����븸����
            if os.fork() > 0:
                raise SystemExit(0)      #�˳�������
        except OSError as e:
            print "fork #1 failed:\n"
            #logyyx.error("fork #1 failed:\n")
            #sys.exit(1)
            raise RuntimeError('fork #1 faild: {0} ({1})\n'.format(e.errno, e.strerror))

        os.setsid()        #�����µĻỰ����
        os.umask(0)        #���������ļ�����Ȩ��
        try:
            #�ڶ���fork����ֹ���̴��ն�
            if os.fork() > 0:
                raise SystemExit(0)
        except OSError as e:
            print "fork #2 failed:\n"
            #logyyx.error("fork #2 failed:\n")
            #sys.exit(1)
            raise RuntimeError('fork #2 faild: {0} ({1})\n'.format(e.errno, e.strerror))
        os.chdir("/")  # �޸Ĺ���Ŀ¼
        # Flush I/O buffers
        sys.stdout.flush()
        sys.stderr.flush()

        # Replace file descriptors for stdin, stdout, and stderr
        with open(self.stdin, 'rb', 0) as f:
            os.dup2(f.fileno(), sys.stdin.fileno())
        with open(self.stdout, 'ab', 0) as f:
            os.dup2(f.fileno(), sys.stdout.fileno())
        with open(self.stderr, 'ab', 0) as f:
            os.dup2(f.fileno(), sys.stderr.fileno())

        return

    def start(self):
        self.isRuning = True
        #���pid�ļ��Ƿ������̽���Ƿ���ڽ���
        esb = os.popen(self.findCmd).read().strip()
        if not (esb == '0'):
            print"the deamon is already running!!!"
            return
        else:
            #�������
            self.daemonize()
            self.run()

    def run(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        while self.isRuning:
            try:
                esb = os.popen(self.findCmd).read().strip()
                if (esb == '0'):
                    #logyyx.info("deamon on  %s" %now)
                    print "deamon on  %s" %now
                    os.system(self.runCmd)
            except:
                pass
            time.sleep(10)

    def KillPid(self,name):
        ps_str = 'ps aux |grep '+name+' | grep -v grep'
        x= os.popen(ps_str).read()
        if x:
            proc = x.split('\n')
            for line in proc:
                print line
                try:
                    proc_id = line.split()[1]
                    os.system('kill -9 %s' % proc_id)
                except:
                    pass
        else:
            return

    def checkpid(self, name):
        findCmd='ps -fe |grep '+name+' | grep -v grep | wc -l'
        esb = os.popen(findCmd).read().strip()
        if not (esb == '0'):
            #ɱ����
            try:
                self.KillPid(name)
            except:
                print"kill %s failed!!!" % name
                logyyx.error("the deamon  %s  kill failed" % name)
                return
        return
    def stop(self):
        self.isRuning = False
        self.checkpid(self.pyfilename)
        self.checkpid(os.path.split(_file_)[-1])#��ȡ����������
        return


if __name__ == "__main__":
    pyfilename = './server/Test.py'
    runCmd = 'python '+pyfilename
    LOG = './tsl.log'
    deamon = Deamon(findCmd, runCmd, stdout=LOG, stderr=LOG)

    if len(sys.argv) != 2:
        print('Usage: {} [start|stop]'.format(sys.argv[0]))
        raise SystemExit(1)
    if 'start' == sys.argv[1]:
        deamon.start()
    elif 'stop' == sys.argv[1]:
        deamon.stop()
    else:
        print('Unknown command {0}'.format(sys.argv[1]))
        raise SystemExit(1)