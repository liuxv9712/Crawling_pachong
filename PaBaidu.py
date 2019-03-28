import requests
#百度的关键词接口：http://www.baidu.com/s?wd=keyword
keyword = "Python"#搜索的关键词
try:
    kv = {'wd':keyword}#构造了一个键值对，wd表示的是搜索引擎接口前的标识
    r = requests.get("http://www.baidu.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('Crawling failure')