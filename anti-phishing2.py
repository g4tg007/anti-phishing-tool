
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2
import threading
import sys
import os
import time
import string
from time import sleep, ctime
from random import randint

#global result
global e_code

#result=[];
e_code="403"

def outxt(file, host):
    host = '%s\n' % (host)
    fo = open(file, 'a')
    fo.write(host)
    fo.close()

def makelist():
    urls = []
    for i in range(4000, 10000):
        n=str(i)
        seed = n.zfill(4)
        url = "http://www1.jingdong"+seed+".xyz/goods.php?id=145"#http://www1.jingdong0091.xyz/goods.php?id=145
        urls.append(url)
    return urls


def checkit(url):
    try:
        headers = {
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req, timeout=20)
        html = response.read()
        print url+"---200 OK"
        outxt("website200_0112.txt",url)
#        result.append(url)
    except Exception, e:
        reason=str(e)
        print url+reason
        #if string.find(reason,e_code)==11:
            #print url+"---"+reason
           # outxt("website200.txt",url)
#            result.append(error)
    pass


def func(url):
    checkit(url)


def checklist():
    urls = makelist();
    for url in urls:
        # line=fd.readline();
        t = threading.Thread(target=func, args=(url,))
        t.start()
        time.sleep(0.009)
        while True:
            time.sleep(0.009)
            #print len(threading.enumerate())
            if(len(threading.enumerate()) < 20):
                break
    


if __name__ == "__main__":
    print "scanner start!!"
    checklist()
