import requests
import time

count = 0
url = "https://www.baidu.com"
start = time.perf_counter()

while count < 100:
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        count +=1
        print("成功爬取{}次".format(count))
    except:
        print("第{}次爬取网站失败".format(count+1))

end = time.perf_counter()

print("成功爬取100次{}\n所需时间为：{:.2f}秒".format(url,end-start))



