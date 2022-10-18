# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 11:55
# @Author  : Saiterlz from lanzhou
# @Email   : kinekok@163.com
# @File    : get_item_id_form_nfuwow.py
# @Software: PyCharm


# http://db.nfuwow.com/70/?item=13477


from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配`
import urllib.request, urllib.error  # 制定URL，获取网页数据
import requests

# import xlwt  # 进行excel操作
# <h1 class="textbox-h1">éæ¹ï¼ä¼è´¨æ³åè¯æ°´</h1>
findName = re.compile(r'<h1 class="textbox-h1">(.*)</h1>')

id_list = []
with open('test222.txt', mode='r', encoding='utf-8') as f:
    for i in f.readlines():
        id_list.append(i.split()[0])

print(id_list)


# id_list =
def main():
    baseurl = "http://db.nfuwow.com/70/?item="  # 要爬取的网页链接
    # 1.爬取网页
    datalist = getData(baseurl, id_list)
    savepath = "test_getID_to_excel.txt"  # 当前目录新建XLS，存储进去
    # dbpath = "movie.db"              #当前目录新建数据库，存储进去
    # 3.保存数据
    # saveData(datalist,savepath)      #2种存储方式可以只选择一种
    with open(savepath, mode='a+', encoding='utf-8') as f:
        for i in range(len(datalist)):
            f.write(id_list[i] + ':' + datalist[i] + '\n')
    # saveData2DB(datalist,dbpath)


def getData(baseurl, idlist):
    datalist = []  # 用来存储爬取的网页信息
    for i in range(len(idlist)):  # 调用获取页面信息的函数，10次
        url = baseurl + str(idlist[i])
        print(url)
        html = askURL(url)  # 保存获取到的网页源码
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('h1', class_="textbox-h1"):
            # print(type(item))
            # print(item)
            get_name = re.findall(findName, str(item))[0]
            print(get_name)
            datalist.append(get_name)
    return datalist


def askURL(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    # request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        # response = urllib.request.urlopen(request)
        response = requests.get(url, headers=headers)
        print(response.encoding)
        html = response.text
        html = html.encode(response.encoding)
        html = html.decode('utf-8')
    except requests.exceptions.ConnectionError as e:
        print(e)
    return html


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
    # init_db("movietest.db")
    print("爬取完毕！")
