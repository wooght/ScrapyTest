# -*- coding: utf-8 -*-

import scrapy
from wooght.items import JsItem                                 #引入容器

from scrapy.http import Request, FormRequest, HtmlResponse      #应用到FormRequest来post提交,Request请求cookie


class SteadSpider(scrapy.Spider):
    name = 'Js'
    allowed_domains = ['xueqiu']                                                #规定本spider的地址域
    urls = ['https://xueqiu.com/ask/square']
    #headers 部分
    user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    headers={
        'User-Agent':user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded"}

    #重写开始请求函数
    def start_requests(self):
        return [Request(self.urls[0],meta={'cookiejar':1},callback=self.parse)] #请求网页,并把cookie保存在meta中

    def parse(self, response):
        #得到响应cookie
        # cookie = response.headers.getlist('Set-Cookie')
        # for c in cookie:
        #     print(c)

        return scrapy.FormRequest(
            url=self.urls[0],
            meta={'cookiejar':response.meta['cookiejar']},
            headers=self.headers,
            callback=self.afterlogin,dont_filter=True)
    def afterlogin(self,response):
        items=JsItem()
        progress_group = response.xpath('//div[@class="ask-item"]')
        for item in progress_group:
            items['ask'] = item.xpath('p[@class="ask-item-status"]/text()').extract_first().strip()
            items['answer'] = item.xpath('div/div/p/text()').extract_first().strip()
            try:
                print(items['ask'],items['answer'])
            except UnicodeEncodeError as e:
                print(e)
                continue

            yield items
