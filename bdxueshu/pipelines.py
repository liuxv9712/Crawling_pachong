# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
from scrapy import log
class BdxueshuPipeline(object):
    def __init__(self):
        try:
            #创建连接对象
            self.db = pymysql.connect(host='localhost', user='root', password='123456',
                                      database='bdxueshu', charset='utf8', port = 3306)
            #创建游标，游标用来进行查询，修改等操作
            self.cursor = self.db.cursor()

        except Exception as e:
            # pass
            print(e)
    def process_item(self, item, spider):
        try:
            self.db.ping(reconnect=True)
            if len(item) == 6:
                #execute()执行SQL语句
                self.cursor.execute(
                    'insert into result(title,authors,abstract,keywords,reference,doi) values (%s,%s,%s,%s,%s,%s)',
                    [ item['title'], item['authors'], item['abstract'],
                      item['keywords'],
                     item['reference'], item['doi']])

                log.msg("数据插入成功", level=log.INFO)
            else:
                return item

        except Exception as e:
            log.msg('Insert error:%s', level=log.ERROR)
            #若出现异常，回滚事务
            self.db.rollback()
        #提交对数据库所做的修改
        self.db.commit()
        return item
