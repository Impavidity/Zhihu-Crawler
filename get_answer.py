#-*- coding: utf-8 -*-
from globalVal import *
from bs4 import BeautifulSoup
import os

#https://marcovaldong.github.io/2016/08/18/Python%E7%88%AC%E8%99%AB%E7%88%AC%E5%8F%96%E7%9F%A5%E4%B9%8E%E5%B0%8F%E7%BB%93/

def get_answer(questionID):
	url = 'http://www.zhihu.com/question/' + str(questionID)
	data = s.get(url, headers=headers)
	soup = BeautifulSoup(data.content, 'lxml')
	# Get titile
	title = soup.title.string.split('\n')[2]
	path = title
	if not os.path.isdir(path):
		os.mkdir(path)
	# Get Description
	description = soup.find('div',{'class':'zm-editable-content'}).strings
	file_name = path + '/description.txt'
	fw = open(file_name, 'w')
	for each in description:
		each = each.encode('gbk','ignore') + '\n'
		fw.write(each)
	# Get answer number
	ans_num = int(soup.find('h3', {'id': 'zh-question-answer-num'}).string.split()[0])
	num = 1
	index = soup.find_all('div',{'tabindex':'-1'})
	for i in range(len(index)):
		print "Scrapying the " + str(num) + 'th answer'
		try:
			a = index[i].find('a',{'class':'author-link'})
			title = str(num) + '_' + a.string.encode('gbk','ignore')
			href = 'http://www.zhihu.com' + a['href']
		except:
			title = str(num) + '_Wuming'
		answer_file_name = path + '/' + title.decode('gbk') + '.txt'
		fr = open(answer_file_name,'w')
		try:
			answer_content = index[i].find('div',{'class':'zm-editable-content clearfix'})
		except:
			answer_content = ["Nothing"]
		for content in answer_content:
			#fr.write(str(content).encode('utf-8')+'\n')
			print content
		num += 1