# -*- coding: utf-8 -*-

import scrapy
from wooght.items import WooghtItem     #引入容器

class DmozSpider(scrapy.Spider):
    name = 'dmoz'                       #爬虫的识别名
    allowed_domains = ['dmoz']          #
                                        #spider启动时进行怕去的url列表
    start_urls = ['http://dmoztools.net/Computers/Programming/Languages/Python/Books/']

    #爬虫默认方法
    def parse(self, response):
        #初始URL完成读取后,将生产response作为唯一参数传递给parse
        #改方法解析respose data,然后提取item,和进一步URL request

        #保存文件
        # filename = response.url.split("/")[-2]
        # with open(filename,'wb') as f:
        #     f.write(response.body)                          #根目录保存 Book,Resources文件

        #取出数据
        # for sel in response.xpath('//div/a'):
        #     #title = sel.xpath('a/text()').extract()
        #     link = sel.xpath('a/@href').extract()
        #     desc = sel.xpath('text()').extract()
        #     print(desc,link,'-------')

        #返回信息到item
        item=WooghtItem()
        for sel in response.xpath('//a[@target="_blank"]'):
            href=sel.xpath('@href').extract()
            str=sel.xpath('div/text()').extract()
            if(len(href)>0 and len(str)>0):
                item['url'] = href[0].strip()
                item['a_text'] = str[0].strip()

                yield item                                      #产出item,供pipeline使用

        #url 跟进
        url = 'http://dmoztools.net/Computers/Programming/Languages/Python/Resources/'
        #继续读取网页  及爬虫爬到新的地址,可以继续进行
        yield scrapy.Request(url,callback=self.parse)
