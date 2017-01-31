#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"
__date__ = "15.12.2016"
__version__ = 0

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def modul():
	global xerox
	global getpass
	global os
	try:
	    import pip
	except ImportError:
	    import urllib2, sys, os
	    urllib2.urlopen("https://bootstrap.pypa.io/get-pip.py").read()
	    dosya = open("get-pip.py", "w").write(urllib2.urlopen("https://bootstrap.pypa.io/get-pip.py").read())
	    os.system("sudo "+sys.executable + " get-pip.py")

	def yukle(module):
	    pip.main(['install', module])

	try:
	    import xerox
	except ImportError:
	    yukle("xerox")

	import getpass, os

def listen():
	file = open("musics.txt", "a")
	while True:
		try:
			if "youtube" in xerox.paste() and "watch" in xerox.paste():
				url = xerox.paste()
				file.write(url+"\n")
				xerox.copy("Tamamdir")
				print "[>] Dosyaya yazılan: %s"%(url)
			else:
				pass
		except KeyboardInterrupt:
			print "[!] CTRL+C algılandı, çıkılıyor..."
			sys.exit(0)

if __name__ == "__main__":
	modul()
	listen()
