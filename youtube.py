#!/usr/bin/env python
#! -*- coding: utf-8 -*-
"""
  ____                          _   ____                 _____ 
 / ___|___  _ ____   _____ _ __| |_|___ \ _ __ ___  _ __|___ / 
| |   / _ \| '_ \ \ / / _ \ '__| __| __) | '_ ` _ \| '_ \ |_ \ 
| |__| (_) | | | \ V /  __/ |  | |_ / __/| | | | | | |_) |__) |
 \____\___/|_| |_|\_/ \___|_|   \__|_____|_| |_| |_| .__/____/ 
                                                   |_|         Bot :) v3

				Author : OguzBey
				Ampülü yeniden bulmaya gerek yok :)
"""
import mechanize,re,sys,getpass
def bilgi():
		print "[+] Example usage:\n[+] python youtube.py -u https://www.youtube.com/watch?v=o9vhJ-UTdBA >> mp3 İndirme"
		print "[+] python youtube.py -v https://www.youtube.com/watch?v=o9vhJ-UTdBA 360 >> video İndirme"

br = mechanize.Browser()
br.set_handle_robots(False)
url = "http://convert2mp3.net/en/index.php"
k_adi = getpass.getuser()
dizin = "/home/"+k_adi+"/Desktop/"
if k_adi == "root":
	dizin = "/"+k_adi+"/Desktop/"
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
		print " İndirme basladi"
		br.retrieve(son_y[9],isim_dizin_2)
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
		print "İndirilmeye başladı.."
		br.retrieve(indir,isim_dizin)
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
except:
	bilgi()
