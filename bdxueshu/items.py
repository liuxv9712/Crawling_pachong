# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BdxueshuItem(scrapy.Item):
    # define the fields for your item here like:
    # 名称，作者，摘要，关键词、被引量和 DOI：数字对象唯一标识，被喻为“互联网上的条形码”,通过它可以方便、可靠地链接到论文全文。

    title = scrapy.Field()
    authors = scrapy.Field()
    abstract = scrapy.Field()
    keywords = scrapy.Field()
    reference = scrapy.Field()
    doi = scrapy.Field()
