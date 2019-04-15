from scrapy import Spider, Request
from selenium import webdriver


class MySpider(Spider):
    name = "my_spider"

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='D:\someFile\python3.7.0\Scripts\chromedriver.exe')
        self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        print("spider closed")
        self.browser.close()

    def start_requests(self):
        # start_urls = ['http://xueshu.baidu.com/s?wd='.format()]#format()格式化一个字符串的输出结果
        start_urls = ['http://xueshu.baidu.com/s?wd=牡丹文化']#format()格式化一个字符串的输出结果
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        domain = response.url.split("/")[-2]
        filename = '%s.html' % domain
        with open(filename, 'wb') as f:
            f.write(response.body)
        print('---------------------------------------------------')