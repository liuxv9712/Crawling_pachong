import requests
#360的关键词接口：http://www.so.com/s?q=keyword
keyword = "Python"#搜索的关键词
try:
    kv = {'q':keyword}#构造的搜索键值对
    r = requests.get("http://www.so.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
except:
    print('Crawling failure')