#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import threading
import os
import re
# import wx
# import wx.xrc
from bs4 import BeautifulSoup
from tqdm import tqdm

class MyFrame1 (threading.Thread):
	musicData  = []
	user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
	
	def __init__( self, threadID, name, counter ):
		# 多线程
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		print('playlist url:')
		self.url_text = input()


		if not os.path.exists("/Volumes/HHD/Music/music"):
			os.mkdir('/Volumes/HHD/Music/music')
		

	def __del__( self ):
		pass

	def start(self):
		# self.output_text.AppendText(u"歌曲获取成功,任务线程开启///\n")
		self.get(self.musicData)


	def main_button_click( self ):
		self.musicData = []
		self.musicData = self.getMusicData(self.url_text.replace("#/",""))

		# print('Music Data')
		# print(self.musicData)

		if len(self.musicData) >1:
			self.start()
			
	def get(self,values):
		print('number of muisc:', len(values))

		downNum    = 0
		rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
		for x in tqdm(values):
			x['name'] = re.sub(rstr, "_", x['name'])
			if not os.path.exists("/Volumes/HHD/Music/music/" + x['name'] + '.mp3'):
				print('***** ' + x['name'] + '.mp3 ***** Downloading...')
				url = 'http://music.163.com/song/media/outer/url?id=' + x['id'] + '.mp3'
				try: 
					self.saveFile(url,'/Volumes/HHD/Music/music/' + x['name'] + '.mp3')
					downNum = downNum + 1
				except:
					x = x - 1
					# self.output_text.AppendText(u'Download wrong~\n')
		# self.output_text.AppendText('Download complete ' + str(downNum) + ' files !\n')
		# pass
		pirnt('Download complete ' + str(downNum) + ' files !\n')

	def getMusicData(self,url):
		headers    = {'User-Agent':self.user_agent}

		webData    = requests.get(url,headers=headers).text
		soup       = BeautifulSoup(webData,'lxml')
		find_list  = soup.find('ul',class_="f-hide").find_all('a')

		tempArr = []
		for a in find_list:
			music_id  = a['href'].replace('/song?id=','')
			music_name = a.text
			tempArr.append({'id':music_id,'name':music_name})

		return tempArr

	def saveFile(self,url,path):
		headers = {
			'User-Agent':
				self.user_agent,
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Upgrade-Insecure-Requests':'1'}
		response = requests.get(url,headers=headers)
		with open(path, 'wb') as f:
			f.write(response.content)
			f.flush()

def main():
	frame = MyFrame1(1, "Thread-1", 1)
	frame.main_button_click()

if __name__ == '__main__':
	main()