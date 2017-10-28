# -*- coding: utf-8 -*-
import scrapy
from wooght.items import SteadItem     #引入容器

from scrapy.http import Request, FormRequest, HtmlResponse


class SteadSpider(scrapy.Spider):
    name = 'Stead'
    allowed_domains = ['homestead']
    urls = ['http://homestead/admin/login']
    user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    headers={
        'User-Agent':user_agent,
        'Referer':urls[0],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded"}
    posts = {'email':'wooght@126.com','password':'111111'}

    #重写开始请求函数
    def start_requests(self):
        return [Request(self.urls[0],
    meta={'cookiejar':1},callback=self.parse)]

    def parse(self, response):
        #得到响应cookie
        # cookie = response.headers.getlist('Set-Cookie')
        # for c in cookie:
        #     print(c)

        #抓取_token
        token=response.xpath('//input[@name="_token"]')
        # print('===========>',response.meta['cookiejar')
        token_str=token.xpath('@value').extract_first().strip()
        print(token_str)
        self.posts['_token'] = token_str
        return scrapy.FormRequest(
            url=self.urls[0],
            meta={'cookiejar':response.meta['cookiejar']},
            headers=self.headers,
            formdata=self.posts,callback=self.afterlogin,dont_filter=True)      # 如果地址和allowed_domains不一样dont_filter=True
    def afterlogin(self,response):
        print('----------------------------------------------')
        print('登录成功!')
        progress_group = response.xpath('//div[@class="progress-group"]')
        for item in progress_group:
            city = item.xpath('span[@class="progress-text"]/text()').extract_first().strip()
            intnum = item.xpath('div/div/@style').extract()[0]
            print(city,intnum[7:11])
