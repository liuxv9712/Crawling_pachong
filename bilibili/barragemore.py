import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
from matplotlib import pyplot as plt

#输入cid,可以多个
cids = input('请输入cid,如果输入多个，请用英文的逗号隔开：')
cids = cids.split(',')

#拼接出完整的url
def get_url(cids):
    urllst = []
    for i in cids:
        urllst.append('http://comment.bilibili.com/%s.xml'%i)
    return urllst
#这里可以优化
urllst = get_url(cids)

#获取url里面的弹幕，并转为list
def get_data(url):
    r = requests.get(url)
    r.encoding = 'utf8'
    soup = BeautifulSoup(r.text,'lxml')
    d = soup.find_all('d')
    dlst = []
    n = 0
    for i in d:
        n+=1
        danmuku = {}
        danmuku['弹幕'] = i.text
        danmuku['网址'] = url
        danmuku['时间'] = datetime.date.today()
        dlst.append(danmuku)
    print('共爬取了%i条数据'%n)
    return dlst
#将多个网址的弹幕拼接到一个list中
def cycle_url(dlst):
    data_all = []
    total_lst = []
    for url in urllst:
        lst = get_data(url)
        data_all.append(lst)
    for single_lst in data_all:
        for single_data in single_lst:
            total_lst.append(single_data)
    return total_lst
#将列表转换为DataFrame
df = cycle_url(urllst)
df = pd.DataFrame(df)
print(df)
#把数据放到Excel里
df.to_excel('B站弹幕数据more.xlsx')

