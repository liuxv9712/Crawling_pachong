#淘宝信息定向爬虫
#采用requests-re库实现了淘宝商品比价定向抓取
#熟练掌握正则表达式在信息提取方面的应用
import requests
import re
from bs4 import BeautifulSoup
#获得页面
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Crawling Failure"
#解析获得的HTML的页面
def parsePage(ilt,html):#ilt表示结果的列表类型
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        return "Parsing Failure"
#输出淘宝的商品信息列表
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"#指定打印出来的信息，第一个位置大小是4，第二个是8，第三个是16
    print(tplt.format("序号","价格","名称"))
    count = 0#输出信息的计数器
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))#count,g[0],g[1]对应序号","价格","名称"
#主函数
def main():
    goods = "毛衣"#搜索关键词
    depth = 2 #爬取深度
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
main()#z最后调用main函数使整个程序运行

