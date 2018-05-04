# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    id = scrapy.Field()
    content = scrapy.Field()
    creationTime = scrapy.Field()
    productColor = scrapy.Field()
    productSize = scrapy.Field()
    userClientShow = scrapy.Field()
    userLevelName = scrapy.Field()
class IdItem(scrapy.Item):
    id = scrapy.Field()
