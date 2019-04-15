import time
from urllib import parse
from scrapy import Request
import scrapy
from bdxueshu.items import BdxueshuItem


class BdxueshuSpider(scrapy.Spider):
    name = 'bdxueshu'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    # 设定域名
    allowed_domains = ['xueshu.baidu.com']

    def start_requests(self):
        # start_urls = ['http://xueshu.baidu.com/s?wd='.format()]#format()格式化一个字符串的输出结果
        # 设置第一个爬取的URL
        start_urls = []
        num = 0
        while num < 470:
            url = 'http://xueshu.baidu.com/s?wd=牡丹文化&pn={0}&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_hit=1'.format(num)
            num += 10
            start_urls.append(url)

        for url in start_urls:
            yield Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        # 初始化Item
        # item = BdxueshuItem()
        # 利用xpath筛选想要爬取的数据,先获取到每篇文章的url
        entry_url_info = response.xpath('//div[@class="sc_content"]/h3')

        # url_params = entry_url_info[0].xpath('./a/@href').extract_first()
        # url = parse.urljoin(response.url, url_params)
        # # entry_url_list.append(url)
        # yield scrapy.Request(url=url, headers=self.headers, callback=self.parse_url)

        # # entry_url_list = []
        for i in entry_url_info:
            # print(i)
            # title = i.xpath('./a/@title').extract_first()
            url_params = i.xpath('./a/@href').extract_first()
            url = parse.urljoin(response.url, url_params)
            # entry_url_list.append(url)
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse_url)

    def parse_url(self,response):
        # 初始化Item
        item = BdxueshuItem()
        item['title'] = response.xpath('//div[@id="dtl_l"]/div[@class="main-info"]/h3/a/text()').extract_first('null')
        item['authors'] = response.xpath('//div[@class="author_wr"]/p[@class="author_text"]/span/a/text()').extract_first('null')
        item['abstract'] = response.xpath('//div[@class="abstract_wr"]/p[@class="abstract"]/text()').extract_first('null')
        keywords_info = response.xpath('//div[@class="kw_wr"]/p[@class="kw_main"]')
        keywords = keywords_info.xpath('string(.)').extract_first('null')
        # for i in keywords_info:
        #     keywords = keywords + i.extract_first() + ','
        item['keywords']=self.format_str(keywords)
        item['reference'] = self.format_str(response.xpath('//div[@class="ref_wr"]/p[@class="ref-wr-num"]/a/text()').extract_first('null'))
        item['doi'] = self.format_str(response.xpath('//div[@class="doi_wr"]/p[@class="kw_main"]/text()').extract_first('null'))

        # for key,value in item:
        #     item[key]=self.format_str(value)
        yield item


    def format_str(self,str):
        return str.replace('\n', '').replace('\t', '').replace(' ', '').replace('\r', '')