import requests#1
from bs4 import BeautifulSoup#2
import datetime#3
import pandas as pd#4

#获取页面数据html
url = r'https://comment.bilibili.com/78830153.xml'
r = requests.get(url)#访问url
r.encoding = 'utf8'#没有-杠
# print(r.text)#输出网页代
#解析页面
soup = BeautifulSoup(r.text,'lxml')#lxml是常用的解析器
d = soup.find_all('d')#弹幕都在d标签里，所以找到页面所有的d标签
# print(d)#输出为一个列表
# print(d[:10])可以输出指定的弹幕
#解析弹幕，将弹幕，网址，时间整理为字典，最后加和成列表，共1000条数据
dlst = []#定义最后保存数据的列表
n = 0#记录爬取了多少条数据
for i in d:
    n+=1
    danmuku = {}#将单条数据装进字典
    danmuku['弹幕'] = i.text
    danmuku['网址'] = url
    danmuku['时间'] = datetime.date.today()
    dlst.append(danmuku)#将一条条数据（字典）保存到总列表里
# print(dlst)
print("爬取了%i条数据"%n)
#将列表数据转为DataFrame数据，并保存到本地
df = pd.DataFrame(dlst)
print(dlst)
df.to_excel('B站弹幕数据.xlsx')#将爬下来的数据放到Excel里
#openpyxl是一个用于写入和读取xlsx格式的excel文件的Python模块。