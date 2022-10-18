# -*- coding: utf-8 -*-
# @Time    : 2022/10/17 21:34
# @Author  : Saiterlz from lanzhou
# @Email   : kinekok@163.com
# @File    : get_item_id_and_name_from_db-nfuwow.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
from lxml import etree
items_file = "./test_get_item_id.txt"
save_file = "./WOTLK_ID.txt"
url_template="http://db.nfuwow.com/80/?item="
headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42",
	"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5"
	}   #以字典的形式设置请求头，处理反爬

"""
GET /80/?item=38908 HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5
Cache-Control: no-cache
Cookie: PHPSESSID=9nki8b64efbk3vqh6ctje84o5e
Host: db.nfuwow.com
Pragma: no-cache
Proxy-Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42

"""

results = []
# 追加写入到文件中
"""
r：只读模式（默认）
w：写模式
a：追加模式
+：读写模式
b：二进制模式，例如声音，视频，图像等
"""
def to_write(filename,word):
	with open(filename,'a+') as f:
		f.write(word+"\n")


if __name__ == '__main__':

	# 创建CSS选择器
	define_select = '#main-contents > div.text > div.textbox > h1'
	with open(items_file, 'r', encoding='utf-8') as f:

		dic = []
		for line in f.readlines():
			item = line.split(":")
			print(item)
			url = url_template+item[0]
			print(url)
			resp=requests.get(url,headers=headers,timeout=60)
			# print(resp)  #结果：<Response [200]>
			# print(resp.text) #拿到页面源代码
			# resutl = BeautifulSoup(resp.text, 'lxml')
			result = etree.HTML(resp.text)
			# print(result)
			item_name = result.xpath("/html/body/div[2]/div/div[2]/div[4]/div[2]/div[1]/div[2]/h1/text()")
			if item_name:
				make_line = str(item[0]) + ":" + str(item_name[0])
				print(make_line)
			else:
				make_line = str(item[0]) +":" +"这个物品不存在"
			# print(bs.find_all(class_='aaa'))
			# //*[@id="main-contents"]/div[1]/div[2]/h1
			# resp.close()  #关掉resp

			# line = line.strip('\n')  # 去掉换行符\n
			# b = line.split(':')  # 将每一行以空格为分隔符转换成列表
			# dic.append(b)
			import time,os
			import random
			time.sleep(random.randint(1,5)+random.random())
			# results.append(make_line)
			to_write(save_file,make_line)





print("全部获取完成!")
