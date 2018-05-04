# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class JingdongPipeline(object):
    def process_item(self, item, spider):
        return item



class JingdongPipeline(object):

    collection = 'jingdong_cup'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_RUI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    # 爬虫启动将会自动执行下面的方法
    def open_spider(self,spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    # 爬虫项目关闭调用的方法
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        table = self.db[self.collection]
        data = dict(item)
        table.insert_one(data)
        return "OK!"