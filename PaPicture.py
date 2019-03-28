#网络图片的爬取并保存：网络图片链接的格式http://www.example.com/picture.jpg
import requests
import os

url = "http://img0.dili360.com/pic/2018/10/25/5bd167f5a541c7u07539289.jpg"
root = "D:/tempFile/picture"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("The file has been saved successfully")
    else:
        print('The file has existed')
except:
    print('Crawling failure')

