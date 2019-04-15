#coding=utf8
from lxml import etree
with open(r'D:\someFile\PyCharm\work\bdxueshu\bdxueshu\test.html','r',encoding='utf-8')as ff:
    response= ff.read()
# response = response.replace('\n', '').replace('\t', '').replace(' ', '').replace('\r', '')
response = etree.HTML(response)
item={}
item['title'] = response.xpath('//div[@id="dtl_l"]/div[@class="main-info"]/h3/a')[0]
item['anthors'] = response.xpath( '//div[@class="author_wr"]/p[@class="author_text"]/span/a')[0]
item['abstract'] = response.xpath('//div[@class="abstract_wr"]/p[@class="abstract"]')[0]
keywords_info = response.xpath('//div[@class="kw_wr"]/p[@class="kw_main"]/span/a')
# print(keywords_info)
keywords = ''
for i in keywords_info:
    keywords =keywords+i.text+','
print(keywords)

# item['abstract'] = response.xpath('//div[@class="abstract_wr"]/p[@class="abstract"]')[0]
# item['doi'] = response.xpath('//div[@class="doi_wr"]/p[@class="kw_main"]')[0]
# print(item['doi'].text)

# print(item['keywords'])
# print(response)
