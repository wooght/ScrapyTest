# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json

class JsPipeline(object):
    def __init__(self):
        print("----------------------------------->is runing")
        self.file = open('json/xueqiu.json','w',encoding='utf-8')
    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(line)
        return item
