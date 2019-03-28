#基于bs4的内容遍历方法
import requests
#怎么使用BeautifulSoup库呢?
from bs4 import BeautifulSoup

url = "http://python123.io/ws/demo.html"
r = requests.get(url)
r.encoding = r.apparent_encoding
demo = r.text
print(demo)
soup = BeautifulSoup(demo,'html.parser')#做成一锅汤
#提取HTML中所有URL链接
for link in soup.find_all('a'):
    #print(soup.p.prettify())
    print(link.get('href'))