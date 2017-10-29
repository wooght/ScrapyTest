# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json
import time

class WooghtPipeline(object):
    def __init__(self):
        self.file = open('data.json','w',encoding='utf-8')
        print('=========================================44===============================>')
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

class SteadPipeline(object):
    def __init__(self):
        self.file = open('hoemstead.json','a+',encoding='utf-8')
        print('----------------------------------------------44------------------------>')
    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(line)
        return item

class JsPipeline(object):
    def __init__(self):
        print("----------------------------------->is runing")
        self.file = open('json/xueqiu.json','a+',encoding='utf-8')
        self.file.write("=======>"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+"<======\n")
    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(line)
        return item
