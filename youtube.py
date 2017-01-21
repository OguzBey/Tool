#!/usr/bin/python2.7
#! -*- coding: utf-8 -*-
"""
  ____                          _   ____                 _____ 
 / ___|___  _ ____   _____ _ __| |_|___ \ _ __ ___  _ __|___ / 
| |   / _ \| '_ \ \ / / _ \ '__| __| __) | '_ ` _ \| '_ \ |_ \ 
| |__| (_) | | | \ V /  __/ |  | |_ / __/| | | | | | |_) |__) |
 \____\___/|_| |_|\_/ \___|_|   \__|_____|_| |_| |_| .__/____/ 
                                                   |_|         Bot :) v4

				Author : OguzBey
				v4 by blackvkng
				Ampülü yeniden bulmaya gerek yok :)
"""
import mechanize,re,sys,getpass
def bilgi():
		print "[*] Example usage:\n[*] python youtube.py -u https://www.youtube.com/watch?v=o9vhJ-UTdBA --> for mp3"
		print "[*] python youtube.py -v https://www.youtube.com/watch?v=o9vhJ-UTdBA 360 --> for mp4"
		print "[*] python youtube.py -f file.txt --> from file, for mp3"
		print "[*] python youtube.py -fv file.txt 360 --> from file, for mp4"

br = mechanize.Browser()
br.set_handle_robots(False)
url = "http://convert2mp3.net/en/index.php"
k_adi = getpass.getuser()
if os.name == "nt":
	dizin = "C:\\Users\\%s\\Desktop"%(str(k_adi))
else:
	if k_adi != "root":
		try:
			os.chdir("/home/"+k_adi+"/Masaüstü/")
			dizin = "/home/"+k_adi+"/Masaüstü/"
		except OSError:
			os.chdir("/home/"+k_adi+"/Desktop/")
			dizin = "/home/"+k_adi+"/Desktop/"

	else:
		try:
			os.chdir("/root/Masaüstü/")
			dizin = "/root/Masaüstü/"
		except OSError:
			os.chdir("/root/Desktop/")
			dizin = "/root/Desktop/"
try:
	def video_bot(y_url,v_kalite):
		br.open(url)
		br.select_form(name="convertForm")
		br['url'] = y_url
		br['format'] = ["mp4"]
		br['quality'] = [v_kalite]
		br.submit()
		y = []
		for link in br.links():
			y.append(link.url)
		url2 = y[10]
		br.open(url2)
		for i in br.links():
			url3 =  i.url
		a = br.open(url3)
		kaynak_kod = a.read()
		parcala = re.findall('<b>(.*?)</b>',kaynak_kod)
		isim_dizin_2 = dizin+parcala[0]+".mp4"
		son_y = []
		for i in br.links():
			son_y.append(i.url)
		print "[>] %s indirilmeye baslandi..."%(parcala[0])
		br.retrieve(son_y[9],isim_dizin_2)
		print "-"*80
	def mp3_bot(y_url):
		br.open(url)
		br.select_form(name="convertForm")
		br['url'] = y_url
		br['format'] = ["mp3"]
		br.submit()
		x = []
		for link in br.links():
			x.append(link.url)
		link2 =  x[10]
		asd = br.open(link2)
		for a in br.links():
			git = a.url
		asdf = br.open(git)
		kaynak_kod =  asdf.read()
		parcala2 = re.findall('>(.*?)</option>',kaynak_kod)
		isim = parcala2[7]
		isim_dizin = dizin+isim+".mp3"
		parcala = re.findall('<audio src="(.*?)"',kaynak_kod)
		indir = parcala[0]
		print "[>] %s indirilmeye baslandi..."%(str(isim))
		br.retrieve(indir,isim_dizin)
		print "-"*80
except Exception, e :
	print "HATA !!!!!! >> %s" %e
	bilgi()
try:
	if sys.argv[1] == "-u":
		if sys.argv[2]:
			y_url = sys.argv[2]
			mp3_bot(y_url)
		else:
			bilgi()
	elif sys.argv[1] == "-v":
		if sys.argv[2]:
			y_url = sys.argv[2]
			kalite = sys.argv[3]
			video_bot(y_url,kalite)
		else:
			bilgi()
			
	elif sys.argv[1] == "-fv":
		if sys.argv[2]:
			y_url = open(sys.argv[2], "r").read().split("\n")
			kalie = sys.argv[3]
			y_url = open(sys.argv[2], "r").read().split("\n")
			print "[.] Loaded %s link(s)"%(len(y_url))
			for i in y_url:
				print "--> %s"%(str(i))
			print "="*80+"\n"
			for i in y_url:
				video_bot(i, kalie)
		else:
			bilgi()
			
	elif sys.argv[1] == "-f":
		if sys.argv[2]:
			y_url = open(sys.argv[2], "r").read().split("\n")
			print "[.] Loaded %s link(s)"%(len(y_url))
			for i in y_url:
				print "--> %s"%(str(i))
			print "="*80+"\n"
			for i in y_url:
				mp3_bot(i)
		else:
			bilgi()
			

except:
	bilgi()
