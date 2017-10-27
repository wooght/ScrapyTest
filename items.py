# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#items 需要抓取数据的容器
class WooghtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()           #网页标题
    description = scrapy.Field()    #网页描述
    url = scrapy.Field()            #网页url地址
    a_text = scrapy.Field()         #地址上的文字
