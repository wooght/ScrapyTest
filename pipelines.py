# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json

class WooghtPipeline(object):
    def __init__(self):
        #打开文件,设定打开编码类型
        self.file = open('data.json','w',encoding='utf-8')

    #pipeline 主函数 用于处理item数据
    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    #spider 被开启的时候调用此函数
    def open_spider(self,spider):
        pass

    #spider 被关闭时调用此函数
    def close_spider(self,spider):
        pass
