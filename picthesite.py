#-*- coding:utf-8 -*-
import sys
import os.path
import urllib2
from PyQt4 import QtGui, QtCore, QtWebKit
import os
from pic_it2 import PageShotter
from pic_it1 import FirefoxPic
import threading
from time import sleep, ctime
from random import randint

def makelist(file):
	items=[]
	fd=open(file,'r')
	for line in fd.readlines():
		item=line.replace('\n','').replace('\r','')
		item=u'http://'+item
		items.append(item)
		pass
	fd.close()
	return items
	pass

def picpage_pyqt(url):
	app = QtGui.QApplication(sys.argv)
	#shotter = PageShotter("http://www.adssfwewfdsfdsf.com")
	shotter = PageShotter(url)
	shotter.shot()
	sys.exit(app.exec_())
	pass

def picpage_seleumn(url):
	shotter=FirefoxPic(url)
	shotter.picpage()
	pass

def func(url):
	url=checkurl(url)
	if url!=0:
		picpage_seleumn(url)
		pass
	#picpage(url)
	pass

def  checkurl(url):
	try:
		headers = {
			"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
		req = urllib2.Request(url, headers=headers)
		response = urllib2.urlopen(req, timeout=20)
		html = response.read()
		print url+"200 OK"
		return url
	except Exception, e:
		reason=str(e)
		#print url+reason
		#if string.find(reason,e_code)==11:
		print url+"---"+reason
		return 0

	pass



def picpagelist():
	urls = makelist("testurl.txt");
	for url in urls:
		# line=fd.readline();
		t = threading.Thread(target=func, args=(url,))
		t.start()
		sleep(0.009)
		while True:
			sleep(0.009)
			#print len(threading.enumerate())
			if(len(threading.enumerate()) < 20):
				break


if __name__ == "__main__":
	picpagelist()
	print u"批量截图完成！"
