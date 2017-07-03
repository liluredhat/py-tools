# coding=utf-8
import urllib
from urllib2 import URLError
from datetime import *  

count = 0  
not_200 = 0

if __name__ == "__main__":
    stime = datetime.now()
    file = open("output.txt")
    file_not_200 = open("error.txt", "a")
    lines = file.readlines()
    # print lines
    for line in lines:
        line = line.strip('\n')
        if len(line) == 0:
           continue
        else:
           # print "check url ",line
           count += 1
           startTime = datetime.now()
           try:
               response = urllib.urlopen(line)
               endTime = datetime.now()
               span = (endTime - startTime).total_seconds()
               print "check url ", line, " took ", span, " s"
               if response.code == 404:
                   not_200 += 1
                   print >> file_not_200, line
           except URLError, e:
               print e.code
               if hasattr(e, 'reason'):  # stands for URLError
                print "can not reach a server,writing..."
                not_200 += 1
                print >> file_not_200, line 
               elif hasattr(e, 'code'):
                print "find http error, writing..."   
                not_200 += 1
                print >> file_not_200, line
               else:
                print "unknown error, writing..."    
                not_200 += 1
                print >> file_not_200, line    
           except Exception, e:
                not_200 += 1
                print >> file_not_200, line
    file.close()
    file_not_200.close()
    etime = datetime.now()
    totaltime = (etime - stime).total_seconds()
    print "took ", totaltime, " s"  # 代码执行完毕之后打印此提示信息
    print "total page:", count
    print "error page:", not_200  
